def is_palindrome(given_string):
    """
        Returns whether string passed is a palindrome
        Arguments:
        given_string
    """
    given_string = given_string.lower()
    reverse_string = given_string[::-1]
    return reverse_string == given_string

check_string = 'Kajak'
print(is_palindrome(check_string))