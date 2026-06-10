
from app import app
from flask import render_template
from app.forms import LoginForm
from config import Config
from flask import render_template, flash, redirect, url_for

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


@app.route('/login', methods=['GET', 'POST'])
def login() :
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect('/index')
	return redirect(url_for('index'))