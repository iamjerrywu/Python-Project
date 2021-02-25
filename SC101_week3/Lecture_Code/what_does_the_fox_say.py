"""
File: what_does_the_fox_say.py
Name: Jerry Liao
----------------------------------
This program shows the basic concepts of
Python dict by inputting data from Youtube
video What Does the Fox Say
"""


def main():
    """
    Add some sound of animals!
    """
    sounds = {}
    sounds['dog'] = 'woof'
    sounds['cat'] = 'meow'
    sounds['bird'] = 'tweet'
    sounds['fox'] = 'grininindergeringer'
    sounds['fox'] = 'wapappapapapapa'

    print_dict(sounds)



def print_dict(d):
    """
    : param d: The dict containing the sound of animals
    ------------------------------------------------
    This function prints out all the key-value pairs in d
    """
    for key in d:
        value = d[key]
        print(key, "->", value)


if __name__ == '__main__':
    main()
