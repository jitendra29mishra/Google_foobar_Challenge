# Find the Access Codes
# =====================

# In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured 
# with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but 
# only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access 
# codes once you're ready to go in. 

# Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in order to 
# help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, 
# you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, 
# if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

# Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet 
# the requirement i < j < k. The length of l is between 2 and 2000 inclusive. The elements of l are between 1 and 999999 inclusive. The answer fits within 
# a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
# (int list) l = [1, 1, 1]
# Output:
# (int) 1

# Inputs:
# (int list) l = [1, 2, 3, 4, 5, 6]
# Output:
# (int) 3

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your 
# solution passes the test cases, it will be removed from your home folder.

def answer(l):
    res = 0
    i = 0
    n_l = len(l) - 2
    while i < n_l:
        first = l[i]
        j = i + 1
        while j < n_l + 1:
            if l[j]%first == 0:
                res += sum([1 for k in l[j+1:] if k%l[j]==0])
            j+=1
        i+=1
    return res

print(answer([1,2,3,4,5,6]))
print(answer([1,1,1]))
print(answer([1,2,3,5,7,11]))