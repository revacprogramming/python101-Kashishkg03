

def get_cs():
    """get string input"""
    a = input("enter the string:")
    return(a)

def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    d = {}
    x = cs.split(';')
    for a in x:
      c=a.split("=")
      d[c[0]]=c[1]
    return(d)
  

def dict_to_cs(d):
    """convert a dictionary to connect string"""
    str = ""
    for i in d:
        str += i + " "
print(type(str))
print(f"Keys in string- {str}")

def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


main()
