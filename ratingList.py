def rating_list(file):
    with open(file, "r") as f:
        data = f.readlines()
        rating_list = {}
        for song in data:
            # print(type(song), song)
            song = song.split('\t')
            rating_list[song[0]] = song[1:]
        return rating_list
