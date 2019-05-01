#!/usr/bin/env python2

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# route for home page
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    return 'Home Page is displayed'

# route for adding new restaurant
@app.route('/restaurant/new/')
def newRestaurant():
    return 'Page for adding new restaurant'

# route for editing existing restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return 'Page for editing existing restaurant'

# route for deleting existing restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return 'Page for deleting existing restaurant'

# route for viewing restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/')
@app.route('/restaurant/<int:restaurant_id>/')
def showMenu(restaurant_id):
    return 'Page for viewing restaurant menu\'s'

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return 'Page for adding new restaurant menu\'s'

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/edit')
def editMenuItem(restaurant_id):
    return 'Page for editing existing restaurant menu\'s'

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def deleteMenuItem(restaurant_id):
    return 'Page for deleting existing restaurant menu\'s'

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)