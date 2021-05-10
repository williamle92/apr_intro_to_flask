from app import app

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/name')
def name():
    name = 'Brian'
    return f'Hello, {name}'