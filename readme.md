# Contacts Database

A simple python interface that connects to google firebase to. This script can view, create, edit, and delete contact info from said database, alllowing for the data to be accessed anywhere, any time through the cloud.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install the firebase_admin python library (pip install firebase_admin)
2. Place your firebase api key file in the main folder under the name "apikey.json."
3. Run contacts.py and follow the in-program instructions.

Instructions for using the software:

1. Most instructions are explained in the program. navigate menus with the numbers displayed.
2. When the program asks for a specific text entry (e.g. first name and last name to find a specific record) case and spacing do not matter.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.13.7
* firebase_admin 7.1.0
* VSCode 1.108.2

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Free Code Camp](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)
* [Official firebase documentation](https://firebase.google.com/docs/reference/admin/python)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Make the UI slightly more intuitive.
* [ ] Allow users to filter results when searching for specific contacts.
* [ ] Make it easier to select a specific contact to delete.
