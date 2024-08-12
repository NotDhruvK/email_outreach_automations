#This file contains all the functions regarding CSV files.
import pandas as pd

def csv_to_dataframe():
    """
    Reads a CSV file into a pandas DataFrame and returns the DataFrame.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        DataFrame: The DataFrame containing the CSV data.
    """
    try:
        df = pd.read_csv("data/contacts.csv")
        print("Successfully read csv file.")
        return df
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {str(e)}")
        return None
    

def dataframe_to_csv(df):
    """
    Updates the provided DataFrame and writes it back to a hard-coded CSV file path.

    Parameters:
        df (DataFrame): The DataFrame to update.

    Returns:
        None
    """
    try:
        file_path = 'data/contacts.csv'  # Replace with your actual file path

        # Write the updated DataFrame back to the CSV file
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    csv_to_dataframe()