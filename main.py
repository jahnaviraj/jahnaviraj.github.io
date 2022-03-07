###FLASK APP FOR PORTFOLIO WEBSITE##
 
from flask import Flask, render_template, request, flash
import smtplib, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('secret_key')

@app.route("/", methods=["GET","POST"])
def home():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
