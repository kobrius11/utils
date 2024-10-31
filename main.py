import sys

from src.generic import FileHandler, Salt


if __name__ == "__main__":
    # file = (
    #     FileHandler.builder
    #         # .set_path(".")
    #         .set_filename('file')
    #         .set_extension('txt')
    #         .set_content('iam a text')
    #         .build()
    # ).write()

    print(Salt.create_salt(k=30))
    