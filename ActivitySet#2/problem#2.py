def add(a, b):
    return(a+b)
    pass

def output(a, b, sum):
    print(a,"+",b,"is",sum)
    pass

def main():
    a,b =map(int,input("enter two numbers:").split())
    sum = add(a, b)

    output(a, b, sum)
main()
