import flask as Flask

app = Flask(name)

@app.route('/')
def hello():
    return 'Hello, World'

@app.route('/bye')  # Corrected route to '/bye'
def bye():
    return 'Goodbye, World'  # Changed message for the '/bye' endpoint

if name == "main":
    app.run(host='0.0.0.0', port=1234, debug=True)