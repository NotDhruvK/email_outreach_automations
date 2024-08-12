# This script will contain all the driver scripts
from time import sleep
from random import randrange
from send_email import send_email
from csv_handler import csv_to_dataframe, dataframe_to_csv
from process_data import process_dataframe, sort_data


def driver():
    # Initialize counters and variables
    outreach_number = 0
    email_counter = 0
    last_used_account = 0
    total_emails_to_send = 180
    accounts_used = {1: 0, 2: 0, 3: 0}  # Track usage of accounts

    # Convert the data into a pandas dataframe using the csv_to_dataframe function
    df = csv_to_dataframe()

    # Clean the data using the process_dataframe function
    df_cleaned = process_dataframe(df)

    # Iterate over the cleaned dataframe
    for index, row in df_cleaned.iterrows():
        if email_counter >= total_emails_to_send:
            print("Reached the limit of 180 emails. Stopping.")
            break

        # Get Name and Email from the row
        name = row['name']
        email = row['email']

        # Cycle through accounts (1 -> 2 -> 3 -> 1)
        if last_used_account == 3:
            email_choice = 1
        else:
            email_choice = last_used_account + 1
        last_used_account = email_choice

        try:
            # Sending the emails
            print(f"Processing email for {name} at {email}")  # Debug print
            send_email(name, email, email_choice, outreach_number)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Update the dataframe
        df_cleaned.at[index, 'account'] = email_choice
        df_cleaned.at[index, 'outreach'] = 1

        # Increment the email counter and the account usage counter
        email_counter += 1
        accounts_used[email_choice] += 1

        # Check if all three accounts have been used
        if all(usage > 0 for usage in accounts_used.values()):
            print("All three accounts have sent an email.")
            time_share = randrange(160, 180)
            print(f"Waiting for {time_share} seconds.")
            sleep(time_share)
    
            # Reset account usage after waiting
            accounts_used = {1: 0, 2: 0, 3: 0}

        # Calculate estimated time required
        estimated_time = ((total_emails_to_send - email_counter) * 3) / 60
        print(f"Estimated time left for completion: {estimated_time:.2f} hours.")

    # Sort and save the updated dataframe back to the CSV file
    sorted_df = sort_data(df_cleaned)
    dataframe_to_csv(sorted_df)
    print(f"Updated DataFrame successfully saved. Total emails sent: {email_counter}")
            

if __name__ == "__main__":
    driver()