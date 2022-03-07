from flask import Flask, render_template, request, redirect, flash, url_for, session
app = Flask(__name__)

#########################################################################
# HTTP Routes
#########################################################################
@app.route('/')
def home():
    if request.args:
        if request.args.get('lang') != 'en':
            return 'sorry english only'
        else:
            return 'this is in english'
    else:
        return 'This is the home page route'
@app.route('/about')
def about():
    return 'You have found the about page route'

@app.route('/contact')
def contact():
    if request.args.get('source') == 'facebook':
        return'you are from facebook'
    else:
        return'You have found the contact page'
#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)