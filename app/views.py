from app import app, db, lm, oid
from flask import render_template, flash, redirect
import forms

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in San Jose!'
        },
        {'author': {'nickname': 'Susan'},
         'body': 'The super 8 is super boring.',
        },
    ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(flask.url_for('index'))

    form = forms.LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    else:
        return render_template('login.html',
                               title='Sign In',
                               form=form,
                               providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(init(id))
