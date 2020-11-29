from flask import Flask, url_for, request, render_template, request, flash
from config import Config
from forms import PrimeCalc
from primecalc import prime_calc
from dashboard import today_value, last_month_value, last_year_value
import database

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
database.init_app(app)


@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello')
@app.route('/index')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    todays_value = today_value()
    last_months_value = last_month_value()
    last_years_value = last_year_value()
    return render_template('dashboard.html',title='Market Dashboard', todays_value=todays_value, last_months_value = last_months_value, last_years_value = last_years_value)

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/numbers', methods=['GET','POST'])
def numbers():
    form = PrimeCalc()
    if form.validate_on_submit():
        flash('User entered {}'.format(form.number.data))
        primes = prime_calc(form.number.data)
        flash('Prime factorization is {}'.format(primes))
    return render_template('numbersnew.html',title='Prime Calculator', form=form)

#with app.test_request_context():
#    print(url_for('index'))
#    print(url_for('profile', username='John Doe'))
#    print(url_for('static', filename='style.css'))
