from flask.ext import wtf


class LoginForm(wtf.Form):
    openid = wtf.TextField('openid', validators=[wtf.Required()])
    remember_me = wtf.BooleanField('remember_me', default=False)
