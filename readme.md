# The Definitive Guide to using this.

## Starting the environment.

1. Firstly start the command prompt and navigate to the folder containing the files.
2. Then start the virtual environment by using the command

```bash
    .venv\Scripts\Activate
```

3. Once activated, the command prompt should have `(venv)` at the beginning of the line.

## Setting up the CSV

1. The CSV file needs to have the format `name,email`.
2. Make sure to include headers and have no spaces in between the entries.
3. Better still, use excel to make the csv file.

## Making changes to the scripts

1. Before running navigate to csv_handler.py
2. In the line `df = pd.read_csv("C:/Users/Dhruv/Desktop/Work/day3.csv")`, replace the path to the path of the CSV file you created.

## Running the script

1. After enabling the virtual environment, run the command `python driver.py` in the command prompt.
