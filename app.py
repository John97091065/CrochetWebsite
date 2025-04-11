from flask import Flask, render_template, render_template_string, request, redirect, flash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)
app.secret_key = 'ffu*@Rudb)QY#VBDQH))G33b30(*2)'

# Email credentials
EMAIL_ADDRESS = 'madebyshandy@gmail.com'
EMAIL_PASSWORD = 'otdk qjts sqrl kjck'

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/item')
def item():
    return render_template('item.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    message = request.form['message']
    file = request.files.get('attachment')

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = f"New Contact Form Submission from {name}"

    # Body of the email
    body = f"""
    Name: {name}
    Phone: {phone}
    Email: {email}
    Message: {message}
    """
    msg.attach(MIMEText(body, 'plain'))

    # If a file is uploaded and is an allowed type, attach it to the email
    if file and allowed_file(file.filename):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={file.filename}'
        )
        msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        flash('Message sent successfully!', 'success')
    except Exception as e:
        flash(f'Error sending message: {e}', 'danger')

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
