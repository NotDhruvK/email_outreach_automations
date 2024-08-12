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

The way this project is set up, you have only one file which will be used for email sending. The name of the file is **contacts.csv**
Make sure that you correctly fill in the NAME and the EMAIL in this file. It is optional to fill in the ACCOUNT and OUTREACH numbers.
**You will need to update this file daily. Fill it with 180 emails daily.**
This file needs to be located in the same directory as the rest of the python files.

## Using the code

To use the code, open Terminal and type

```
cd /Desktop/email_outreach
```

Alternatively, you can use `Tab` to autocomplete the result in the terminal.

Change the directory to `email_outreach` and then run the following:

**If you want to clean and sort the data**

```
python3 process_data.py
```

**If you want to send the emails**

```
python3 driver.py
```

# Getting the chages from github

In order to update your files to the latest version, run

```
git pull origin main
```
