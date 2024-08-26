from flask import Blueprint, render_template, request, session, redirect, url_for

mainbp = Blueprint('main', __name__)

class User:
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.user_type = 'guest'

    def signup(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def login(self, email, password):
        self.email = email
        self.password = password

    @mainbp.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get("email")
            passwd = request.form.get("password")  # Updated to match the form field name
            print(f"Email: {email}\nPassword: {passwd}")
            # Store email in session
            session['email'] = email
            return redirect(url_for('main.dashboard'))  # Redirect to a dashboard or another page after login
        
        return render_template('login.html')

    @mainbp.route('/logout')
    def logout():
        if 'email' in session:
            session.pop('email')
        return 'User logged out'

    @mainbp.route('/dashboard')
    def dashboard():
        if 'email' not in session:
            return redirect(url_for('main.login'))
        return f"Welcome, {session['email']}! You are logged in."
