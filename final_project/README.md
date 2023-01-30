# Powerful women in tech Application
# Every day is a learning day
 ** Hadeel Hassan ** 
---------------------------------------------------------------------------------------
This Flask application allows users to view a list of most powerful women in high-tech, and their details. <br>Users can also add,update or delete in the list.


## Installation

1. Install the required packages: Flask , flask-sqlalchemy ,Flask-Migrate in my python project
2. Import the modules we need: Flask, render_template, request, redirect, url_for,Migrate, migrate,SQLAlchemy,os and webbrowser
3. Create the database and import the sample data 
4. Update the database configuration in the `config.py` file
5. Run the application: `python app.py`

## Usage

- Run the application by executing `python app.py`
- Open a web browser and navigate to `http://localhost:5000`
- View the photo list of the women 
- There is an option to add new member to the list by "add_profile" page
- Click in one photo to open a page with the details of this women by "womam_identify" page.
- There is an option to add a review by the user in "womam_identify" page.
- There is an option to delete or change details in the "womam_identify" page by two buttons.
- The update button take the user to alter_info page where can he change or update new infomartion.


## Built With

- [Python](https://www.python.org/) - The programming language used
- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [HTML] - Markup Language
- [Django] - Python web framework 
-  CSS framework used for styling

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a pull request

## Description

- Create Flask application
- Create database to your site subject
- The options of the site will be to charge an information about new member,like:
  1. woman image
  2. Name
  3. Position
  4. Company
  5. Country
  6. Date of birth
  7. About her success
- On the homepage of the site will present all the images as a link for each one detail page.
- The detail page will contain all the data that belong for the same woman with option to write a review

## Design 

This is a Flask web application that has functionality to store information about women, such as name, position, company, country, birth date, about, and a profile picture.<br>
This information is stored in a SQLite database using the SQLAlchemy library. The user can add, delete, or view information about a woman.
The uploaded images are stored in a folder,<br>
and the path to the image is stored in the database. The file format of the images must be in 'png', 'jpg', 'jpeg', 'gif', or 'jfif'.

## Table of Contents
Depending on the  project directory and the contents of the files, I will divide the contents:
1. README.md 
2. app.py - it contain code that sets uo the application
3. templates - it contain all the HTML files 
4. static - it contain the upload images and the CSS file
5. instance - file that contains configuration settings or data specific to an individual instance of a software application
6. migrations - is a versioned change to the database schema, used for version control and to keep track of changes made to the database over time.

## Tests

The following tests we may run in the application to ensure it's functioning correctly:
1. Unit tests: to test individual functions and modules
2. Integration tests: to test the interaction between different parts of the application.
3. Functional tests: to test end-to-end functionality of the application, simulating a user's actions.
4. Load tests: to test the performance and scalability of the application under heavy loads.
5. Security tests: to test for vulnerabilities and ensure data protection.
6. Usability tests: to test the user interface and the user experience of the application.

## Bugs

1. If we try to update the image for one of the women in update page , in the home page we will get an icon instead of image.
2. popup message may appear just once in the first time we get in the application.

## MY project sources:
Next to all the tools that Alex taught me, in this project I was helped further with
these sites,<br> I collect my application information about powerful women:
- https://chat.openai.com/
- https://google.com
- https://en.wikipedia.org/wiki/Main_Page
- https://www.thinkdigitalpartners.com/
- https://www.womentech.net/
- https://www.techopedia.com/
- https://www.techtarget.com/whatis/
- https://www.forbes.com/lists/power-women/?sh=7b0a2d175a95

## Author

- **Hadeel Hassan** - https://github.com/HADEEL186/HW_HdeelHassan


