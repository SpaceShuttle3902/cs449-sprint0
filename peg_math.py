#This file contains helper function that we can use unit testing on
#Simple logic of solitaire gamne, for sprint0


#This returns True if the move is exactly two moves, accordig to Peg Solitaire rules
def is_valid_jump_distance(from_pos, to_pos):
    return abs(to_pos - from_pos) == 2

#This function gives performance rating based on the # of marbles left when game ends.
def rating(marbles_left):
    if marbles_left <= 1:#Best outcome if left with 1
        return "Outstanding"
    elif marbles_left == 2:#Left with 2 marbles
        return "Very Good"
    elif marbles_left == 3:#Left with 3 marbles
        return "Good"
    else:#If for or more marbles are left, the rating is labeled average
        return "Average"
