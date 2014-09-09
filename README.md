There is no method of creating accounts in bulk for Scratch 2. However, schools may need to register hundreds of accounts to teach the new curriculum in England. This script was written to automate the process for LGFL schools, though it should work for any arbitrary set as long as the input file is formatted correctly.

##Requirements
- Python 3 interpreter obtained from here: https://www.python.org/download
- Python Selenium bindings. After installing Python, type “pip install selenium” at the command line.
- Selenium ChromeDriver obtained from here:
- Copy the chromedriver.exe file into the directory with the downloaded scratch-automated.py file.
- CSV file of students with username, password, email address and date of birth in DD/MM/YYYY format, with the header row removed.
- In London, LGFL schools can download the data from their Atomwide support site and format before using. The file needs to be saved as a CSV file.
The filename must be export.csv

##Running the script
- Copy students.csv to the scratch-automated-registration directory
- Extract the chromedriver.exe from the zip file and copy it into the scratch-automated-registration directory
- Run the script by typing python scratch-website-selenium.py into the command line

## Issues
Occasionally the browser may crash. The script should automatically close and restart the browser, and resume from where it left off. 

If it is interrupted for another reason, it will fail when resuming as the account will already have been created.  Look in the students.log text file to find the most recently created account, and delete that row and all above rows from the students.csv file and restart. 
If the username or email address is already in use (very unlikely for LGFL USO usernames) it will also fail, so try to pick unique usernames, for example by adding your school’s name to the start.

##LGFL specific instructions

Export, create students.csv, delete all columns that aren’t “full USO username”, password, email, DOB. Delete the header.

Scratch does not allow full stops in usernames, but LGFL USO usernames include them. Full stops are replaced with hyphens (-). For example a username:
>abcde001.999

will become:

>abcde001-999

For new joiners,  open Atomwide in user view, select the students, add the “Latest move or create” column and export to Excel. You can then easily delete all students who joined before the previous run before exporting to csv.

##Technical Notes
The instructions provided are for Windows, however it should work on Mac OSX or Linux

Similarly it is intended to run using Python 3.4 as this release includes pip, but should run on Python 2.

Chrome was selected as Firefox was found to be less stable during testing. You can change which browser is used by changing the:

>driver = webdriver.Chrome()

line to another listed [here](http://selenium-python.readthedocs.org/en/latest/api.html), downloading the relevant WebDriver and placing it in the scratch-automated-registration directory. Firefox's WebDriver is included by default and can be used by simply changing the line to:

>driver = webdriver.Firefox()

##Future changes
Performance could be improved dramatically by parallelising to use multiple browser windows at once. I'd be happy to do this in future if there is demand for it.

Similarly it could detect when a user has already been created and continue or fail in a nicer way. 