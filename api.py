from flask import Flask, request
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)
api = restful.Api(app)

venues = {}
specials = {}

def abort_if_foo_doesnt_exist(_id, _dict):
	if _id not in _dict:
		restful.abort(404)

venue_parser = reqparse.RequestParser()
venue_parser.add_argument('name', type=str)
venue_parser.add_argument('address', type=str)
venue_parser.add_argument('latitude', type=float)
venue_parser.add_argument('longitude', type=float)

special_parser.add_argument('venue_id', type=int)
special_parser.add_argument('item', type=str)
special_parser.add_argument('description', type=str)
special_parser.add_argument('day', type=str)
special_parser.add_argument('time_start', type=int)
special_parser.add_argument('time_end', type=int)

class Venue(restful.Resource):
	def get(self, venue_id):
		abort_if_foo_doesnt_exist(venue_id, venues)
		return {venue_id: venues[venue_id]}

	def put(self, venue_id):
		args = venue_parser.parse_args()
		venues[venue_id] = args
		return {venue_id: venues[venue_id]}

	def delete(self, venue_id):
		abort_if_foo_doesnt_exist(venue_id, venues)
		del venues[venue_id]

class Special(restful.Resource):
	def get(self, special_id):
		abort_if_foo_doesnt_exist(special_id, specials)
		return {special_id: specials[special_id]}

	def put(self, special_id):
		args = special_parser.parse_args()
		specials[special_id] = args
		return {special_id: specials[special_id]}

	def delete(self, special_id):
		abort_if_foo_doesnt_exist(special_id, specials)
		del specials[special_id]

api.add_resource(Venue, '/venue/<string:venue_id>')
api.add_resource(Special, '/special/<string:special_id>')



if __name__ == '__main__':
	app.run(debug = True)

