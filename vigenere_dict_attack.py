#crypto Net Hacker
from time import clock
from math import ceil
#dictionary atack

f=open("words.txt","r")
words=f.read().split()
f.close()

def az(m):
    r=""
    m=m.replace(" ","").lower()
    for i in m:
        if i.isalpha():
            r+=i
    return r


def is_english(m):
    c=0
    w=0
    n=m.split()
    for i in n:
        if az(i) in words:
            c+=1
        else:
            w+=1
    return c>w

def encipher_vigenere(msg,key):
    ciph=""
    key=key*int(ceil(float(len(msg))/len(key)))
    for i,j in zip(msg,key):
        ciph+=chr((ord(i)+ord(j)-32)%95+32)
    return ciph

def decipher_vigenere(ciph,key):
    msg=""
    key=key*int(ceil(float(len(ciph))/len(key)))
    for i,j in zip(ciph,key):
        msg+=chr((ord(i)-ord(j)-32)%95+32)
    return msg

def d_atack(ciph):
    p_var={}
    #looping atack
    for i in words:
        m=decipher_vigenere(ciph,i)
        if is_english(m):
            p_var[i]=m
            break
    return p_var


if __name__=="__main__":
    c=raw_input("Enter you cipher text:")
    print "Wait! dictionary atack..."
    t=clock()
    atack=d_atack(c)
    span=clock()-t
    if atack=={}:
        print ":( sorry can't decipher !"
    else:
        print "Key found in ",int(span)," sec"
        for i in atack:
            print "key:",i
            print "text :",atack[i]
            print "finished!"
