'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# initialize a counter
# set up a helper function
    # keep track of count
    # implement recursion
    # base case is if the word is less than 2 / empty because it's 2 characters
    # if the word starts with th
        #add 1 to the counter and slice word to start at the 3rd index next time is recurses the word
        # if it does not start with th then just slice word with 1 to move to the 2nd index so you dont accidently skip if it is in the next index
    #return the helper function

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