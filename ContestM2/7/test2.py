"""
>>> import sys, io
>>> from alt7 import main_func
>>> sys.stdin = io.StringIO(chr(10).join(['5', '60', '20', '00', '10', '30']))
>>> main_func()
Initial array:
60, 20, 00, 10, 30
**********
Phase 1
Bucket 0: 60, 20, 00, 10, 30
Bucket 1: empty
Bucket 2: empty
Bucket 3: empty
Bucket 4: empty
Bucket 5: empty
Bucket 6: empty
Bucket 7: empty
Bucket 8: empty
Bucket 9: empty
**********
Phase 2
Bucket 0: 00
Bucket 1: 10
Bucket 2: 20
Bucket 3: 30
Bucket 4: empty
Bucket 5: empty
Bucket 6: 60
Bucket 7: empty
Bucket 8: empty
Bucket 9: empty
**********
Sorted array:
00, 10, 20, 30, 60
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)