import smtplib
import logging

def loginTester():
    SMTP_SERVER = 'smtpout.secureserver.net'
    SMTP_PORT = 465

    logging.basicConfig(filename='errors.txt', level=logging.ERROR)

    for email_option in range(1,11):
        if (email_option == 1):
            username = "drew@automateyourworkplace.site"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 2):
            username = "drewa@automateyourworkplace.site"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 3):
            username = "drew@automateyourworkplace.store"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 4):
            username = "drewa@automateyourworkplace.store"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 5):
            username = "drew@automateyourworkplace.shop"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 6):
            username = "drewa@automateyourworkplace.shop"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 7):
            username = "drew@automateyourworkplace.online"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 8):
            username = "drewa@automateyourworkplace.online"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 9):
            username = "drew@automateyourworkplace.fun"
            password = "Shirtpant123#"
            
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue

        elif (email_option == 10):
            username = "drewa@automateyourworkplace.fun"
            password = "Shirtpant123#"

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(username, password)
                print(f"Logged in as {username}")
                continue


if __name__ == "__main__":
    loginTester()