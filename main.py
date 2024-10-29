import sys

sys.path.append('./src/')

from generic.file import FileHandler


if __name__ == "__main__":
    file = FileHandler.builder.build()