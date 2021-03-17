"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
prefix_dict = {}
word_dict = {}
cnt = [0] * 1


def main():
    input_word = None
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or " + EXIT + " to quit)")
    while input_word != EXIT:
        input_word = input("Find anagrams for:")

        #check whether input string valid format
        for item in input_word:
            if not item.isalpha():
                print("Invalid word format, please enter again")
                break
        find_anagrams(input_word)


def read_dictionary():
    with open(FILE, 'r') as f:
        words = f.read().splitlines()
        for word in words:
            for i in range(len(word) - 1):
                prefix = word[:i + 1]
                if prefix not in prefix_dict:
                    prefix_dict[prefix] = True
            word_dict[word] =True
        prefix_dict[''] = True


def dfs(string, anagram, res, visited):
    # print(''.join(anagram))
    cnt[0] +=1
    if len(visited) == len(string) and word_dict.get(''.join(anagram), False) and ''.join(anagram) not in res:
        print(''.join(anagram))
        res.add(''.join(anagram))
        return
    if not has_prefix(''.join(anagram)):
        return
    for i in range(len(string)):
        if i in visited:
            continue
        visited.add(i)
        anagram.append(string[i])
        dfs(string, anagram, res, visited)
        anagram.pop()
        visited.remove(i)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    cnt[0] = 0
    dfs(s, [], set(), set())


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    return prefix_dict.get(sub_s, False)


if __name__ == '__main__':
    main()

