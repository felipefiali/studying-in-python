# Given a string S made only of english characters, check whether you can make it a palindrome by removing just one character

def check_if_palindrome_removing_1_char(value):
    i = 0
    j = len(value) - 1

    diffs = 0

    while j > i:
        if value[i] == value[j]:
            i += 1
            j -= 1
        else:
            if diffs > 0:
                return False
            else:
                diffs += 1

            if i + 1 == j:
                return True
            else:
                if value[i + 1] == value[j]:
                    i += 1
                elif value[j - 1] == value[i]:
                    j -= 1
                else:
                    return False

    return True