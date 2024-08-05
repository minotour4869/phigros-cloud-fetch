import os
import json
from colorama import Fore, Style
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv
from fetchCloud import Player

with open("music-info.json", "r") as f:
    music_info = json.load(f)

if __name__ == "__main__":
    load_dotenv()
    player = Player(os.getenv("SESSION_TOKEN"))

    b19 = player.get_b19()
    print(Style.BRIGHT + "Username: " + Style.RESET_ALL + f"{player.summary['username']}")
    print(Style.BRIGHT + "RKS: " + Style.RESET_ALL + f"{player.summary['display_rks']}")

    table = Table("Title", "Difficulty", "Rating", "Score", "Accuracy", "Play rating", "Is it phi?")
    for entry in b19:
        for song in music_info:
            if song["sid"] == entry["songId"]:
                table.add_row(song["title"], entry["difficulty"], f'{entry["rating"]}', f'{entry["score"]}', f'{entry["acc"]:.2f}%', f'{entry["play_rating"]:.2f}', "*" if entry["acc"] == 100 else "")
                break

    console = Console()
    console.print(table)
    
