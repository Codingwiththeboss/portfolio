import requests
import json
from flask import Flask, render_template 

app = Flask(__name__)
@app.route("/")
def index():
   return render_template("index.html")

@app.route("/projects")
def projects():
   return render_template("projects.html")

@app.route("/pokemon/<pokemon_name>")
def get_pokemon(pokemon_name):
   response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")x
   return response.json()
if __name__ == "__main__":
   app.run(debug=True)


