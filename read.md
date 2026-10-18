
# HTML & JSON Server

This project is a Flask server that demonstrates HTTP, routing, HTML responses, JSON APIs, and client-server communication.


## Features

- HTML pages: /, /about, /projects, /contact
- JSON endpoints: /api/about, /api/projects
- GET and POST methods: /api/contact
- HTTP status codes: 200, 400, and 404


## How to run 

1. Install Python.
2. Install the dependencies:
   pip install -r requirements.txt

3. Start the application:
   python myserver.py

4. Visit http://127.0.0.1:5000 in your browser.


## Test the API

GET /api/about
GET /api/projects
GET /api/contact
POST /api/contact     

(The POST endpoint returns the submitted JSON data and a confirmation message.)


## What this project shows:

- Flask routes and endpoints
- HTTP GET and POST requests
- HTML and JSON responses
- HTTP status codes
- Client-server architecture
