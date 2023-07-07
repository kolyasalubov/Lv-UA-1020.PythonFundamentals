from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import base64
import re


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'
db = SQLAlchemy(app)


class Items (db.Model):
    idid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Integer, default=1)
    image_data = db.Column(db.LargeBinary, nullable=True)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    sort_option = request.args.get('sort')
    if sort_option == 'A-Z':
        items = Items.query.order_by(Items.title.asc()).all()
    elif sort_option == 'price-up':
        items = Items.query.order_by(Items.price.asc()).all()
    elif sort_option == 'price-down':
        items = Items.query.order_by(Items.price.desc()).all()
    elif sort_option == 'amount-up':
        items = Items.query.order_by(Items.amount.asc()).all()
    elif sort_option == 'amount-down':
        items = Items.query.order_by(Items.amount.desc()).all()

    else:
        items = Items.query.all()

    return render_template('index.html', data_=items)


@app.route('/create', methods=['POST', 'GET'])
def create_item():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        description = request.form['description']
        amount = request.form['amount']
        image_file = request.files['image']
        image_data = image_file.read()

        if not re.match(r'^[A-Za-z][A-Za-z0-9\s]{4,}$', title):
            flash('Invalid title. Only letters, numbers and spaces are allowed.')
            return redirect(url_for('create_item'))

        if not re.match(r'^[1-9]\d*$', price):
            flash(
                'Invalid price. Please enter a valid numeric value. Integer positive number')
            return redirect(url_for('create_item'))

        if not re.match(r'^[A-Za-z0-9\s_-]+$', description):
            flash('Invalid description. Only letters, numbers, and spaces are allowed.')
            return redirect(url_for('create_item'))

        if not re.match(r'^[1-9]\d*$', amount):
            flash('Invalid amount. Please enter a valid iInteger positive number')
            return redirect(url_for('create_item'))

        vendor_code = Items.query.filter_by(description=description).first()
        if vendor_code:
            vendor_code.amount = int(vendor_code.amount) + int(amount)
            db.session.commit()
            return redirect('/')
        else:
            item = Items(title=title, price=price, description=description,
                         amount=amount, image_data=image_data)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Have a misstace"

    else:
        return render_template('create.html')


@app.template_filter('b64encode')
def base64_encode(value):
    return base64.b64encode(value).decode('utf-8')


if __name__ == "__main__":
    app.run(debug=True)
