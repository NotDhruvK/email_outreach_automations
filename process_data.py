# This file contains the functions required to clean and sort the data.
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
        pandas.DataFrame: The cleaned DataFrame
    """
    initial_count = len(df)

    # Discard rows where either 'name' or 'email' is empty
    df_cleaned = df.dropna(subset=['name', 'email'], how='any')
    discarded_count = initial_count - len(df_cleaned)

    # Fill empty 'account' and 'outreach' columns with 0 and convert them to integers
    df_cleaned['account'] = df_cleaned['account'].fillna(0).astype(int)
    df_cleaned['outreach'] = df_cleaned['outreach'].fillna(0).astype(int)

    # Remove duplicate emails, keeping the first occurrence
    df_cleaned = df_cleaned.drop_duplicates(subset='email', keep='first')

    final_count = len(df_cleaned)

    print(f"Total entries after processing: {final_count}")
    print(f"Total discarded entries: {discarded_count}")

    return df_cleaned

if __name__ == "__main__":
    from csv_handler import csv_to_dataframe, dataframe_to_csv

    dataframe = csv_to_dataframe()
    df = process_dataframe(dataframe)
    sorteddf = sort_data(df)
    dataframe_to_csv(sorteddf)