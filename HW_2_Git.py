# https://www.codewars.com/kata/52c4dd683bfd3b434c000292
import re

def is_interesting(number, awesome_phrases):
    pass


def is_polindrom(number):

    """
    fuction check if number is polindrom

    Every digit is the same number: 1111
    The digits are a palindrome: 1221 or 73837


    param 1: number
    return True is number polindrom
    return False is number is not polindrom

    """
    if type(number) != type(' '): #check type
        str_num = str(number)

    return True if str_num == str_num[::-1] else False

def is_zero(number):
    """
    Any digit followed by all zeros: 100, 90000

    :param number:
    :return: True or False. True is Any digit followed by all zeros: 100, 90000
    """
    str_num = str(number) if type(number) != type(' ') else number
    template=re.compile('\d{1}0+')
    if re.fullmatch(template, str_num):
        return True
    else:
        return False



if __name__ == '__main__':
    print(is_zero(12345))
    print(is_zero(1000))
    print(is_zero(10))
    print(is_zero(90))
    print(is_zero(900))
    print(is_zero(9000))
    print(is_zero(9001))
    print(is_zero(19000))







