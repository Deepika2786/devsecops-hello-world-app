# app.py
# This line imports the Flask class from the flask library.
# Flask is a micro web framework for Python.
from flask import Flask

# This line creates an instance of the Flask class.
# '__name__' tells Flask where to look for resources.
app = Flask(__name__)

# This is a 'decorator' that tells Flask which URL (or route) should trigger the function below it.
# In this case, '/' means the root URL (e.g., http://your-ip:5000/).
@app.route('/')
# This is the function that gets called when someone visits the '/' route.
# It simply returns the string 'Hello, World from DevSecOps Pipeline!'.
def hello_world():
    return 'Hello, World from DevSecOps Pipeline!'

# This block ensures that the Flask application runs only when the script is executed directly (not imported as a module).
# 'host='0.0.0.0'' makes the server accessible from any IP address (not just localhost).
# 'port=5000' makes the application listen on port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)