# Import the Flask class from the flask module along with render_template class
from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
import json

# Create an instance of the Flask class. This is our WSGI application.
# The __name__ argument is the name of the application's module. It helps Flask find resources (like templates and static files).
app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Needed for future flash messages (error/success notifications)

#with open('data/books.json', 'r') as f:
# books = json.load(f)

#[
#    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'status': 'Completed'},
#    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'status': 'To Read'},
#    {'id': 3, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'status': 'In Progress'},
#    {'id': 4, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'status': 'To Read'},
#    {'id': 5, 'title': 'Clean Code', 'author': 'Robert C. Martin', 'status': 'completed'},
#    {'id': 6, 'title': 'Python Crash Course', 'author': 'Eric Matthes', 'status': 'to-read'}
#]

# The route() decorator tells Flask what URL should trigger the following function.
# In this case, when a user visits the root URL (i.e., '/'), the home() function will run.
@app.route('/')
def home():
    # This function returns the response we want to send to the client (the browser).
    # Here, we are returning a string of HTML. Flask will automatically convert this string into an HTTP response.

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # ✅ Load fresh data from file each time
    with open('data/books.json', 'r') as f:
        books = json.load(f)
    

    return render_template('home.html', current_time=current_time, books=books)

    # render_template() is a Flask function that looks in the 'templates' folder
    # It processes the HTML template and returns the final HTML to the browser
   # return render_template('home.html')# '<h1>Hello, PyMentor!</h1><p>My first Flask app is running!</p><p><a href="/status">Check server status</a></p><p><a href="/contact">Get in contact</a></p>'

# We define another route for the URL '/status'
@app.route('/status')
def status():
    # This function returns a dictionary. Flask will automatically convert dictionaries to JSON responses.
    # return {'status': 'OK', 'message': 'Server is running smoothly!'}
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('status.html', status='OK', message='server is running smoothly', current_time=current_time)

@app.route('/contact')
def contact():
    # CONTACT PAGE ROUTE:
    # This function renders the 'contact.html' template and passes contact details (name and email) as context variables.
    # Flask automatically substitutes these variables in the Jinja template before sending the final HTML to the browser.
    # render_template() looks in the 'templates' folder and injects the provided data into the Jinja placeholders.

    return render_template('contact.html', name='naoman', email='naoman@mymail.com' )  #{'Name': 'Naoman', 'email': 'naoman@mymail.com'}

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']

        # Read existing books
        with open('data/books.json','r') as f:
            books =json.load(f)
       #     books.append({books.title})
        

        if books:
            max_id = max(book['id'] for book in books)
        else:
            max_id = 0
        

        # Create a new book entry
        new_book = {
            "id": max_id + 1,  # simple ID system
            "title": title,
            "author": author,
            "status": status
        }
        
        # Append to the list
        books.append(new_book)
        
        # Save back to JSON
        with open('data/books.json','w') as f:
            json.dump(books, f, indent=4)

        flash('Book added successfully!')
        return redirect(url_for('home'))  # ✅ now Flask knows what to do
    else:
        # Render the empty form page
        return render_template('add_book.html')
# --------------------------------------------------
# Route: /delete/<id>
# Purpose: Remove a book record by its ID
# Method: GET (simple link trigger)
# --------------------------------------------------
@app.route('/delete/<int:id>')
def delete_book(id):
    pass
    # Load books
    # Find the one with matching ID
    # Remove it
    # Save back to JSON
    # Flash message
    # Redirect home

# This condition checks if this script is executed directly (as opposed to being imported).
# If it is, then we run the Flask development server.
if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # debug=True enables the debugger and automatic reloader. This is useful during development but should be turned off in production.
    # host='0.0.0.0' makes the server available to any device on the network (not just localhost).
    # port=5000 specifies the port to listen on. The default is 5000.
    app.run(debug=True, host='0.0.0.0', port=5000)