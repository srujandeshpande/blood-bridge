import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import base64
import requests
import random

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://srujan:mongodb@bloodbridge1-8kivy.gcp.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'BloodBridge1')

#Home page
@app.route('/')
def home_page():
	return render_template('index.html')

#Map page
@app.route('/map')
def map_page():
	return render_template('homepage.html')

#Add new User
@app.route('/add_new_user', methods=['POST'])
def add_new_user():
    inputData = dict(request.form)
    Donor_Data = pymongo.collection.Collection(db, 'Donor_Data')
    Donor_Data.insert_one(inputData)
    return Response(status=200)

#Org landing page
@app.route('/org_lander')
def org_lander():
    return render_template('page2.html')
