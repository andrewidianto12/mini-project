import json
import requests
import traceback
from flask import make_response, jsonify, current_app, request
from flask_restful import Resource, reqparse
from flask_sieve import Validator

class PokeList(Resource):
    @classmethod
    def get(cls):
        r = requests.get('https://pokeapi.co/api/v2/pokemon')
        return r.json()

   