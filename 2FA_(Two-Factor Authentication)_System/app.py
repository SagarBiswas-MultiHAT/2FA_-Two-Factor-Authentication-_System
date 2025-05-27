from flask import Flask, render_template, request, redirect, url_for, flash
import pyotp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data
users = {
    "sagarbiswas.sb76@gmail.com": {
        "password": "example",
        "totp_secret": pyotp.random_base32()
    }
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email in users and users[email]['password'] == password:
        totp = pyotp.TOTP(users[email]['totp_secret'])
        otp = totp.now()

        # Send OTP via email
        send_email(email, otp)

        flash('OTP sent to your email. Please verify.\n', 'info')
        return redirect(url_for('verify', email=email))
    else:
        flash('Invalid credentials', 'danger')
        return redirect(url_for('home'))

@app.route('/verify/<email>', methods=['GET', 'POST'])
def verify(email):
    if request.method == 'POST':
        otp = request.form['otp']
        totp = pyotp.TOTP(users[email]['totp_secret'])

        # Log the OTPs for debugging
        print(f"Generated OTP: {totp.now()}")
        print(f"Entered OTP: {otp}")

        if totp.verify(otp, valid_window=2):  # Allow a tolerance of 2 time steps
            flash('OTP successfully verified! You are now logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
            return redirect(url_for('verify', email=email))

    return render_template('verify.html', email=email)

def send_email(to_email, otp):
    from_email = "eng.sagar.aiub@gmail.com"
    from_password = "use your own app password of the email account"

    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
        flash('Failed to send OTP email. Please try again later.', 'danger')

if __name__ == '__main__':
    app.run(debug=True)
