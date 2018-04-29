
def palindrome_num():
    result = 11
    # 考虑二进制回文得出只能是奇数
    while True:
        if str(bin(result)[2:]) == str(bin(result)[2:][::-1]) \
                and str(result) == str(result)[::-1]\
                and str(oct(result)[2:]) == str(oct(result)[2:][::-1]):
            print(result)
            return
        result += 2


if __name__ == '__main__':
    palindrome_num()