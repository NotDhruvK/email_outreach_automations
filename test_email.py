import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_email():
    SMTP_SERVER = 'smtpout.secureserver.net'
    SMTP_PORT = 465
    USERNAME = 'swam@cognicraftagency.website'
    PASSWORD = 'Shirtpant#23'

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
            msg.attach(MIMEText(body, 'html'))

            server.sendmail(USERNAME, 'dhruvadam@gmail.com', msg.as_string())
            print("Test email sent successfully.")
    except Exception as e:
        print(f"Failed to send test email. Error: {str(e)}")

if __name__ == "__main__":
    test_email()
