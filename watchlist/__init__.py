import os
import sys
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user


WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os .path.dirname(app.root_path), 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'login'

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


from watchlist import views, errors, commands
from watchlist.models import User



