# This script includes the information and the functions to send emails.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(filename='errors.txt', level=logging.ERROR)

SMTP_SERVER = 'smtpout.secureserver.net'
SMTP_PORT = 465

def send_email(to_name, to_email, email_option, subject_option=0, body_option=0):
    if (email_option == 1):
        username = 'swam@cognicraft.agency'
        password = "Shirtpant#23"
    elif (email_option == 2):
        username = "swam@cognicraftagency.social"
        password = "Shirtpant#23"
    elif (email_option == 3):
        username = "swam@cognicraftagency.website"
        password = "Shirtpant#23"
    
    try:
        # Set up the server
        smtp_server = SMTP_SERVER  # Replace with your SMTP server
        smtp_port = SMTP_PORT  # Replace with your SMTP port
        smtp_user = username  # Replace with your email
        smtp_password = password  # Replace with your email password

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = "Personalized Email"

        # Create the body of the message (a plain-text and an HTML version)
        text = f"Hello {to_name},\n\nThis is a personalized message."
        html = f"""\
        <html>
            <body>
                <p>Hello {to_name},<br><br>
                   This is a personalized message.</p>
            </body>
        </html>
        """

        # Attach parts into message container.
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))

        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_name} at {to_email}")

    except Exception as e:
        # Log any errors
        logging.error(f"Failed to send email to {to_name} ({to_email}): {str(e)}")
