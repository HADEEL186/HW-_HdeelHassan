# importing the modiles requested for the application
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os

# variable that creates a Flask web application instance
app = Flask(__name__)

#  run the application in debug mode
app.debug = True

# sets the database URI for SQLAlchemy to connect to the database 'women.db'.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///women.db'

# sets the folder where uploaded files will be stored to 'static/upload/'.
app.config['UPLOAD_FOLDER'] = 'static/upload/'

# sets the maximum allowed file size for uploads to 16 MB.
app.config['MAX_CONTENT_LENGHT'] = 16 * 1024 * 1024

# is a set of allowed file extensions for uploads.
ALLOWED_EXTENSIONS = set(['png' , 'jpg', 'jpeg', 'gif', 'jfif'])

# function that returns True if the given file has an extension that is in ALLOWED_EXTENSIONS.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# object that will allow the application to interact with a database using SQLAlchemy's
db = SQLAlchemy(app)

# table stores information about "Women" submitted by visitors of the website.
class Women(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rate = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    position = db.Column(db.String(20), unique=False, nullable=True)
    company = db.Column(db.String(20), unique=False, nullable=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    birth_date = db.Column(db.String(20), unique=False, nullable=False)
    about = db.Column(db.String(200), unique=False, nullable=False)
    filename = db.Column(db.String(100), unique=False, nullable=True)
    def __repr__(self):
        return f"Woman : {self.name}, Rate: {self.rate,}"

# table stores reviews of the women made by visitors of the website.
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    woman_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20),unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    def __repr__(self):
        return f"Name: {self.name}, Content: {self.review_text}"

# table stores contact information submitted by visitors of the website.
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=False, nullable=False)
    email = db.Column(db.String(20),unique=False, nullable=False)
    message = db.Column(db.String, unique=False, nullable=False)
    def __repr__(self):
        return f"Name: {self.name}, Email: {self.email}"

migrate = Migrate(app, db)

# displays information about all women stored in the database
@app.route("/")
def home():
    women_info = Women.query.all()
    return render_template("homepage.html", women_info=women_info)

#  displays a form for adding a new woman to the database
@app.route("/add_profile")
def add_data():
    return render_template("add_profile.html")

# displays information about the website
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

# add a new woman to the database based on information submitted from the form
@app.route("/add", methods=["POST", "GET"])
def woman_information():
    if request.method == "POST":
        rate = request.form.get("rate")
        name = request.form.get("name")
        position = request.form.get("position")
        company = request.form.get("company")
        country = request.form.get("country")
        birth_date = request.form.get("birth_date")
        about = request.form.get("about")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        file_name = file.filename
        woman_row = Women(rate=rate,name=name, position=position, company=company,country=country,
                       birth_date=birth_date,about=about,filename=file_name)
        db.session.add(woman_row)
        db.session.commit()
        return redirect("/")

# deletes a woman from the database, specified by the id provided in the URL.
@app.route("/delete/<int:id>")
def erase(id):
    data = Women.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.woman_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")

#  redirect to the location of the image file
@app.route("/display_image/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename='upload/' +filename))

# display woman from the database, specified by the id provided in the URL.
@app.route('/woman_identify/<woman_id>')
def woman_identify(woman_id):
    woman_specific = Women.query.get(woman_id)
    reviews_specific =Reviews.query.filter(Reviews.woman_id == woman_id)
    return render_template("woman_identify.html",woman_specific=woman_specific, reviews_specific=reviews_specific)

# add a review
@app.route("/add_review", methods=["POST"])
def review_management():
    if request.method == "POST":
        name = request.form.get("name")
        review_text = request.form.get("review_text")
        woman_id = request.form.get("woman_id")
        review_row = Reviews(name=name,review_text=review_text, woman_id=woman_id)
        db.session.add(review_row)
        db.session.commit()
        return redirect("/")

# update woman information
@app.route("/alter_info/<int:id>", methods=["POST", "GET"])
def alter_info(id):
    if request.method == "POST":
        data = Women.query.get(id)
        rate = request.form.get("rate")
        name = request.form.get("name")
        position = request.form.get("position")
        company = request.form.get("company")
        country = request.form.get("country")
        birth_date = request.form.get("birth_date")
        about = request.form.get("about")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        file_name = file.filename
        if request.form.get("rate"):
            data.rate = rate
        if request.form.get("name"):
            data.name=name
        if request.form.get("position"):
            data.position=position
        if request.form.get("company"):
            data.company=company
        if request.form.get("country"):
            data.country=country
        if request.form.get("birth_date"):
            data.birth_date=birth_date
        if request.form.get("about"):
            data.about=about
        if request.files.get("file_name"):
            data.filename=file_name
        db.session.commit()
        return redirect(url_for('woman_identify', woman_id=id))
    else:
        return render_template("alter_info.html")

# add a visitor message to contact with the user
@app.route("/contact", methods=["POST", "GET"])
def contact_management():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        contact_row = Contact(name=name, email=email, message=message)
        db.session.add(contact_row)
        db.session.commit()
        return render_template("contact.html")
    else:
        return render_template("contact.html")



# start the execution of the Flask application
if __name__ == "__main__":
    app.run()
