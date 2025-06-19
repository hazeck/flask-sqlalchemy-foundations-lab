#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Naming convention to prevent migration issues
metadata = MetaData()

# Initialize the SQLAlchemy object
db = SQLAlchemy(metadata=metadata)

# Define the Earthquake model
class Earthquake(db.Model):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

