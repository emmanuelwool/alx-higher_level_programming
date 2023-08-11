#!/usr/bin/python3

if __name__ == "__main__":
    """Count arguments."""
    import sys

    count = len(sys.argv) - 1
    sum=0
    for i in range(count):
        sum=sum+i
print("sum of arg is {}".format(sum))
