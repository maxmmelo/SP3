import S3

n = 1
classe = S3.semi()
while n != "0":
    print("quin exercici vols veure?")
    print("prèmer 0 per sortir")
    n = input()

    if n == "1":
        classe.exercici1()

    elif n == "2":
        classe.exercici2()

    elif n == "3":
        classe.exercici3()

    elif n == "4":
        classe.exercici4()
    
    else:
    	print("t'has equivocat")
