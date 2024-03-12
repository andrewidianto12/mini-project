from .resources.poke.poke_list import PokeList
from .resources.poke.poke_detail import PokeDetail
from .resources.poke.review import Review
def initialize_routes(api):
    api.add_resource(PokeList, '/poke')
    api.add_resource(PokeDetail, '/poke/<name>')
    api.add_resource(Review, '/poke/<name>/review')