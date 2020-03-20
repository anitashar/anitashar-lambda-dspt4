

def enlarge(n):
    return n*100




if __name__ == '__main__':

    print("global scope")

    y = float(input('Please input a number to enlarge: '))
    print(enlarge(y))