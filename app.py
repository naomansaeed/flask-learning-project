# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class. This is our WSGI application.
# The __name__ argument is the name of the application's module. It helps Flask find resources (like templates and static files).
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger the following function.
# In this case, when a user visits the root URL (i.e., '/'), the home() function will run.
@app.route('/')
def home():
    # This function returns the response we want to send to the client (the browser).
    # Here, we are returning a string of HTML. Flask will automatically convert this string into an HTTP response.
    return '<h1>Hello, PyMentor!</h1><p>My first Flask app is running!</p><p><a href="/status">Check server status</a></p><p><a href="/contact">Get in contact</a></p>'

# We define another route for the URL '/status'
@app.route('/status')
def status():
    # This function returns a dictionary. Flask will automatically convert dictionaries to JSON responses.
    return {'status': 'OK', 'message': 'Server is running smoothly!'}

@app.route('/contact')
def contact():
    # This function returns a dictionary. Flask will automatically convert dictionaries to JSON responses.
    return {'Name': 'Naoman', 'email': 'naoman@mymail.com'}


# This condition checks if this script is executed directly (as opposed to being imported).
# If it is, then we run the Flask development server.
if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # debug=True enables the debugger and automatic reloader. This is useful during development but should be turned off in production.
    # host='0.0.0.0' makes the server available to any device on the network (not just localhost).
    # port=5000 specifies the port to listen on. The default is 5000.
    app.run(debug=True, host='0.0.0.0', port=5000)