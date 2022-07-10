def get_cs():
    a = input("Enter the input:")
    return(a)

def cs_to_lot(cs):
    """convert connected string to list of strings"""
    y = []
    lt = cs.split(";")
    for i in lt:
        x = (i.split("="))
        y.append(tuple(x))
    return y
def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)
  
main()
