from xo import Token

def boardSetup():
    print('''
    ___________________
    |     |     |     |
    |     |     |     |
    |___ _|_____|_____|
    |     |     |     |
    |     |     |     |
    |___ _|_____|_____|
    |     |     |     |
    |     |     |     |
    |___ _|_____|_____|
    ''')

def main():
    num1 = Token()
    num1.setPos(10, 20)
    pos = num1.getPos()
    print(pos)
    numbers=[]
    for i in range(10):
        newNum = Number(i, i)
        numbers.append(newNum)
    for number in numbers:
        print(number)


if __name__ == '__main__':
    main()