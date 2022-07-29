def is_palindrome(given_string):
    """
        Returns whether string passed is a palindrome
        Arguments:
        given_string
    """
    reverse_string = given_string[::-1]
    if reverse_string.lower() == given_string.lower():
        return True
    else:
        return False

check_string = 'Kajak'
print(is_palindrome(check_string))