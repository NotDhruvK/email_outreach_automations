import smtplib
import logging

def loginTester():
    SMTP_SERVER = 'smtpout.secureserver.net'
    SMTP_PORT = 465

    logging.basicConfig(filename='errors.txt', level=logging.ERROR)

    for email_option in range(1,13):
        if (email_option == 1):
            username = "swam@cognicraftagency.live"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 2):
            username = "swamc@cognicraftagency.live"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 3):
            username = "swam@cognicraftagency.solutions"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 4):
            username = "swamc@cognicraftagency.solutions"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 5):
            username = "swam@cognicraftagency.agency"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 6):
            username = "swamc@cognicraftagency.agency"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 7):
            username = "swam@cognicraftagency.tech"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 8):
            username = "swamc@cognicraftagency.tech"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 9):
            username = "swam@cognicraftagency.site"
            password = "Shirtpant#23"
            
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 10):
            username = "swamc@cognicraftagency.site"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 11):
            username = "swam@cognicraftagency.today"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 12):
            username = "swamc@cognicraftagency.today"
            password = "Shirtpant#23"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

if __name__ == "__main__":
    loginTester()