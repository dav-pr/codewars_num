# https://www.codewars.com/kata/52c4dd683bfd3b434c000292
import re
import numpy as np


def is_interesting(number, awesome_phrases, flag=True):

      if   number>97:
        if is_polindrom(number) or is_digits_are_sequential_inc_or_dec(number) or is_zero(number) or is_one_value(number,
                                                                                                                  awesome_phrases):
            return 2
        elif flag== True and (is_interesting(number + 1, awesome_phrases, flag=False) == 2 or is_interesting(number + 2, awesome_phrases,flag=False) == 2):
            return 1
        else:
            return 0
      else:
          return 0


def is_polindrom(number):
    """
    fuction check if number is polindrom

    Every digit is the same number: 1111
    The digits are a palindrome: 1221 or 73837


    param 1: number
    return True is number polindrom
    return False is number is not polindrom

    """
    if number>99:
        if type(number) != type(' '):  # check type
            str_num = str(number)
        else:
            str_num = number


        return True if str_num == str_num[::-1] else False

    else:
        return False



def is_digits_are_sequential_inc_or_dec(number):
    """
    check if The digits are sequential, incementing†: 1234
    The digits are sequential, decrementing‡: 4321

    :param number:
    :return: True or False
    """
    if number>99:
        if type(number) != type(' '):  # check type
            str_num = str(number)
        else:
            str_num = number
        arr = np.array(list(str_num), np.int32)
        # check for 0 after 9
        # For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
        for i, value in enumerate(arr):
            if i<len(arr)-1 and  value == 9 and arr[i + 1] == 0:
                arr[i + 1] = 10

        arr = np.diff(arr)
        flag = bool((arr>0).prod()) or bool((arr<0).prod())
        arr=abs(arr)
        arr = bool((arr == 1).prod()) and flag
        return arr

    else:
        return False


def is_zero(number):
    """
    Any digit followed by all zeros: 100, 90000

    :param number:
    :return: True or False. True is Any digit followed by all zeros: 100, 90000
    """
    str_num = str(number) if type(number) != type(' ') else number
    template = re.compile('\d{1}0+')
    if re.fullmatch(template, str_num):
        return True
    else:
        return False


def is_one_value(number, awesome_phrases):
    """
    The digits match one of the values in the awesome_phrases array


    :param number: in digit
    :param awesome_phrases: awesome_phrases array
    :return: True or False
    """
    arr = np.array(awesome_phrases)
    arr = arr == number
    arr = bool((arr == 1).sum())
    return arr




# best solution
def is_good(n, awesome):
    return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0

def is_interesting(n, awesome):
    if n > 99 and is_good(n, awesome):
        return 2
    if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
        return 1
    return 0

if __name__ == '__main__':
    # for testing
    print(is_interesting(3210, []))
