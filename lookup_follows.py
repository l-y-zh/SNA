import requests
import os
import json

from config import BEARER_TOKEN


"""
user.fields is adjustable, options include:
created_at, description, entities, id, location, name,
pinned_tweet_id, profile_image_url, protected,
public_metrics, url, username, verified, and withheld
"""
def get_user_fields(field="created_at"):
    return {"user.fields": field}


def create_url(tail, userid):
    user_id = userid
    url = f'https://api.twitter.com/2/users/{user_id}/follow{tail}'
    
    return url


def create_auth_followers(req):
    req.headers["Authorization"] = f'Bearer {BEARER_TOKEN}'
    req.headers["User-Agent"] = "v2FollowersLookupPython"

    return req


def create_auth_following(req):
    req.headers["Authorization"] = f'Bearer {BEARER_TOKEN}'
    req.headers["User-Agent"] = "v2FollowingLookupPython"

    return req


def connect_to_endpoint_with_tail(fields, tail, userid):
    url = create_url(tail, userid)
    response = requests.request("GET", url, auth=create_auth_followers if tail=="ers" else create_auth_following, params=fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            f'Request returned an error: {response.status_code} {response.text}'
        )
    return response.json() 


from random import randint
if __name__ == "__main__":
    tail = ["ers", "ing"]
    fields = get_user_fields()
    json_response = connect_to_endpoint_with_tail(fields, tail[randint(0, 1)], 2244994945)
    print(json.dumps(json_response, indent=4, sort_keys=True))

