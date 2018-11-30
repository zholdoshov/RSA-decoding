from sympy.ntheory import isprime,primefactors
from sympy.core.numbers import igcd,mod_inverse
'''
Test 
pub_key=(629,461) where n=629 e=461 
cipher='060001153470225542229524082470234060619577002619046470470619540619423082470234001470000303'
message='Puffballs unequaled.'
'''
def private_key(p,q,e):
    return (p*q,mod_inverse(e,(p-1)*(q-1)))

def public_key(p,q,e):
    return (p*q,e)
def encipher(pub_key,plain):
    n,k=pub_key
    return pow(plain,k,n)

def decipher(prv_key,plain):
    n,k=prv_key
    return pow(plain,k,n)

def decrypt(prv_key,ct):
    d=len(str(prv_key[0]))
    c=[ct[i:i+d] for i in range(0,len(ct),d)]
    m=[]
    for i in c:
        m.append(str(decipher(prv_key,int(i))).zfill(d-1))
    n="".join(m)
    p=[chr(int(n[i:i+3])) for i in range(0,len(n),3)]
    return "".join(p)
def check(p,q,e):
    phi=(p-1)*(q-1)
    return p!=q and isprime(p) and isprime(q) and phi>e and igcd(phi,e)==1
def encrypt(pub_key,pt):
    d=len(str(pub_key[0]))
    if len(pt)%2!=0:
        pt+="x"
    p=[str(ord(i)).zfill(3) for i in pt]
    print (p)
    n="".join(p)
    m=[n[i:i+d-1].zfill(d-1) for i in range(0,len(n),d-1)]
    print (m)
    c=[]
    for i in m:
        c.append(str(encipher(pub_key,int(i))).zfill(d))
    return "".join(c)

if __name__=="__main__":
    n=int(input("Enter n modulus:"))
    e=int(input("Enter e modulus:"))
    m=input("Enter enter message:")
    print ("Please wait! Factoring keys...")
    f=primefactors(n)
    p=f[0]
    q=f[1]
    if check(p,q,e):
        print ("keys are:",(p,q))
        pubk=public_key(p,q,e)
        prvk=private_key(p,q,e)
        print ("public key:",pubk)
        print ("private key:",prvk)
        dect=decrypt(prvk,m)
        print (dect)
        dect+="\np and q :"+str(p)+" "+str(q)+"\n"+"e:"+str(e)+"\n"
        f=open("decrypted.txt","w")
        f.write(dect)
        f.flush()
        f.close()
    else:
        raise ValueError("Conditions are not held")
    
