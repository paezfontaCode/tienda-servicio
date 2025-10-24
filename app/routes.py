from flask import Blueprint, render_template, redirect, url_for 
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('auth.login')) 

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template(f'{current_user.role}/dashboard.html')