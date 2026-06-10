
from app import app
from flask import render_template
from app.forms import LoginForm
from config import Config


@app.route('/')
@app.route('/index')

def index() :
	user = {'username' : 'Muzembela'}
	posts = [ 
			{
				'author' : {'username' : 'Manuel'},
				'body' : 'Beatiful Day in Belas Shopping!'
			},
			{
				'author' : {'username' : 'Bernardo'},
				'body' : 'The avengers movie are good!'
			}
			]
	return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login() :
	form = LoginForm()
	return render_template('login.html', title = 'Sign In', form=form)