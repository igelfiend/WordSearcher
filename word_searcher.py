# -*- coding: utf-8 -*-

import sys
import pandas as pd


def main(chars):
    data = pd.read_csv("russian_nouns.txt", names=["word"])
    print("total words: {0}".format(len(data)))
    print("searching word for chars: \"{0}\"".format(chars))

    new_data = data
    for char in chars:
        new_data = new_data[new_data["word"].str.contains(char)]
        if len(new_data) == 0:
            print("At char \"{0}\" now data was found".format(char))
            return

    print("found:")
    print(new_data.to_string())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please type contained chars")
        exit(0)
    else:
        main(sys.argv[1])
