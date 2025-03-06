# Birthday Tracker Web Application

## Overview
This is a simple web application built with Flask that allows users to:
- Add birthdays (name, month, and day) to a database
- View a list of stored birthdays
- Uses SQLite as the database backend through CS50's SQL module

## Features
- Add new birthday entries via a form
- Display all stored birthdays
- Basic caching prevention
- Auto-reloading templates during development

## Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- CS50 Python library (`pip install cs50`)

## Usage
1. Run server and access the application at `http://127.0.0.1:5000/`
2. Submit a new birthday:
   - Enter a name
   - Select a month (1-12)
   - Select a day (1-31)
3. View all stored birthdays on the main page

## Routes
- `/` (GET): Displays all birthdays
- `/` (POST): Adds a new birthday to the database

## Technical Details
- **Framework**: Flask
- **Database**: SQLite via CS50 SQL
- **Template Engine**: Jinja2 (via Flask)
- **Cache Prevention**: Implemented via response headers

## Configuration
- Templates auto-reload is enabled for development
- Responses are configured to prevent caching
- Database connection uses SQLite file `birthdays.db`
