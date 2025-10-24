#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin',
                     password=generate_password_hash('admin123'),
                     role='admin')
        db.session.add(admin)
        db.session.commit()
        print('Usuario admin creado (admin / admin123)')
    else:
        print('BD ya inicializada')