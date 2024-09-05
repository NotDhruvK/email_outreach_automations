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
        username = "swam@cognicraftagency.live"
        password = "Shirtpant#23"
    elif (email_option == 2):
        username = "swamc@cognicraftagency.live"
        password = "Shirtpant#23"
    elif (email_option == 3):
        username = "swam@cognicraftagency.solutions"
        password = "Shirtpant#23"
    elif (email_option == 4):
        username = "swamc@cognicraftagency.solutions"
        password = "Shirtpant#23"
    elif (email_option == 5):
        username = "swam@cognicraftagency.agency"
        password = "Shirtpant#23"
    elif (email_option == 6):
        username = "swamc@cognicraftagency.agency"
        password = "Shirtpant#23"
    elif (email_option == 7):
        username = "swam@cognicraftagency.tech"
        password = "Shirtpant#23"
    elif (email_option == 8):
        username = "swamc@cognicraftagency.tech"
        password = "Shirtpant#23"
    elif (email_option == 9):
        username = "swam@cognicraftagency.site"
        password = "Shirtpant#23"
    elif (email_option == 10):
        username = "swamc@cognicraftagency.site"
        password = "Shirtpant#23"
    elif (email_option == 11):
        username = "swam@cognicraftagency.today"
        password = "Shirtpant#23"
    elif (email_option == 12):
        username = "swamc@cognicraftagency.today"
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
                            Our System, which combines the power of Targeted Advertising with DCT Automated Prospecting, gets you more than a dozen new client opportunities every single month!.<br> 
                            And the best part about this is that you don't have even have to pay us anything upfront!</p>
                            <p>Yes, you read that right.</p>
                            <p>We'll generate leads, work those leads, and convert them into qualified booked calls. Not just that, we will also take care of all advertising and appointment scheduling, ensuring that we deliver on our promise of providing you with a complete ROI.</p>
                            <p>Right now, we're offering a 14-day free trial of our entire system, so that you can test it out without any risk or commitments. You can get more info about this on our website as well!</p>
                            <p>This is a limited time offer though, so check out our website and book a call with me or reach out by simply replying to this email and I'll give you a call to fill you in about this. (Don't forget to mention the best time to call you in your reply :)</p>
                            <p>Looking forward to sepaking to you!!</p>
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
