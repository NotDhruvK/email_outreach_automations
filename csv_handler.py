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
        # Just replace the file path of the leads.
        # Make sure that the CSV headers are name, email.
        df = pd.read_csv("C:/Users/Dhruv/Desktop/Work/day3.csv")
        print("Successfully read csv file.")
        return df
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {str(e)}")
        return None
    

if __name__ == "__main__":
    csv_to_dataframe()