import random
import smtplib
from email.mime.text import MIMEText

# =====================================================
# Generate OTP
# =====================================================

def generate_otp():

    otp = random.randint(100000, 999999)

    return str(otp)

# =====================================================
# Send OTP Email
# =====================================================

def send_otp_email(receiver_email, otp):

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    subject = "Cybersecurity Platform MFA OTP"

    body = f"""

    Your OTP for login is: {otp}

    Do not share this OTP with anyone.
    """

    message = MIMEText(body)

    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        server.quit()

        return {

            "message": "OTP Sent Successfully"
        }

    except Exception as e:

        return {

            "error": str(e)
        }
