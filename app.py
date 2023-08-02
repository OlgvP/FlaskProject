from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import re
import html
import bleach
import mysql.connector


app = Flask(__name__)
app.secret_key = '6Lc9_xMUAAAAAFPVNhvDKb9lMXHGI4o7-zhqkTgL'
mydb = mysql.connector.connect(
    host="localhost",
    user="Olga",
    password="**********",
    database="databaseflask"
)

app.jinja_env.autoescape = True

# Function for validating email address using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

# Sanitize user input
def sanitize_input(input_data):
    return bleach.clean(input_data)

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
        if not name:
            print('ENTERED VALIDATION - NAME FIELD')
            errors.append('Name is required.')
        if not email:
            errors.append('Email is required.')
        if is_valid_email(email) == None:
            errors.append('Email is invalid.')
        if not country:
            errors.append('Country is required.')
        if not gender:
            errors.append('Gender is required.')
        if not reason:
            reason = ['other']  # If no other option was chosen, 'other' will be selected
     
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
            # Save data into databaseflask
            mycursor = mydb.cursor()
            sql = "INSERT INTO contacts (name, email, country, message, gender, reason) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (name, email, country, message, gender, ', '.join(reason))
            mycursor.execute(sql, val)
            mydb.commit()


            return redirect(url_for('confirmation',
                                    name=name,
                                    email=email,
                                    country=country,
                                    message=message,
                                    gender=gender,
                                    reason=', '.join(reason)))
            mycursor.close()
    return render_template('form.html')

@app.route('/confirmation')
def confirmation():
    name = sanitize_input(html.escape(request.args.get('name')))
    email = sanitize_input(html.escape(request.args.get('email')))
    country = sanitize_input(html.escape(request.args.get('country')))
    message = sanitize_input(html.escape(request.args.get('message')))
    gender = sanitize_input(html.escape(request.args.get('gender')))
    reason = sanitize_input(html.escape(request.args.get('reason')))


    return render_template('confirmation.html',
                           name=name,
                           email=email,
                           country=country,
                           message=message,
                           gender=gender,
                           reason=reason)

if __name__ == '__main__':
    app.run(debug=True)

