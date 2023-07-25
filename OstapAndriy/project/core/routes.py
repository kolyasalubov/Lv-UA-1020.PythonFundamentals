from datetime import datetime
from core.models import ShortUrls
from core import app, db
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for


def generate_short_id(num_of_chars: int):
    """Функція для генерації short_id із заданої кількості символів"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Будь ласка, введіть інший ідентифікатор користувача!')
            return redirect(url_for('index'))

        if not url:
            flash('Потрібна URL-адреса!')
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        flash('Недійсний URL')
        return redirect(url_for('index'))