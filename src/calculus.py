
def integral(func,a,b,*,method="Simpson"):
    _int = (b-a)/6*(func(a)+4*func((a+b)/2)+func(b))
    return _int

def derivative(func,x,h=1e-10):
    _slope = (func(x+h)-func(x))/h
    return _slope
