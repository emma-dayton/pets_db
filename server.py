from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    db = connectToMySQL('pets_db')
    pets = db.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", pets=pets)


@app.route('/add_pet', methods=['POST'])
def add_pet():
    db = connectToMySQL('pets_db')

    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)
