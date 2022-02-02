# Open Ad Platform

An open source platform for online advertising.  The software itself will be able to be used to provide a web service that allows for embedding of ads on multiple websites.  It will be built in Python using Flask, with a MySQL database backend, via SQLAlchemy.

I will gladly welcome contributions!  For more information about contributing to this project, see the CONTRIBUTING.txt file.

# Setup

## Create a virtualenv

`virtualenv .venv`

Activate it

`source .venv/bin/activate`

## config.py

Enter your database backend config into `config.py`. By default it is set to generic pymysql values that probably won't work. Visit the SQLAlchemy docs for more info on what to do here.

## Final instructions

Run `python3 db_create.py` to create the correct db schema.

Run `python3 db_populate_defaultad.py` to throw in a sample ad.

Finally run `python3 run.py` and visit `https://localhost:5000` to see the software in action!
