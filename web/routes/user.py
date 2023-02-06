from flask import Blueprint, session, redirect, render_template, request, url_for
from .. import baseDAO, log
import re
from web.models.User import User
from web.dao.UserDAO import UserDAO

user_view = Blueprint('user_routes', __name__)
userDAO = UserDAO(baseDAO)


@user_view.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    # Check if "email" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']

        # Check if user exists using MySQL
        user = userDAO.get_user(email, password)
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['user_id'] = user.user_id
            session['user_fullname'] = user.first_name + ' ' + user.last_name
            # Redirect to home page
            return redirect(url_for('user_routes.home'))
        else:
            msg = 'User does not exist or username/password incorrect'
    return render_template('index.html', msg=msg)


@user_view.route('/logout')
def logout():
    print("logout")
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('user_fullname', None)
    # Redirect to login page
    return redirect(url_for('user_routes.login'))


@user_view.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form \
            and 'first_name' in request.form:
        # Create variables for easy access
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        admin = False

        user = userDAO.get_user_by_email(email)
        # If account exists show error and validation checks
        if user:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not first_name or not password or not email:
            msg = 'Please fill out the form!'
        else:
            user_dict = {'first_name': first_name,
                         'last_name': last_name,
                         'email': email,
                         'password': password,
                         'admin': admin}

            user = User(**user_dict)
            print(user)
            userDAO.create_user(user)
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@user_view.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', user_fullname=session['user_fullname'])
    # User is not loggedin redirect to login page
    return redirect(url_for('user_routes.login'))


@user_view.route('/profile')
def profile():
    print("Profile")
    # Check if user is loggedin
    if 'loggedin' in session:
        user_id = session['user_id']
        user = userDAO.get_user_by_id(user_id)
        return render_template('profile.html', user=user)
    return redirect(url_for('login'))
