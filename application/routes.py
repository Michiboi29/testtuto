from application import app
from flask import render_template, flash, redirect, url_for, request
from application.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    toi = LoginForm().username.data
    if toi is None:
        toi = 'inconnu'
    global user
    user = {'username': toi}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Yo {} essai de s'inscrire, je me souvien tu d'une âme ? {}".format(
            form.username.data, form.remember_me.data))
        return index()
    return render_template('login.html', title='Insciption', form=form)

