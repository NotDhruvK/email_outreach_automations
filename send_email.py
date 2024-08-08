# This script includes the information and the functions to send emails.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(filename='errors.txt', level=logging.ERROR)

SMTP_SERVER = 'smtpout.secureserver.net'
SMTP_PORT = 465

def send_email(to_name, to_email, email_option, outreach_number):
    if (email_option == 1):
        username = "swam@cognicraft.agency"
        password = "Shirtpant#23"
    elif (email_option == 2):
        username = "swam@cognicraftagency.social"
        password = "Shirtpant#23"
    elif (email_option == 3):
        username = "swam@cognicraftagency.website"
        password = "Shirtpant#23"
    
    try:
        # Set up the server
        # Set up the server
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(username, password)
            print(f"Logged in as {username}")

            # Setting up the body
            body = f"""\
                    <html>
                        <body>
                            <p>Hey {to_name},</p>
                            <p>Been trying very hard to find your email, lol. I know this may come off as weird, but I thought I’d reach out nonetheless.</p>
                            <p>My name is Swam and I’ve been helping Therapy & Counselling Practices generate new clientele and grow their business for more than a year now.<br>
                            Our Expert Growth Program, which combines the power of AI Advertising with DCT Automated Prospecting, gets you a minimum of 10+ new client opportunities every single month!</p>
                            <p>Yes, you read that right.</p>
                            <p>We'll generate leads, work those leads, and convert them into qualified booked calls. Not just that, we will also take care of all advertising and appointment scheduling, ensuring that we deliver on our promise of providing you with a minimum of 10+ client opportunities per month.</p>
                            <p>Would you mind jumping on a quick Zoom call later this week? I'll let you in on how our Expert Growth Program exactly works. If you want, we can set it up for you or you can keep the entire thing for yourself. Seems like a win-win, right?<br>
                            Would love to provide loads of value!</p>
                            <p>Best,<br>Swam</p>
                        </body>
                    </html>
                    """
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = to_email
            msg['Subject'] = f"Hey {to_name}, are you still taking on new clients"
            msg.attach(MIMEText(body, 'html'))

            # Send the email
            server.sendmail(username, to_email, msg.as_string())
            print(f"Email sent to {to_name} at {to_email}")

    except Exception as e:
        # Log any errors
        logging.error(f"Failed to send email to {to_name} ({to_email}): {str(e)}")
