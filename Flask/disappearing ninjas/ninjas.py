from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def single_ninja(color):
    if color == "blue":
        color_str = "leonardo.jpg"
    elif color == "purple":
        color_str = "donatello.jpg"
    elif color == "red":
        color_str = "raphael.jpg"
    elif color == "orange":
        color_str = "michelangelo.jpg"
    else:
        color_str = "notapril.jpg"
    return render_template('single.html', color_string = color_str)

app.run(debug=True)
