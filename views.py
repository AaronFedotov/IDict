from flask import  render_template, url_for, request, redirect, flash, abort

from app import app
from forms import TranslationForm


@app.route('/')
@app.route('/index')
def welcome():
	return render_template('index.html', title='IDict - Homepage')

@app.route('/basic', methods=['GET','POST'])
def basic():
	form = TranslationForm()
	translation = form.entry.data
	return render_template('basic_dictionary.html', title='Basic Dictionary', form=form, translation=translation)

@app.route('/exercise')
def exercise():
	return render_template('exercise_dictionary.html', title='Exercise Dictionary')

@app.route('/quiz')
def quiz():
	return render_template('quiz_dictionary.html', title='Quiz Dictionary')

if __name__ == '__main__':
	app.run()