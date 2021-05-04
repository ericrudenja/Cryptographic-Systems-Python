from ctypes import *

# The workaround for the
# REFERENCE C LANGUAGE LINE: unsigned long y=v[0],z=v[1], sum=0,   /* set up */
def code(v, k):
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0)

    # REFERENCE C LINE: delta=0x9e3779b9, n=32 ;  /* a key schedule constant */
    delta = 0x9e3779b9
    n = 32

    # REFERENCE C LINES: while (n-->0) {                       /* basic cycle start */
    #   sum += delta ;
    #     y += (z<<4)+k[0] ^ z+sum ^ (z>>5)+k[1] ;
    #     z += (y<<4)+k[2] ^ y+sum ^ (y>>5)+k[3] ;   /* end cycle */

    while(n>0):
        sum.value += delta
        y.value += (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
        z.value += (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
        n -= 1

    print(y.value, z.value)

print(code([1385482522,639876499], [1,2,3,4]))