#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import dateutil.parser
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

# TODO: connect to a local postgresql database
db = SQLAlchemy()
def db_setup(app):
  app.config.from_object('config')
  db.app = app
  db.init_app(app)
  migrate = Migrate(app, db)
  return db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# Venue model
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)), nullable=False)
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show', backref='venue')

    def __repr__(self):
      return f'<Venue {self.id} {self.name}>'


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# Artist model
class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String(120)), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show', backref='artist')

    def __repr__(self):
      return f'<Artist {self.id} {self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

# Show model
class Show(db.Model):
  __tablename__ = 'Show'
  """docstring for ClassName"""

  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
  start_time = db.Column(db.DateTime, default=datetime.now, nullable=False)


  def __repr__(self):
    return f'<Show {self.id}, Artist {self.artist_id}, Venue {self.venue_id}>'