# Variables Used
sharedPrime = 23    # p
sharedBase = 5      # g
 
#Random varaibles chosen by each party

maateSecret = 6     # a
BhagwanSecret = 15      # b
 
# Begin
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , sharedPrime )
print( "    Publicly Shared Base:  " , sharedBase )
 
# ABC Sends DEF A = g^a mod p
A = (sharedBase**ABCSecret) % sharedPrime
print( "\n  ABC Sends Over Public Chanel: " , A )
 
# DEF Sends ABC B = g^b mod p
B = (sharedBase ** DEFSecret) % sharedPrime
print(" DEF Sends Over Public Chanel: ", B )
 
print()

print( "Privately Calculated Shared Secret:" )
# ABC Computes Shared Secret: s = B^a mod p
ABCSharedSecret = (B ** ABCSecret) % sharedPrime
print( "    ABC Shared Secret: ", ABCSharedSecret )
 
# DEF Computes Shared Secret: s = A^b mod p
DEFSharedSecret = (A*DEFSecret) % sharedPrime
print( "    DEF Shared Secret: ", DEFSharedSecret )


Publicly Shared Variables:
    Publicly Shared Prime:  23
    Publicly Shared Base:   5

  ABC Sends Over Public Chanel:  8
 DEF Sends Over Public Chanel:  19

Privately Calculated Shared Secret:
    ABC Shared Secret:  2
    DEF Shared Secret:  2
