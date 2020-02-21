'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# initialize a counter
# set up a helper function
    # keep track of count
    # implement recursion
    #base case is if the word is less than 2 
def count_th(word):
    count = 0

    def count_helper(word, count):
        if len(word) < 2:
            return count
        elif word.startswith('th'):
            return count_helper(word[2:], count + 1)
        else:
           return count_helper(word[1:], count) 

    return count_helper(word, count)