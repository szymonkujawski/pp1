def f(palindrome):
    backwords = palindrome
    backwords_list = list(backwords)
    backwords_list.reverse()
    palindrome_list = list(palindrome)

    if palindrome_list== backwords_list:
        return True
    else:
        return False
    
print(f("radar"))
print(f("12-11-21"))
print(f("book"))
