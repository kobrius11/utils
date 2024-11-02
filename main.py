import sys
from pprint import pprint

from src.generic import FileHandler, Salt, HashFactory, HashEnum
import requests




if __name__ == "__main__":
    # file = (
    #     FileHandler.builder
    #         # .set_path(".")
    #         .set_filename('file')
    #         .set_extension('txt')
    #         .set_content('iam a text')
    #         .build()
    # ).write()

    # test = Salt.create_salt(k=30)
    # print(test)

    has = HashFactory.create_hash(HashEnum.MD5, "1234567891")
    print(has)

    r = requests.get("http://127.0.0.1:8000/", params={"x": 3, "y":5}, headers={'Login-Request': str(has)})
    pprint(r.json())
