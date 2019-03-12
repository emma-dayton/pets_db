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


@app.route('/safe_add_pet', methods=['POST'])
def safe_add_pet():
    db = connectToMySQL('pets_db')
    data = {
    'name': request.form['name'],
    'species': request.form['species']
    }
    print(data)
    safe_query = 'INSERT INTO pets (name, species, created_at, updated_at) VALUES(%(name)s, %(species)s, now(), now())'
    db.query_db(safe_query, data)
    return redirect('/')

@app.route('/dangerous_add_pet', methods=['POST'])
def dangerous_add_pet():
    db = connectToMySQL('pets_db')
    db.query_db(
    f'''INSERT INTO pets (name, species, created_at, updated_at)
    VALUES({request.form['name']}, {request.form['species']}, now(), now())'''
    )
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
