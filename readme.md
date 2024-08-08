# Getting set up

Firstly you will need to install python and git on your machine.

```
brew install python
brew install git
```

# Packages to be installed

Thease are the dependencies that need to be installed on your machine in order to successfully run the program

```
pip install {package_name}
```

The list of packages are 1. smptlib

Just replace the name of the package as given in the list into the command.

# Using the Scripts

## Locating the files.

In order to use the script, firstly you need to get to the location of the file in your computer.
After opening terminal,

```
pwd
```

This will show you the current working directory.

```
cd ..
```

This command will allow you to go up in your folder structure.
**OR**
You can directly enter the path of your working directory in the terminal interface.

```
cd {path_of_the_file}
```

## Updating the files

The way this project is set up, you will have three files which will be responsible for the email sending. These are

1. firstemail.csv
2. secondemail.csv
3. thirdemail.csv

**You will need to update these files daily. Fill them with 60 emails daily.**
These files need to be located in the same directory as the rest of the python files.

## Using the code

To use the code, open Terminal and type

```
python3 driver.py
```

# Getting the chages from github

In order to update your files to the latest version, run

```
git pull origin main
```
