# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # Initialize the database
# def init_db():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS info (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# init_db()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     email = request.form['email']
    
#     # Insert into database
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO info (name, email) VALUES (?, ?)', (name, email))
#     conn.commit()
    
#     # Debugging: Check if data is successfully inserted
#     cursor.execute('SELECT * FROM info')
#     print("Database Content After Insertion:", cursor.fetchall())
#     conn.close()

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Ensure index.html is in a 'templates' folder

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    location = request.form["location"]
    # Save the data to SQLite or handle it as needed
    print(f"Received: {name}, {email}, {phone}, {location}")
    return redirect("/")  # Redirect back to the homepage after submission

if __name__ == "__main__":
    app.run(debug=True)
