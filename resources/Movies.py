from flask import jsonify, request
from flask_restful import Resource
from .profit import getMaximumProfit

class Movies(Resource):

    def post(self): 
        body = request.get_json(force=True)

        if len(body)==0:
            return {"error":"List is empty"}    
        movies = body['movies']
        res = getMaximumProfit(movies)

        return res
        
       


