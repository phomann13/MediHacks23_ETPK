from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('emai')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', cateogry='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', cateogry='error')
        elif password1 != password2:
            flash('Passwords don\t match.', cateogry='error')
        elif len(password1) < 7:
            flash('Email must be greater than 6 characters.', cateogry='error')
        else:
            flash('Account created!', cateogry='success')
            # add user to database 
            
    return render_template("signup.html")