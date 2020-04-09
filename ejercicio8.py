text = (input("ingrese cadena o frase a descomponer  ")).lower()
ok=True
while(ok==True):
    conta = 0
    letra=(input("ingrese letra a buscar")).lower()
    for i in text:
        if (i.isalpha()):
            if(letra==i):
             conta+=1  
    print ("la letra: ",letra," se repite: ",conta," veces")
    print("si quiere buscar otra letra ingrese 1 sino ingrese 0")
    con=(int(input("ingrese opcion  ")))
    if(con == 1):
        ok = True
    else:
        if(con==0):
            ok=False