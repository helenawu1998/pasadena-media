from app import app
from db_setup import init_db, db_session
from forms import PersonSearchForm
from flask import flash, render_template, request, redirect
# from [database] import database class


if __name__ == '__main__':
    
    app.run()
