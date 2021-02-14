'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 2:   # ========== Check if word is has at least 2 letters ==========
        return 0
    else:
        if word[0:2] == "th":   # ========== If the first two letters are "th", add one to the count ==========
            return 1 + count_th(word[2:])   # ========== Count the remaining letters ==========
        # ========== Remove the first letter and repeat with the remaining letters ==========
        else:
            return count_th(word[1:])
