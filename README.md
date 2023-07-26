# Project: Form in Python with Flask

## Skills developed:
* Backend: PYTHON programming (introduction to logical structures)
* Sanitization and validation of a form
* Implementation of POST and GET methods
* Implementation of templates with Jinja

## Problem statement:
The company Hackers Poulette™ sells DIY kits and accessories for Rasperri Pi. They want to allow their users to contact their technical support. Your mission is to develop a Python script that displays a contact form and processes its response: sanitization, validation, and then sending feedback to the user.

## Performance criteria:
* If the user makes an error, the form should be returned to them with valid responses preserved in their respective input fields.
* Ideally, display error messages near their respective fields.
* The form will perform server-side sanitization and validation.
* If sanitization and validation are successful, a "Thank you for contacting us." page will be displayed, summarizing all the encoded information.
* Implementation of the honeypot anti-spam technique.

#### Form fields
First name & last name + email + country (list) + message + gender (M/F) (Radio box) + 3 possible subjects (Repair, Order, Others) (checkboxes). All fields are mandatory, except for the subject (in this case, the value should be "Others").

## Contact Form (Python)
* Presentation: server/client architecture (transmissive, 10")
* Sanitization: neutralizing any harmful encoding (<script>)
* Validation: mandatory fields + valid email
* Sending + Feedback
* NO NEED FOR JAVASCRIPT OR CSS

#### At the end of this project, you should be able to:
- Explain the difference between a POST request and a GET request.
- Protect yourself against XSS vulnerabilities.
- Protect yourself against SSTI attacks.
- Use a micro framework.
- Perform a deployment.
