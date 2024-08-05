import struct
from ratingList import rating_list

difficulty = ["EZ", "HD", "IN", "AT", "Legacy"]
difficulty_list = rating_list("difficulty.tsv")

def getBool(num, index):
        return bool(num & 1 << index)

class ByteReader:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def read_record_len(self):
        num = self.data[self.pos]
        self.pos += 1 + (num >= 128)
        return num

    def read_string(self):
        length = self.data[self.pos]
        # print(length)
        self.pos += length + 1
        # print(self.data[self.pos - length:self.pos])
        return self.data[self.pos - length:self.pos].decode()

    def read_score_acc(self):
        self.pos += 8
        data = struct.unpack("if", self.data[self.pos - 8: self.pos])
        return {"score": data[0], "acc": data[1]}

    def read_record(self, songId: str):
        record_end = self.data[self.pos] + self.pos + 1

        # played
        self.pos += 1
        played = self.data[self.pos]

        # fc
        self.pos += 1
        fc = self.data[self.pos]

        diff = difficulty_list[songId]
        self.pos += 1

        # print(played, fc)
        
        records = []
        for d in range(len(diff)):
            if getBool(played, d):
                record = self.read_score_acc()
                record["songId"] = songId
                record["difficulty"] = difficulty[d]
                record["rating"] = float(diff[d])
                record["play_rating"] = (record["acc"]-55)/45
                record["play_rating"] = record["play_rating"]*record["play_rating"]*record["rating"]
                records.append(record)
        return records

        
        
