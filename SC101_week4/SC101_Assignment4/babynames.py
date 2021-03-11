"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

Author:
sheng-hao wu

File:
source code of data processing based on yearly (1900~2010) baby's name ranking profile
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # check if name already in dictionary
    if name in name_data:
        # update year's rank in following condition:
        # 1: year not in year/rank dict, add sub-dict
        # 2: if year inside, check if existed rank value larger than new rank, if yes, update to new rank
        if year not in name_data[name] or year in name_data[name] and int(name_data[name][year]) > int(rank):
            name_data[name][year] = rank
    # if not, add sub-dict
    else:
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    # 1st line is year and only
    with open(filename, 'r') as f:
        year = f.readlines()[0].strip()
    # after 1st line, each line contains rank, name1, name2
    with open(filename, 'r') as f:
        name_data_lines = f.readlines()[1:]
        # traverse each line
        for name_data_line in name_data_lines:
            # delimiters ',' to separate line into three components
            name_data_list = name_data_line.split(',')
            rank = name_data_list[0].strip()
            name1 = name_data_list[1].strip()
            name2 = name_data_list[2].strip()
            add_data_for_name(name_data, year, rank, name1)
            add_data_for_name(name_data, year, rank, name2)

def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    # init empty name_data dictionary
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    res = []
    for name in name_data:
        # find if target in name_data (case-insensitive)
        if target.lower() in name.lower():
            res.append(name)
    return res



def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
