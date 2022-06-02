from questions import numbers_list

def check_n2() -> None:
    if sorted(numbers_list) != numbers_list:
        raise Exception('N2 is Incorrect!')
    
    print('N2 Success')


if __name__ == '__main__':
    check_n2()
