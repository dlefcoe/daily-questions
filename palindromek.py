'''

courtesy of d ross.


'''



def is_palindrome(string):
    """ Return whether string is palindrome."""
    return string == string[::-1]


def can_make_palindrome(string, k):
    """Check whether palindrome is achievable."""
    counter = dict()

    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1

    # Count number of letters that appear an odd number of times
    odds = len([x for x in counter if counter[x] % 2 != 0])

    if odds > k + 1:
        return "Impossible"
    else:
        print("Pallindrome possible, attempting..")
        return bruteforce(string, k)

counter = 0
def bruteforce(string, k, *args):
    """Return whether palindrome can be made by removing at most k chars."""
    if len(string) < 2 or is_palindrome(string):
        return True

    if k == 0:
        return False

    # Recursively remove up to k chars from all positions
    global counter
    for pos in range(len(string)):
        oneless = string[:pos] + string[pos + 1:]
        removed = string[pos]
        #print(oneless, f"removed {*args, removed}")
        counter += 1
        if bruteforce(oneless, k - 1, *args, removed, counter):
            print('counter:', counter)
            print(oneless, f"removed {*args, removed}")
            return True
    
    return False

#x = can_make_palindrome("waterrfetawx", 2)
x = can_make_palindrome("wzlaxgterrfetawx", 6)
print(x)
