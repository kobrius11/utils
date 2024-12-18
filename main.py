import sys
from pprint import pprint

from src.generic import FileHandler, Salt, HashFactory, HashEnum
from src.request import Headers
import requests
from src.generic import HttpUrl, UrlParams

from src.db.service import TodoService

DBNAME = "users"

# db = (
#     DBControler()
#         .connect_db(DBNAME)
#         .create_table(DBNAME, ["username PRIMARY KEY", "password"])
#         .insert(DBNAME, ["user", "25f9e794323b453885f5181f1b624d0b"])
#         .close()
# )

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

    url_params = UrlParams(
        host="www.google.com",
        schema="https",
        port=443,
        path="",
        query=""
    )
    url = HttpUrl.try_create_url(url_params)

    password_hash = HashFactory.create_hash(HashEnum.MD5, "123456789")

    headers = Headers()
    headers["username"] = str("user")
    headers["password"] = str(password_hash)

    r = requests.get(str(url), headers=headers)
    pprint(r.content)
