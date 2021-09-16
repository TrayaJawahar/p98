def SwapFileData ():
    f1 = input("ENTER THE NAME OF THE FIRST FILE:")
    f2 = input ("ENTER THE NAME OF THE SECOND FILE:")

    with open(f1 ,'r') as a:
        data_a=a.read()
    with open(f2 ,'r') as b:
        data_b=b.read()
    with open (f1,'w') as a:
        a.write(data_b)
    with open (f2,'w') as a:
        b.write(data_a)

SwapFileData()