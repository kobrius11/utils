import sys

from src.generic import FileHandler, Salt, HashFactory, HashEnum


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

    has = HashFactory.create_hash(HashEnum.MD5, "12322112233")
    print(has)

