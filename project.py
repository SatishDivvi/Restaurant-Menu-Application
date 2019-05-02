#!/usr/bin/env python2

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

# route for home page
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants = restaurants)

# route for adding new restaurant
@app.route('/restaurant/new/')
def newRestaurant():
    return render_template('newRestaurant.html')

# route for editing existing restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html')

# route for deleting existing restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html')

# route for viewing restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/')
@app.route('/restaurant/<int:restaurant_id>/')
def showMenu(restaurant_id):
    return render_template('menu.html')

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return render_template('newMenuItem.html')

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/edit')
def editMenuItem(restaurant_id):
    return render_template('editMenuItem.html')

# route for adding new restaurant menu's
@app.route('/restaurant/<int:restaurant_id>/menu/delete')
def deleteMenuItem(restaurant_id):
    return render_template('deleteMenuItem.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)