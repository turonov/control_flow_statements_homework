def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
   
    d = 0
    if(a>=0):
        d += 1
    if(b>=0):
        d += 1
    if(c >= 0):
        d += 1
                     
    return d


print(main(4,-8, 5))    