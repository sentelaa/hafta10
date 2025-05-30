import sys

s2=sys.argv[2]
s3=sys.argv[3]

k = s2.split('=')[1]
k1=s3.split('=')[1]




def uret(str):

    a=''
    b=0
    k = str[2]
    l = str[3]

    a = k.split('=')[1]
    b = l.split('=')[1]

    return a,b
x , y = uret(sys.argv)


