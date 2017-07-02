from flask import Flask



app = Flask(__name__)
from src.views import app
app.secret_key = 'some_random_key'# secret key is needed to keep the client-side sessions secure
# object called session which allows you to store information specific to a user from one request to the next. 
