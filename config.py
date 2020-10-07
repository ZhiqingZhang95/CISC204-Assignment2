
# DO NOT EDIT

# Assignment for 18zz119

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (Q|(~R|~P))
s2 = ((P|~Q)&(Q|P))
s3 = ((P|R)|~Q)
s4 = ((~R|P)&(R|P))

s5 = ((T>>R)>>(S|(~T&R)))
s6 = ((~R>>(~T&S))|~(T|~R))
