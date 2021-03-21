Assignment 4: Barky Service Transformation
 
https://github.com/winzadot/barkyservice

Created this project in a Virtual environment
Steps to create https://iecpdsa.blogspot.com/2021/03/flask-service-environment-setup.html


Flask
appservice.py is the file where we can access the api calls with routes

In powershell,
set environment variables to set the default page 
$env:FLASK_APP = "appservice.py"
Run app
python -m flask run
Open the page and see the results
http://127.0.0.1:5000/jsonresult to return json results


Flask-SQLAlchemy
flasksql.py is the flash file which uses the models.py( ORM) to access db

Html files:
Under the templates folder
Login files and register files under auth folder
Css file under static folder
Layout page is base.html

These files are called using auth.py
a


