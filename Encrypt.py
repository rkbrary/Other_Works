
def expomod(a,n,z): # Adapté des notes de BB
    i=n
    r=1
    x=a%z
    while(i>0):
        if i%2==1: r=(r*x)%z
        x=(x**2)%z
        i=i//2
    return r

def pgcd_etendu(n, phi): # Repris du solutionnaire du TP
    if phi == 0: return (1, 0, n) #Cas de base de l'induction
    else:       #Etape d'induction avec phi et (n mod phi)
        (s1, t1, d) = pgcd_etendu(phi, n % phi)
        s = t1
        t = s1 - (n//phi)*t1
        return (s, t, d)

def inverse(n, phi):
    s, t, d=pgcd_etendu(n,phi)
    if d!=1: raise Exception('The inverse of {} mod {} does not exist since their pgcd is {}.'.format(n, phi, d))
    return s%phi


# Part b)
n=41
p=19
q=23
phi=(p-1)*(q-1)
print('phi is {}.'.format(phi))
s=inverse(n,phi)
print('The inverse of {} mod {} is {}.'.format(n, phi, s))

z=p*q
m=123
print('The message of Alice is {}'.format(m))
c=expomod(m,n,z)
decrypted_m=expomod(c,s,z)
print('The decrypted message by Bob is {}'.format(decrypted_m))
if m==decrypted_m: print('The message has been correctly passed!') # It works with n=41, m=123

