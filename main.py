from flask import Flask, request
import requests as rq
import json
import os


app = Flask(__name__)
PODCAST_API = os.getenv("PODCAST_API")


@app.route('/lookup', methods=["GET"])
def lookup():
    """ /lookup This endpoint to search the podcast in the api of the apple
        Params: @name
        Example: curl -XGET 'http://0.0.0.0:5000/loopkup?name=Crime%20Junkie'
        Response: Array of json in case of exists more
                  that one match of the podcast.
        TODO: add the artistId also as an option to search the podcast
    """
    name = request.args.get("name")
    result = rq.get(PODCAST_API)
    if result.status_code != 200:
        return "Error Reported...!"

    podcasts = result.json()["feed"]["results"]
    response = []
    for i in podcasts:
        if i["name"] == name:
            response.append(i)

    return json.dumps(response, indent=4)


# /ping use this endpoint to check if the server is alive
@app.route('/ping')
def index():
    return "pong"
