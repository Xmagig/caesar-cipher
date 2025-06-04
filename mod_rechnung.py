pars = [("a",1),("b",2),("c",3),("d",4),("e",5),("f",6),("g",7),("h",8),("i",9)
            ,("j",10),("k",11),("l",12),("m",13),("n",14),("o",15),("p",16),("q",17),("r",18)
            ,("s",19),("t",20),("u",21),("v",22),("w",23),("x",24),("y",25),("z",26),(" ",27)]
def mod(x:int,m:int):
    n=round(((x/m)-int(x/m))*m)
    return n
def encode(letter:str):
    for b,z in pars:
        if letter.lower() ==b:
            return z
        else: 
            pass
def decode(number:int):
    for b,z in pars:
        if number == z:
                return b 
def incription(ms:str,PK):
    new_ms = ""
    for b in ms:
        key=mod(int(PK),27)
        c=key+encode(b)
        
        new_ms +=decode(c)

    return new_ms

def decription(PK):
        message=[]
        code=input("enter code or nothing to finish")
        if code == "":
            pass
        else:
            for b in code:
                n=encode(b)
                original=mod(n+27-int(PK),27)
                message.append(original)
        real_mesage=""
        for number in message:
            real_mesage+=decode(number)
        return real_mesage


loop=True
while loop:
    do=input("press 1 to incode \n" \
            "press 2 to decode \n" \
            "nothing to exit\n")
    if do == "":
        do = 0
    else:
        do = int(do)
    if do == 1:
        message = input("enter message")
        key = input("enter key")
        print(incription(message,key))
    elif do == 2:
        key = input("enter key")
        print(decription(key))
    elif do == 0:
        exit()