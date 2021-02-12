from projectA.src.bar1 import sample


def increment_sample():
    return sample() + 1.


def is_palindrome(s):
    p = s.lower().replace(" ", "")
    return p == p[::-1]
