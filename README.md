# PHIGROS CLOUD FETCH
A (re-written?) library to fetch your cloud save of a game called Phigros. It should use your `sessionToken` to call requests to the game's api and return datas for you to use.

## Requirements
- A `sessionToken`, which can be found in the `.userdata` file in your backup of the game.
- `Python >= 3.11`

## Usage
If you just want to test my b19 table implementation, you can do as follow:
1. Create a new `.env` file, with content like below:
```
SESSION_TOKEN='your_sessionToken_here'
```
2. Run `python test.py` and it should generate your information and a B19 table like this:

## Problem
The data in this repo is the data for the version `3.8.0`. If the game is updated and you have newer save, you should follow the tutorial of [7aGiven's Phigros_Resource repo](https://github.com/7aGiven/Phigros_Resource?tab=readme-ov-file#%E4%BD%BF%E7%94%A8%E7%A4%BA%E4%BE%8B) to get the newest `difficulty.tsv` and `music-info.json`. Also this is only my (kinda, since i almost copied from [this repo](https://github.com/7aGiven/PhigrosLibrary)) implementation on the library and not really having a function yet, hope can get more idea and design path for this repo.
