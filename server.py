from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add_pet', methods=['POST'])
def add_pet():
    # submit info and SQL query go here
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)
