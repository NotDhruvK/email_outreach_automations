import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_email():
    SMTP_SERVER = 'smtpout.secureserver.net'
    SMTP_PORT = 465
    USERNAME = 'drewa@automateyourworkplace.site'
    PASSWORD = 'Shirtpant123#'

    msg = MIMEMultipart()
    msg['Subject'] = 'Test Email'
    msg['From'] = USERNAME
    msg['To'] = 'dhruvadam@gmail.com'  # Replace with a valid recipient

    try:
        print("Creating SMTP_SSL connection...")
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=10) as server:
            print("Connection established.")
            print("Logging in...")
            server.login(USERNAME, PASSWORD)
            print("Login successful.")
            print("Sending email...")
            body = f"""
                    <html>
                        <body>
                           <p>Hey Dhruv,</p> 
                           <p>I’ve been trying to get in touch with you for a while now, lol. I know this may seem a bit out of the blue, but I thought I’d reach out anyway.</p> 
                           <p>My name is Drew, and I’ve been helping businesses like yours streamline their operations and run more efficiently through powerful automation systems for over a year now.<br> Our Automation System is designed to simplify your workflows, reduce manual tasks, and help your business operate smoother, faster, and with fewer errors.<br> And here’s the best part: We’re currently offering a <strong>40% discount</strong> for a limited time!</p> 
                           <p>Yes, you read that right.</p> 
                           <p>We’ll automate your scheduling, client management, follow-ups, and more, allowing you to focus on growing your business while we handle the heavy lifting in the background. All you need to do is sit back and enjoy the increased efficiency!</p> 
                           <p>Right now, we’re offering a <strong>limited-time 40% discount</strong> on our full automation package. If you’re interested in learning more or trying it out, simply reply to this email or visit our website to book a call with me. Don’t forget to let me know the best time to reach you!</p> 
                           <p>Looking forward to speaking with you soon!</p> 
                           <p>Best,<br>Drew</p>
                        </body>
                    </html>
                    """
            msg.attach(MIMEText(body, 'html'))

            server.sendmail(USERNAME, 'dhruvadam@gmail.com', msg.as_string())
            print("Test email sent successfully.")
    except Exception as e:
        print(f"Failed to send test email. Error: {str(e)}")

if __name__ == "__main__":
    test_email()
