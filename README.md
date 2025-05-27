# 2FA (Two-Factor Authentication) System

## Description
This project implements a Two-Factor Authentication (2FA) system using Python (Flask) for the backend and HTML/CSS for the frontend. The system provides an additional layer of security by requiring users to verify their identity using a one-time password (OTP) sent via email.

## Features
- **Email-based OTP Login**: Users receive a one-time password via email for authentication.
- **TOTP Generation**: Time-based One-Time Passwords (TOTP) are generated using the `pyotp` library.
- **Flash Messages**: User-friendly feedback messages for login and OTP verification.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Libraries**: `pyotp`, `smtplib`

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Pip (Python package manager)

### Installation
1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd "c:\Users\sagar\OneDrive\Desktop\JavaScript\JavaScript Parts\CyberSec\2FA_(Two-Factor Authentication)_System"
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
1. Open `app.py` and update the following variables with your email credentials:
   ```python
   from_email = "your_email@example.com"
   from_password = "your_email_password"
   ```
2. If you have 2FA enabled on your email account, generate an app password and use it as `from_password`.

### Running the Application
1. Start the Flask development server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
1. Enter your email and password on the login page.
2. Check your email for the OTP.
3. Enter the OTP on the verification page to complete the login process.

## Screenshots
**-- LOGIN PAGE**
<br></br>
![](https://imgur.com/6JV9JeD.png)
<br></br>
**VERIFICATION PAGE**
<br></br>
![](https://imgur.com/ZoGi6qj.png)
<br></br>
**RECEIVED MAIL**
<br></br>
![](https://imgur.com/VnEvlpo.png)
<br></br>

## Security Considerations
- Use HTTPS in production to secure communication.
- Store sensitive information like email credentials in environment variables.


## Acknowledgments
- [Flask Documentation](https://flask.palletsprojects.com/)
- [pyotp Documentation](https://pyauth.github.io/pyotp/)
