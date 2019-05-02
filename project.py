#!/usr/bin/env python2

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)


# route for home page
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    return render_template('restaurants.html', restaurants = restaurants)

# route for adding new restaurant
@app.route('/restaurant/new/')
def newRestaurant():
    return render_template('newRestaurant.html')

# route for editing existing restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html', restaurant = restaurant)

# route for deleting existing restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html', restaurant = restaurant, restaurants = restaurants)

# route for viewing restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/')
@app.route('/restaurant/<int:restaurant_id>/')
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant = restaurant, menu = items)

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return render_template('newMenuItem.html', restaurant_id = restaurant_id)

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/edit')
def editMenuItem(restaurant_id):
    return render_template('editMenuItem.html', item = item, restaurant_id = restaurant_id)

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/delete')
def deleteMenuItem(restaurant_id):
    return render_template('deleteMenuItem.html', item = item, restaurant_id = restaurant_id)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)