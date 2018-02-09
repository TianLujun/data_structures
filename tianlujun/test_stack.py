from tianlujun.data_structures import *
def matches(op, clo):
    opens = '([{'
    closes = ')]}'
    if op in opens and clo in closes:
        return opens.index(op) == closes.index(clo)
    else:
        return False

def check_parentheses(symbol_string):
    s = Stack()
    balance = True
    index = 0

    while index < len(symbol_string):
        if s.is_empty():
            s.push(symbol_string[index])
        elif s.peek() in '([{' and matches(s.peek(), symbol_string[index]):
            s.pop()
        else:
            s.push(symbol_string[index])
        index = index + 1

    if s.is_empty():
        return True
    else:
        return False

def divide_by_2(dec_num):
    rem_stack = Stack()
    bin_str = ''
    while dec_num > 0:
        rem_stack.push(dec_num % 2)
        dec_num = dec_num // 2
    while not rem_stack.is_empty():
        bin_str = bin_str + str(rem_stack.pop())
    return bin_str

def base_converter(dec_num, base):
    rem_stack = Stack()
    result_string = ''
    digits = '0123456789ABCDEF'

    while dec_num > 0:
        rem_stack.push(dec_num % base)
        dec_num = dec_num // base
    while not rem_stack.is_empty():
        result_string = result_string + str(digits[rem_stack.pop()])
    return result_string

def infix_to_postfix():

    return