"""
This script is an example of how to pick groups of 'r' people randomly from within a larger sample of N people such that no single person appears in two groups.
I find this script useful when I have to divide my employees into groups randomly

First Output:


$ python random_generator.py
Groups chosen are:
0. ('Shiva', 'Rahul')
1. ('Smitha', 'Nilaya')
2. ('Mohan', 'Raji')
3. ('Preedhi', 'Annapoorani')
4. ('Kiran', 'Avinash')
5. ('Raj', 'Rohan D.')
6. ('Indira', 'Rohini')
7. ('Sravanti', 'Akkul')

"""
import argparse
import itertools
import random

#Note: Listing employees just to keep the example short
#You would (ideally) get a list of employees from some central datastore
#UPDATE EMPLOYEES TO SUIT YOUR CONTEXT
EMPLOYEES = ['Raji', 'Avinash', 'Shiva', 'Annapoorani', 'Rohan D.', 'Smitha', 'Indira', 'Rohan J.', 'Nilaya', 'Mohan', 'Rohini', 'Sravanti', 'Rahul', 'Preedhi', 'Raj', 'Kiran', 'Akkul']

def check_no_overlap(my_tuple, reference_list):
    """
    Verify if at least one member of a tuple overlpas with the members in a list of tuples
    :return result_flag: boolean
    """
    result_flag = True
    for reference_tuple in reference_list:
        result_flag &= set(my_tuple).isdisjoint(set(reference_tuple))
        if result_flag is False:
            break

    return result_flag

def get_groups(group_size):
    """
    Return groups of size group_size
    :return groups: list of tuples
    """
    unique_groups = []
    expected_num_groups = int(len(EMPLOYEES)/group_size)
    #We shuffle the combinations to keep the order fresh everytime
    random.shuffle(EMPLOYEES)
    if group_size >= len(EMPLOYEES):
        unique_groups.append(tuple(EMPLOYEES))
    else:
        #all_combos is a list of all group_size combinations
        all_combos = list(itertools.combinations(EMPLOYEES, group_size))

        #Our next step is to make the groups disjoint
        #'disjoint' = One employee cannot appear in two groups
        for combo in all_combos:
            if check_no_overlap(combo, unique_groups):
                unique_groups.append(combo)
            #A small optimization is to stop checking combos once we reach the expected number of groups
            if len(unique_groups) == expected_num_groups:
                break

    return unique_groups

#----START OF SCRIPT
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', dest = 'size', type = int, default = 2, help = 'Size of the group you want')
    args = parser.parse_args()
    if args.size < 1:
        parser.error(f'Invalid argument --size {args.size}. Group size should be an positive integer.')
    groups = get_groups(args.size)
    if len(groups):
        print('Groups chosen are:')
        for i, group in enumerate(groups):
            print(f'{i}. {group}')