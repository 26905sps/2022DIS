from flask import Flask, render_template, request, redirect, flash, session, url_for
from datetime import datetime, date
from flask_wtf import FlaskForm
import sqlite3
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, SelectField, widgets
from wtforms.fields.html5 import DateField # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, InputRequired

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddksididkdkdl'

#connect to database
con = sqlite3.connect('user.db', check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()


# configure file uploads used when registering an act
app.config['UPLOADED_IMAGES_DEST'] = 'static/images/acts'




### Form models ####
class MultiCheckboxField(SelectMultipleField):
    # a custom object to use in SubmitVideo form,
    # need to import widgets from wtforms above
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SubmitVideo(FlaskForm):
    url = StringField('URL', validators=[DataRequired(message="You must submit a URL"), URL(message="Nota valid URL")])
    description = TextAreaField('Description', validators=[DataRequired()])
    topics = MultiCheckboxField('Topics for this video', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit URL')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


########## routes ##########
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            un = form.username.data
            pw = form.password.data
            sql = """
                    select *
                    from users
                    where userid = ?
                    and password = ?;"""

            cur.execute(sql,(un,pw))
            result = cur.fetchall()
            if len(result) == 1:
                session['userid'] = result[0][0]
                session['firstname'] = result[0][1]
                session['lastname'] = result[0][2]
                session['staffcode'] = result[0][3]
                session['isstudent'] = result[0][5]
                return redirect(url_for('home'))
            else:
                flash('Username or password incorrect, try again')


        else:
            flash("There is something missing!")
    return render_template('login.html', title='Login', form=form)

@app.route('/home')
def home():
    if session['userid']:
        id = session['userid']

        sql = """select v.videourl, t.topic, s.subject, v.description
                    from videos v, topics t, subjects s, enrolments e
                    where v.topicid = t.topicid
                    and t.subject = s.subject
                    and s.subjectid = e.subjectid
                    and userid = ?;
        """
        cur.execute(sql, (id,))
        studentresults = cur.fetchall()

        if session['staffcode']:
            sql = """select distinct v.videourl, t.topic, s.subject, v.description
                                from videos v, topics t, subjects s, enrolments e
                                where v.topicid = t.topicid
                                and t.subject = s.subject
                                and s.subjectid = e.subjectid;
                    """
            cur.execute(sql,)
            staffresult = cur.fetchall()
            return render_template('home.html',staffresults=staffresult,)
    else:
        return redirect(url_for('index'))
    return render_template('home.html', video=studentresults)

@app.route('/submit', methods=['GET','POST'])
def submit():
    if session['userid']:
        form = SubmitVideo()# get the subject & topic combinations to choose from
        my_topics = []
        sql = """select distinct t.topic, s.subject, t.topicid
                    from topics t, subjects s, enrolments e, users u
                    where t.subject = s.subject
                    and s.subjectid = e.subjectid
                    and u.userid = ?
                    order by s.subject asc, topic asc;"""
        cur.execute(sql, (session['userid'],))
        results = cur.fetchall()
        for row in results:
            my_topics.append((row['topicid'],row['topic']+' -'+row['subject']))
        form.topics.choices = my_topics

        # deal with the post data
        if request.method == 'POST':
            if form.validate_on_submit():
                #now deal with the data
                videou = str(form.url.data)
                videod = str(form.description.data)
                videotopics = form.topics.data
                print(videou, videod)

                sql_topic = """
                            select topicid
                            from topics
                            where topic = ?"""
                cur.execute(sql_topic, (videotopics))
                topicide = str(cur.fetchall())

                sql_video = """insert
                    into videos(videourl, topicid, description)
                    values(?, ?, ?);"""

                # try:
                cur.execute(sql_video,(videou,topicide,videod))
                con.commit()
                # except:
                #     flash("Oops! Something went wrong! Check the values and try again")
                # else:
                #     return redirect(url_for('index'))

    return render_template('submit.html', title = 'Submit', form = form)

@app.route('/logout')
def logout():
    if session['userid']:
    # clear out the session
        session['userid'] = None
        session['firstname'] = None
        session['lastname'] = None
        session['staffcode'] = None
        session['isstudent'] = None
        flash("You have successfully logged out")
        return redirect(url_for('index'))

@app.route('/approve')
def approve():
    if session['staffcode']:
        return(render_template('approve.html'))
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)
