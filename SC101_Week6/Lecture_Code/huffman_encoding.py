"""
File: huffman_encoding.py
Name:
-----------------------------------
This program demonstrates the idea of zipping/unzipping
through the algorithm of Huffman Encoding.
We will be using all of the important concepts
we learned today to complete this hugh project.
"""

from ds import Tree, PriorityQueue

# The string to be zipped/unzipped
TARGET = 'stancode sc001 sc101'


def main():
    d = build_dict()

    ############################
    # TODO: Build a priority queue based on d
    priority_queue = PriorityQueue()
    ############################

    tree = encoding(priority_queue)
    print(decoding(tree, '1010101101010100010100110100000101010101100111'))


def build_dict():
    """
    :return: dict, a Python dictionary containing ch as key,
                    the number of ch occurrence as value
    """
    pass


def decoding(tree, unzip_words):
    """
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param unzip_words: str, the mystery compressed binary digits to be unzipped
    :return: str, the unzipped words
    """
    pass


def encoding(pq):
    """
    :param pq: PriorityQueue, containing all the ch we need to encode
    :return: Tree, a binary tree that has all the ch encoded
    """
    pass


if __name__ == '__main__':
    main()
