import os
from os.path import join, dirname
from app import init_app
from dotenv import load_dotenv
from flask import render_template, request, jsonify
import requests

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

config = "config.Config"

# init_app('name', config)
# name in here can be changes to project name.
app = init_app("app", config)

# Define route to render index.html


def search_pokemon(query, category):
    if category == 'pokemon':
        url = f"https://pokeapi.co/api/v2/pokemon/{query.lower()}"
    elif category == 'type':
        url = f"https://pokeapi.co/api/v2/type/{query.lower()}"
    else:
        return None

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list_types', methods=['GET'])
def list_types():
    url = "https://pokeapi.co/api/v2/type"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types = [t['name'] for t in data['results']]
        return render_template('types.html', types=types)
    else:
        return render_template('error.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['pokemon_name']
        category = request.form['category']
        result = search_pokemon(query, category)
        if result:
            if category == 'pokemon':
                return render_template('result.html', pokemon=result)
            elif category == 'type':
                return render_template('type_result.html', type_info=result)
        else:
            return render_template('error.html')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=app.config.get("APP_DEBUG"),
        port=app.config.get("APP_PORT"),
    )
