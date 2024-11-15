# This file contains the functions required to clean and sort the data.
import pandas as pd

def sort_data(df):
    """
    Sorts the DataFrame in ascending order based on the 'account' column.

    Args:
        df (pandas.DataFrame): The DataFrame to be sorted.

    Returns:
        pandas.DataFrame: The sorted DataFrame.
    """
    # Sort the DataFrame by the 'account' column in ascending order
    sorted_df = df.sort_values(by='account', ascending=True)
    print(f"Sorted the data in ascending order.")
    return sorted_df

def process_dataframe(df):
    """
    Cleans the data by dropping all the empty "name" and "email" rows. Populates the "account" and "outreach" columns with the required integers.
    Finally, drops all the duplicated email entries.

    Args:
        df (pandas.DafaFrame): The DataFrame to be cleaned.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    initial_count = len(df)

    # Discard rows where either 'name' or 'email' is empty
    df_cleaned = df.dropna(subset=['name', 'email'], how='any')
    discarded_count = initial_count - len(df_cleaned)

    # # Fill empty 'account' and 'outreach' columns with 0 and convert them to integers
    # df_cleaned['account'] = df_cleaned['account'].fillna(0).astype(int)

    # Remove duplicate emails, keeping the first occurrence
    df_cleaned = df_cleaned.drop_duplicates(subset='email', keep='first')

    final_count = len(df_cleaned)

    print(f"Total entries after processing: {final_count}")
    print(f"Total discarded entries: {discarded_count}")

    return df_cleaned

def csv_to_dataframe(file_path):
    """
    Reads a CSV file and converts it into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The DataFrame created from the CSV file.
    """
    return pd.read_csv(file_path)

def dataframe_to_csv(df, file_path):
    """
    Writes the pandas DataFrame to a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to be written to CSV.
        file_path (str): The file path to write the CSV to.
    """
    df.to_csv(file_path, index=False)
    print(f"Data has been written to {file_path}.")

if __name__ == "__main__":
    import sys

    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <file_path>")
    #     sys.exit(1)

    # file_path = sys.argv[1]

    # Read the CSV file
    dataframe = csv_to_dataframe("C:/Users/Dhruv/Desktop/Work/day1.csv")

    # Process the DataFrame
    df_cleaned = process_dataframe(dataframe)

    # Write the sorted DataFrame back to the CSV file
    # dataframe_to_csv(df_cleaned,"C:/Users/Dhruv/Desktop/Work/day1.csv")