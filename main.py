from flask import Flask , render_template , request , redirect , url_for
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField , SelectField , SubmitField , PasswordField

app = Flask(__name__)

#these are dummy data to show the home
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



# class RegistrationForm(FlaskForm):
#     email = StringField('Email' , validators=[DataRequired])
#     password = PasswordField('Password' , validators=[DataRequired])
#     confirm_password = PasswordField('Confirm Password' , validators=[DataRequired])
#

@app.route('/')
def home():
    return render_template("home.html",posts=posts)

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
