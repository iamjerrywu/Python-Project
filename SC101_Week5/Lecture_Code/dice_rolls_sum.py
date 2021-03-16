"""
File: dice_rolls_sum.py
Name:
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    dice_sum(TOTAL)

def helper(target_sum, current, cnt_list):
    cnt_list[0]+=1
    if target_sum == sum(current):
        cnt_list[1] = current[-1]
        print(current)
        print(cnt_list[0])
    else:
        # print(current)
        for roll in range(1, 7):
            if roll > cnt_list[1]:
                cnt_list[1] = float('inf')
                break
            if sum(current) <= target_sum:
                # Choose
                current.append(roll)
                # Explore
                helper(target_sum, current, cnt_list)
                # Un-choose
                current.pop()
            else:
                break

def dice_sum(target_sum):
    cnt_list = [0, float('inf')]
    helper(target_sum, [], cnt_list)

if __name__ == '__main__':
    main()
