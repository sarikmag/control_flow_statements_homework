def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """

    y = a%10
    y = y*10
    x = a//10
    b = y + x
    if b<=a:
        return 'True'
    return 'False'
print(main(21))
    