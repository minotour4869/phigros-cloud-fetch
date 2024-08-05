import requests
import zipfile
import io
from Crypto.Cipher import AES
from Crypto.Util import Padding 
from miscs import key, iv
from ByteReader import ByteReader

def read_record(url):
    result = requests.get(url).content
    with zipfile.ZipFile(io.BytesIO(result)) as zip:
        with zip.open("gameRecord") as record:
            if record.read(1) != b"\x01":
                raise "Invalid record"
            return record.read()

def decrypt_record(url):
    print("Reading record...")
    record = read_record(url)

    print("Decrypting...")
    record = AES.new(key, AES.MODE_CBC, iv).decrypt(record)
    record_raw = Padding.unpad(record, AES.block_size)

    print("Parsing...")
    records = []
    reader = ByteReader(record_raw)
    for i in range(reader.read_record_len()):
        song_id = reader.read_string()[:-2]
        record = reader.read_record(song_id)
        records.extend(record)
    return records
