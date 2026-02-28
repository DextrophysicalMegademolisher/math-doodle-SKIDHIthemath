import sympy
#i dont even know if t works lol
def multifactorial(n, m, d):
    if n>1:
        return n*factorial(n-m, m, d)
    elif n<0:
        return factorial(n+m, d)/(n+m)
    else:
        x=sympy.symbols('x')
        co=sympy.symbols(f'a0:{d+1}')
        f=sum(co[i]*x**i for i in range(d+1))
        r=[]
        r.append(f.subs(x, 0)-1)
        r.append(f.subs(x, 1)-1)
        for k in range(1, d):
            fk=sympy.diff(f, x, k)
            ff=sympy.diff(f, x, k-1)
            ll=fk.subs(x, 1)
            rr=k*ff.subs(x, 0)+fk.subs(x, 0)
            r.append(ll-rr)
        p=f.subs(sympy.solve(r, co))
        return p.subs(x, n)
d=7 #floating point error ruins higher degree approximations due to chaotic behavior of large matrices, for now 7 is recommended
print(factorial(0.5, m, d))
d=20 #avoids floating point
print(factorial(sympy.S('1/2'), m, 8).evalf())
