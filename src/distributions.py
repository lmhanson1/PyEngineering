import math
from .calculus import integral

def normal_dist(mean, sd, x2, x1=None):

    def pdf(x):
        part1 = 1/(math.sqrt(2*math.pi*sd**2))
        part2 = -(x-mean)**2/(2*sd**2)
        part3 = math.e**(part2)
        return part1*part3
    
    if x1:
        z1 = (x1-mean)/sd
        z2 = (x2-mean)/sd
        return integral(pdf,z1,z2)
    else:
        z2 = (x2-mean)/sd
        return integral(pdf,-6,z2)
