# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/YoDatabase"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
