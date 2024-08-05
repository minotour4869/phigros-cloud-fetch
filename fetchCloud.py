import os
import json
import base64
import struct
import requests
from dotenv import load_dotenv
from decryptRecord import decrypt_record
from miscs import global_headers, HOST

class Player:
    def __init__(self, session_token):
        self.__headers = global_headers.copy()
        self.__headers["X-LC-Session"] = session_token
        self.summary = self.get_summary()
        self.record = self.get_record()

    def get_player(self):
        r = requests.get(HOST + "/users/me", headers=self.__headers)
        return r.json()["nickname"]

    def get_summary(self):
        r = requests.get(HOST + "/classes/_GameSave", headers=self.__headers)
        result = r.json()["results"][0]

        username = self.get_player()
        updatedAt = result["updatedAt"]
        url = result["gameFile"]["url"]
        
        summary = base64.b64decode(result["summary"])
        summary = struct.unpack("=BHfBx%ds12H" % summary[8], summary)
        return {
            "username": username,
            "updatedAt": updatedAt,
            "url": url,
            "saveVer": summary[0],
            "challenges": summary[1],
            "rks": summary[2],
            "display_rks": f"{summary[2]:.2f}",
            "gameVer": summary[3],
            "avatar": summary[4].decode(),
            "completion": {
                "EZ": summary[5:8],
                "HD": summary[8:11],
                "IN": summary[11:14],
                "AT": summary[14:17]
            }
        }

    def get_record(self):
        return decrypt_record(self.summary["url"])

    def get_b19(self):
        record = self.record.copy()
        record = sorted(record, key=lambda x: x["play_rating"], reverse=True)
        return record[:19]

if __name__ == "__main__":
    load_dotenv()
    player = Player(os.getenv("SESSION_TOKEN"))
    print(player.summary)
    with open("decrypted.txt", "w") as f:
        json.dump(decrypt_record(player.summary["url"]), f, indent=4)
