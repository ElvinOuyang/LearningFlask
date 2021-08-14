"""
Practice Flask API script.

Following https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24.
"""

from flask import Flask, jsonify
from subdomain import subdomain_bp  # import blueprint from subdomain script

app = Flask(__name__)
app.register_blueprint(subdomain_bp, url_prefix='/subdomain')  # registers bp from app

app.logger.info('This is an INFO message')  # use app.logger to log messages

@app.before_request
def before():
    """
    Use before_request decorator to execute before requests.
    
    Use this decorator to log user requests from terminal.
    """
    print("This is executed BEFORE each request")

@app.route('/home/')
def home():
    """Use @app.route to define URL path."""
    return "Home page"

@app.route('/increase-<int:number>/')
def incrementer(number):
    """Use <dtype:variable-name> to define variable in URL path."""
    return "Incremented number is " + str(number + 1)

@app.route('/greet-<string:name>/')
def hello(name):
    """Use int, string, and other python native types."""
    return "Hello " + name

@app.route('/person/')
def get_person():
    """Use flask.jsonify function to wrap dictionary as serializables."""
    return jsonify({'name': 'Elvin',
                    'address': 'USA'})

@app.route('/numbers/')
def get_number():
    """Use jsonify to also process lists and tuples."""
    return jsonify(list(range(5)))

@app.route('/contact')
def contact():
    """
    Notice the path does not have trailing slash.
    
    When trying to visit /contact/, a 404 Not Found will be returned.
    """
    return 'Contact page'

@app.route('/teapot/')
def teapot():
    """Use the second item in returned tuple as status code when needed."""
    return "Would you like some tea?", 418


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, use_reloader=True, threaded=True)
    # use_reloader will reload the server when codes are changed
    # threaded will treat each request in a different thread