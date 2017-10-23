def pyth_triplets(n=1000):
    
    for x in xrange(1, n):
        x2= x*x # time saver
        for y in xrange(x+1, n): # y > x
            z2= x2 + y*y
            zs= int(z2**.5)
            if zs*zs == z2 and x+y+zs==1000:
                yield x, y, zs
                return "Product: ",x*y*zs


print list(pyth_triplets())
