#!/bin/bash

export FLASK_APP=main.py
export PODCAST_API=https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json
flask run
