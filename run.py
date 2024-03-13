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

# POKEMON_API_URL = "https://pokeapi.co/api/v2/"


def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def get_pokemon_type(type_name):
    url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def get_pokemon_types():
    url = "https://pokeapi.co/api/v2/type"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types = [type_data['name'] for type_data in data['results']]
        return types
    else:
        return []


def search_pokemon(query, category):
    if category == 'pokemon':
        return get_pokemon_info(query)
    elif category == 'type':
        return get_pokemon_type(query)
    else:
        return None


@app.route('/')
def index():
    types = get_pokemon_types()
    return render_template('index.html', pokemon_types=types)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        if 'pokemon_name' in request.form:  # Handling search by Pokemon name
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
        elif 'type' in request.form:  # Handling search by Pokemon type
            type_name = request.form['type']
            result = get_pokemon_type(type_name)
            if result:
                return render_template('type_result.html', type_info=result)
            else:
                return render_template('error.html')
    return render_template('index.html', pokemon_types=get_pokemon_types())


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=app.config.get("APP_DEBUG"),
        port=app.config.get("APP_PORT"),
    )
