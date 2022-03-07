###FLASK APP FOR PORTFOLIO WEBSITE##
 
from flask import Flask, render_template, request, flash
import smtplib, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('secret_key')

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        admin_email = os.getenv('contact_email')
        admin_password = os.getenv('contact_password')
        with smtplib.SMTP('smtp.gmail.com', 587) as conn:
            conn.ehlo()
            conn.starttls()
            conn.login(admin_email, admin_password)
            conn.sendmail(admin_email , "jahnaviraj25@gmail.com", f'Subject: {subject} \n\n{message}\n\n-{name}\n{email}')
            conn.quit()

            flash("Your message was successfully sent. Thankyou!")

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
