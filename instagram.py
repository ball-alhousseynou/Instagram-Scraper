import json
import urllib
import urllib.request
import numpy as np
from fake_useragent import UserAgent
ua = UserAgent()


class INSTAGRAM:
    def __init__(self) -> None:
        self.base_url = "https://www.instagram.com/"

    def data(self, instagram_user):
        headers = {
            "User-Agent": ua.random
        }
        instagram_url = self.base_url + instagram_user 
        instagram_api = instagram_url + "/?__a=1"
        req = urllib.request.Request(instagram_api, None, headers)
        response_json = urllib.request.urlopen(req).read()
        data = json.loads(response_json)
        followers = data["graphql"]["user"]["edge_followed_by"]["count"]
        following = data["graphql"]["user"]["edge_follow"]["count"]
        biography = data["graphql"]["user"]["biography"]
        posts = data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
        return {"instagram_user": instagram_url,
                "total posts": posts,
                "followers": followers,
                "following": following,
                "biography": biography}


if __name__ == "__main__":
    instagram_page = "championsleague"
    instagram = INSTAGRAM()
    data = instagram.data(instagram_page)
    print(json.dumps(data, indent=4))
