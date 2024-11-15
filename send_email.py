# This script includes the information and the functions to send emails.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(filename='errors.txt', level=logging.ERROR)

SMTP_SERVER = 'smtpout.secureserver.net'
SMTP_PORT = 465

def send_email(to_name, to_email, email_option):
    # Replace these email settings with your own
    if (email_option == 1):
        username = "drew@automateyourworkplace.site"
        password = "Shirtpant123#"
    elif (email_option == 2):
        username = "drewa@automateyourworkplace.site"
        password = "Shirtpant123#"
    elif (email_option == 3):
        username = "drew@automateyourworkplace.store"
        password = "Shirtpant123#"
    elif (email_option == 4):
        username = "drewa@automateyourworkplace.store"
        password = "Shirtpant123#"
    elif (email_option == 5):
        username = "drew@automateyourworkplace.shop"
        password = "Shirtpant123#"
    elif (email_option == 6):
        username = "drewa@automateyourworkplace.shop"
        password = "Shirtpant123#"
    elif (email_option == 7):
        username = "drew@automateyourworkplace.online"
        password = "Shirtpant123#"
    elif (email_option == 8):
        username = "drewa@automateyourworkplace.online"
        password = "Shirtpant123#"
    elif (email_option == 9):
        username = "drew@automateyourworkplace.fun"
        password = "Shirtpant123#"
    elif (email_option == 10):
        username = "drewa@automateyourworkplace.fun"
        password = "Shirtpant123#"
    
    try:
        # Set up the server
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(username, password)
            print(f"Logged in as {username}")

            # Setting up the body
            body = f"""\
                    <html>
                        <body>
                           <p>Hey {to_name},</p> 
                           <p>I’ve been trying to get in touch for a while now! I know this message is a little out of the blue, but I thought I’d reach out anyway.</p> 
                           <p>I’m Drew, and I’ve been helping businesses like yours work faster and more easily with smart automation systems for over a year. Our system can simplify your workflows, cut down on manual tasks, and help things run smoother and with fewer mistakes. And the best part? We’re offering a <strong>40% discount</strong> for a limited time!</p> 
                           <p>Yes, you read that right.</p> 
                           <p>Here’s how it helps, {to_name}: we’ll automate your scheduling, client management, follow-ups, and more. That way, you can focus on growing your business while we handle the heavy lifting in the background. Just sit back and enjoy the extra efficiency!</p> 
                           <p>Right now, we’re offering a <strong>limited-time 40% discount</strong> on our full automation package. If you’d like to learn more or give it a try, reply to this email or check out our website to book a call with me. Don’t forget to let me know the best time to reach you!</p> 
                           <p>Looking forward to speaking with you soon!</p> 
                           <p>Best,<br>Drew</p>
                        </body>
                    </html>
                    """
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = to_email
            msg['Subject'] = f"Hey {to_name}, tired of wasting time on manual tasks?"
            msg.attach(MIMEText(body, 'html'))

            # Send the email
            server.sendmail(username, to_email, msg.as_string())
            print(f"Email sent to {to_name} at {to_email}")

    except Exception as e:
        # Log any errors
        logging.error(f"Failed to send email to {to_name} ({to_email}): {str(e)}")

if __name__ == "__main__":
    # This is only for testing purposes
    send_email("Dhruv", "dhruvadam@gmail.com", 1)