# This script will contain all the driver scripts
import csv
from send_email import send_email

def email_selector():
    # Set which account to send from
    print("Which email do you want to send from?")
    print("1. swam@cognicraft.agency")
    print("2. swam@cognicraftagency.social")
    print("3. swam@cognicraftagency.website")

    choice = input("Please enter the number corresponding to the email: ")

    return choice

def file_selector(choice):
    if (choice == 1):
        return 'firstemail.csv'
    elif (choice == 2):
        return 'secondemail.csv'
    elif (choice == 3):
        return 'thirdemail.csv'

def subject_selector():
    choice = 0
    return choice


def body_choice():
    choice = 0
    return choice

def driver():
    # Get which account to send from
    email_choice = email_selector()
    subject_choice = 0
    body_choice = 0
    file_choice = file_selector(email_choice)

    # Read the CSV file
    with open(file_choice, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            email = row['email']
            send_email(name, email, email_choice, subject_choice, body_choice)
            

if __name__ == "__main__":
    driver()