from flask import Flask, render_template, request, redirect, flash, url_for, session
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myverysecretkey'

#########################################################################
# HTTP Routes
#########################################################################
@app.route('/')
def home():
    if request.args.get('r'):
        a = int(request.args.get('r'))
        b = random.randint(1,5)
        d = (5 + a - b) % 5
        if b == 1:
            flash('opponent plays rock')
        if b == 2:
            flash('opponent plays paper')
        if b == 3:
            flash('opponent plays scissors')
        if b == 4:
            flash('opponent plays lizard')
        if b == 5:
            flash('opponent plays spock')

        if d == 1 or d == 3:
            flash('Win')
        if d == 2 or d == 4:
            flash('Loss')
        if d == 0:
            flash('Tie')

    if request.args.get('play'):
        session['gameon'] = True

    return render_template('paper.html', gameon=session['gameon'])
#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)