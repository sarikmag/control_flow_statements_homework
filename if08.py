def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a/10<10 and a/10>0:
        if a%2==0:
            return 'two-digit even number'
        return 'two-digit odd numer'
    if a/100<10 and a/100>0:
        if a%2==0:
            return 'three-digit even number'
        return 'three-digit odd number'
    if a/10>-10 and a/10<0:
        if a%2==0:
            return 'two-digit even number'
        return 'two-digit odd numer'
    if a/100>-10 and a/100<0:
        if a%2==0:
            return 'three-digit even number'
        return 'three-digit odd number'
    
print(main(57))