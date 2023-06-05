from flask import Flask

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1>' \
            '<p>This is a paragraph</p>'  \
            '<div style="width:100%;height:0;padding-bottom:74%;position:relative;"><iframe src="https://giphy.com/embed/r7KBK5ewpCAxi" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/r7KBK5ewpCAxi">via GIPHY</a></p>'




# Different routes using the app.route decorator.
@app.route('/bye')
def bye():
    return "Bye!"


# Creating variable paths & converting the path to a specified data type.
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload.
    app.run(debug=True)

greet()