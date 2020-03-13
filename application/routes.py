from application import app
from flask import render_template, flash, redirect, url_for, request
from application.forms import LoginForm
from Api.sql_fonctions import sql_read, sql_insert

@app.route('/')
@app.route('/index')
def index():
    toi = LoginForm().username.data
    if toi is None:
        toi = 'inconnu'
    global user
    user = {'username': toi}
    sql_insert('ami', prenom='etienne', nom='mich', age=20)
    sql_insert('ami', prenom='bob', sex='M')
    amis = sql_read('ami', distinct=True)
    return render_template('index.html', title='Home', user=user, amis=amis)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Yo {} essai de s'inscrire, je me souvien tu d'une âme ? {}".format(
            form.username.data, form.remember_me.data))
        return index()
    return render_template('login.html', title='Insciption', form=form)

