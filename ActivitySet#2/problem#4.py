

def get_cs():
    """get string input"""
    a = input("enter the input")
    return(a)

def cs_to_lot(cs):
    """convert connected string to list of strings"""
    y = []
    lt = cs.split()
    for i in lt:
        x = (i.split('='))
        y.append(tuple(x))
    return y

def lot_to_cs(lot):
    """convert list of strings to connected string"""
    
    for j in lot:
        

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)

main()
