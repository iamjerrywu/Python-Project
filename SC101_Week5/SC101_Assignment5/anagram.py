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
    while True:
        input_word = input("Find anagrams for:")

        # check if input string = "EXIT, need to break the loop
        if input_word == EXIT:
            break

        # check whether input string valid format (is alpha letters)
        for item in input_word:
            if not item.isalpha():
                print("Invalid word format, please enter again")
                break
        # First should find all the permutations of the input string
        # Since input string might contains duplicated letter i.e. contains (n repeated twice)
        # Doing string in sorted form will help we do pruning in recursion letter to reduce T(n) run-time
        find_anagrams(sorted(input_word))


# read all the words from dictionary.txt file
# here are two python dict:
#   1. prefix_dict: to store every prefix of the word from dictionary.txt file (not including itself)
#      help reducing the recursive searching time (if unfinised permutation is not in prefix_dict, then can break early)
#   2. word_dict: to store the word from dictionary.txt
#      use to check whether the final permutation is equal to word exactly
def read_dictionary():
    with open(FILE, 'r') as f:
        # remove the line breaker '\n'
        words = f.read().splitlines()
        for word in words:
            for i in range(len(word) - 1):
                # store all prefix of word in prefix_dict
                prefix = word[:i + 1]
                if prefix not in prefix_dict:
                    prefix_dict[prefix] = True
            # store all word in word_dict
            word_dict[word] =True


def dfs(string, anagram, res, visited, search):

    # print "Searching" to indicate programs is actually running in case of long time no response
    if not search[0]:
        print("Searching...")
    search[0] = True

    cnt[0] +=1
    anagram_str = ''.join(anagram)
    # base case of recursion:
    # if every position in string has been visited, and anagram string is valid (in word_dict)
    # add anagram string to result
    if len(visited) == len(string) and anagram_str in word_dict:
        res.append(anagram_str)
        search[0] = False
        print("Found: ", anagram_str)
        return
    # pruning, avoid useless searching
    # when anagram exist (bypass '') and it's not in prefix_dict, then no need to go further searching
    if anagram and not has_prefix(anagram_str):
        return
    # traverse all the element in string
    for i in range(len(string)):
        # 1. use visited(set) to record positions that has been visited within string, if already visited, continue!
        # 2. for duplicated letters, since already sorted, same letter must in order, continue if followed case happen!
        #    - when same letters in order and when permutations start from previous same letter have all be searched
        if i in visited or string[i] == string[i - 1] and i - 1 not  in visited:
            continue
        # recorded the already visited position
        visited.add(i)
        # add letter to anagram
        anagram.append(string[i])
        # keep dfs recursion
        dfs(string, anagram, res, visited, search)
        # backtracking that remove letter from anagram
        anagram.pop()
        # remove the visited position
        visited.remove(i)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    cnt[0] = 0
    res = []
    # do Depth-First Search" recursively to find all anagrams of input string
    # s: input sorted string
    # []: list that store anagram
    # res: list that store all valid anagram
    # set(): used to record visited position within string
    # []: liste 1st element to control print("start search")
    dfs(s, [], res, set(), [False])
    print(str(len(res)), "anagrams:", res)
    print(cnt[0])


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    return sub_s in prefix_dict


if __name__ == '__main__':
    main()

