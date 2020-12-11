from flask import Flask, request
import requests as rq
import json
import os
import upload

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
        return "{\"Error\":\"Error Happend, contact the developer\"}"

    podcasts = result.json()["feed"]["results"]
    response = []
    for i in podcasts:
        if i["name"] == name:
            response.append(i)

    return json.dumps(response, indent=4)


@app.route('/add_top', methods=["POST"])
def upload_top():
    """ /add_top use this endpoint to add the top 20 podcast
        init the file top_20.json
    """
    return upload.upload_top(request, "x", "Saved")


@app.route('/update_top', methods=["POST"])
def update():
    """ /update_top use this endpoint to replace the top 20 podcast
        the function replace the top_20.json file.
    """
    return upload.upload_top(request, "w", "Updated")


@app.route('/remove_podcast', methods=["POST"])
def remove_podcast():
    podcast_id = request.args.get("podcast_id")
    if podcast_id is None or podcast_id == "":
        return '{"Error":"Please add a valid podcast id"}'
    return upload.read_top(podcast_id)


# /ping use this endpoint to check if the server is alive
@app.route('/ping')
def index():
    return "pong"
