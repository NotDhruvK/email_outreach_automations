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

    return int(choice)

def file_selector(choice):
    if (choice == 1):
        return 'csv_files/firstemail.csv'
    elif (choice == 2):
        return 'csv_files/secondemail.csv'
    elif (choice == 3):
        return 'csv_files/thirdemail.csv'

def subject_selector():
    choice = 0
    return choice


def body_choice():
    choice = 0
    return choice

def driver():
    # Get which account to send from
    email_choice = email_selector()
    file_choice = file_selector()
    outreach_number = 0

    if file_choice is None:
        print("Invalid file choice. Exiting.")
        return

    # Read the CSV file
    try:
        with open(file_choice, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            print("Opened csv file")
            for row in reader:
                name = row['name']
                email = row['email']
                print(f"Processing email for {name} at {email}")  # Debug print
                send_email(name, email, email_choice, outreach_number)
    except FileNotFoundError:
        print(f"File not found: {file_choice}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
            

if __name__ == "__main__":
    driver()