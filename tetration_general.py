import sympy
def tetrate(n, h, g=1):
    x, u=sympy.symbols('x u')
    co=sympy.symbols(f'a1:{n+1}')
    fu=sum(co[i-1]*u**i for i in range(1, n+1))
    uu=(sympy.exp(u+1)-1).series(u, 0, n+1).removeO()
    fexp=fu.subs(u, uu).series(u, 0, n+1).removeO()
    d=fexp-fu-1
    s=[d.coeff(u, i) for i in range(n)]
    sol=sympy.solve(s, co)
    slog_approx=fu.subs(sol).subs(u, x - 1)
    f=slog_approx-h
    dfdx=sympy.diff(f, x)
    current_x=float(g)
    for i in range(10):
        fx=float(f.subs(x, current_x))
        dfx=float(dfdx.subs(x, current_x))
        current_x=current_x-(fx/dfx)
    return slog_approx, current_x
n=5
h=0.5
slog, v=tetrate(n, h)
print(sympy.latex(slog))
print(v)