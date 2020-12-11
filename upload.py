import json


def upload_top(req, file_action, message):
    if req.is_json is not True:
        return "{\"Error\":\"Invalid JSON\"}"
    podcast_list = req.get_json()
    if len(podcast_list) < 20:
        return "{\"Error\":\"Amount of podcast is under 20\"}"
    return save_file(podcast_list, file_action, message)


def save_file(podcast_list, file_action, message):
    try:
        f = open("top_20.json", file_action)
        f.write(json.dumps(podcast_list, indent=4))
        f.close()
    except FileExistsError as ferr:
        return "{\"Error\":\"Already Exists Top20 Podcast:"+ferr.strerror+"\"}"
    except OSError as err:
        return "{\"Error\":\"Error Writting File "+err+"\"}"
    return "{\"Ok\":\"Top "+message+"\"}"


def read_top(podcast_id):
    f = open("top_20.json", "r")
    podcast_json = json.loads(f.read())
    new_podcast_dict = []
    for i in podcast_json:
        if i["id"] != podcast_id:
            new_podcast_dict.append(i)
    if len(new_podcast_dict) == len(podcast_json):
        return '{"Warning":"Podcast Id not Found"}'
    return save_file(new_podcast_dict, "w", "Updated file top_20.json")
