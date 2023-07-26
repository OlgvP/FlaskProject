from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import re

app = Flask(__name__)
app.secret_key = '6Lc9_xMUAAAAAFPVNhvDKb9lMXHGI4o7-zhqkTgL'
app.jinja_env.autoescape = True

# Function for validating email address using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

# Implement CSP after processing the request
@app.after_request
def apply_csp(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("POST METHOD")
        name = request.form.get('from')
        email = request.form.get('email')
        country = request.form.get('country')
        message = request.form.get('message')
        gender = request.form.get('gender')
        reason = request.form.getlist('reason')

        print(is_valid_email(email))

        # Validation
        errors = []
        user_input = []
        if not name:
            print('ENTERED VALIDATION - NAME FIELD')
            errors.append('Name is required.')
        #else:
            #user_input.append("Name and next name: " + name)
        if not email:
            errors.append('Email is required.')
        #else:
            #user_input.append("Email: " + email)
        if is_valid_email(email) == None:
            errors.append('Email is invalid.')
        if not country:
            errors.append('Country is required.')
        if not gender:
            errors.append('Gender is required.')
        if not reason:
            reason = ['other']  # If no other option was chosen, 'other' will be selected
        #flash(user_input)
        # Checking honeypot
        honeypot = request.form.get('honeypot')
        if honeypot:
            errors.append('Sorry, we cannot process your request at the moment.')

        # If user makes an error
        if errors:
            print(errors)
            for error in errors:
                flash(error)
        else:
            # If validation is correct, redirect to confirmation
            print(errors)
            return redirect(url_for('confirmation',
                                    name=name,
                                    email=email,
                                    country=country,
                                    message=message,
                                    gender=gender,
                                    reason=', '.join(reason)))
    return render_template('form.html')

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    email = request.args.get('email')
    country = request.args.get('country')
    message = request.args.get('message')
    gender = request.args.get('gender')
    reason = request.args.get('reason')

    return render_template('confirmation.html',
                           name=name,
                           email=email,
                           country=country,
                           message=message,
                           gender=gender,
                           reason=reason)

if __name__ == '__main__':
    app.run(debug=True)

