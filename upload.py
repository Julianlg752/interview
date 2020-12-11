import json


def upload_top(req, file_action):
    if req.is_json is not True:
        return "{\"Error\":\"Invalid JSON\"}"
    podcast_list = req.get_json()
    if len(podcast_list) < 20:
        return "{\"Error\":\"Amount of podcast is under 20\"}"
    try:
        f = open("top_20.json", file_action)
        f.write(json.dumps(podcast_list, indent=4))
        f.close()
    except FileExistsError as ferr:
        return "{\"Error\":\"Already Exists Top20 Podcast:"+ferr.strerror+"\"}"
    except OSError as err:
        return "{\"Error\":\"Error Writting File "+err+"\"}"
    return "{\"Ok\":\"Top Saved\"}"
