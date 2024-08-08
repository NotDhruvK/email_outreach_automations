# This script will contain all the driver scripts
import csv
from time import sleep
from random import randrange
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
        return 'data/firstemail.csv'
    elif (choice == 2):
        return 'data/secondemail.csv'
    elif (choice == 3):
        return 'data/thirdemail.csv'

def subject_selector():
    choice = 0
    return choice


def body_choice():
    choice = 0
    return choice

def driver():
    # Get which account to send from
    email_choice = email_selector()
    file_choice = file_selector(email_choice)
    outreach_number = 0
    counter = 0

    if file_choice is None:
        print("Invalid file choice. Exiting.")
        return

    # Read the CSV file
    try:
        with open(file_choice, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            print("Opened csv file")
            for row in reader:
                counter += 1
                name = row['name']
                email = row['email']

                # Calculating estimated time.
                time_share = randrange(160,180)
                print(f"Waiting for {time_share} seconds.")
                estimated_time = ((60 - counter) * 3)
                print(f"Estimated time left for completion : {estimated_time} minutes.")

                # Wait so that only 20 emails are delivered in an hour                
                sleep(time_share)

                # Sending the emails
                print(f"Processing email for {name} at {email}")  # Debug print
                send_email(name, email, email_choice, outreach_number)

    except FileNotFoundError:
        print(f"File not found: {file_choice}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
            

if __name__ == "__main__":
    driver()