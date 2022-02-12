import json


def aggregate_nodes(response_json):  # a list consists of user_response, followers_response, following_response
    """
    {
        nodes: {
            id_str: {
                name: "",
                username: ""
            }
        }
    }
    """
    user_nodes = {"nodes": {}}
    for rj in response_json:
        for data in rj["data"]:
            user_nodes["nodes"].setdefault(
                str(data["id"]),
                {
                    "name": data["name"],
                    "username": data["username"],
                }
            )
            json_str = json.dumps(user_nodes, indent=4, sort_keys=True, ensure_ascii=False)

    with open("json/user_nodes.json", "w", encoding="utf-8") as f:
        f.write(json_str)

    return user_nodes


def get_name(user_id):
    with open("json/user_nodes.json", "r") as f:
        json_obj = json.load(f)
        name = json_obj["nodes"][str(user_id)]["name"]

    return name


def get_user_name(user_id):
    with open("json/user_nodes.json", "r") as f:
        json_obj = json.load(f)
        user_name = json_obj["nodes"][str(user_id)]["username"]

    return user_name


def get_followers_json(user_id):
    return f'{user_id}_followers.json'


def get_following_json(user_id):
    return f'{user_id}_following.json'
