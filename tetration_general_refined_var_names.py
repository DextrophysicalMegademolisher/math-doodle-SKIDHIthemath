import sympy


def get_superlog_approximation(degree, target_height, initial_guess=1.0):
    """
    Approximates the super-logarithm (slog) using Taylor series
    and solves for x given a specific height using Newton's Method.
    """
    x, u = sympy.symbols('x u')

    # Generate coefficients for the polynomial approximation
    coefficients = sympy.symbols(f'a1:{degree + 1}')

    # Define the Abel functional equation components
    # fu represents our super-logarithm polynomial
    fu = sum(coefficients[i - 1] * u ** i for i in range(1, degree + 1))

    # Taylor expansion of (e^(u+1) - 1)
    exp_series = (sympy.exp(u + 1) - 1).series(u, 0, degree + 1).removeO()

    # Substitute and find the difference for the functional equation
    f_expanded = fu.subs(u, exp_series).series(u, 0, degree + 1).removeO()
    difference_eq = f_expanded - fu - 1

    # Solve the system of linear equations for the coefficients
    equations = [difference_eq.coeff(u, i) for i in range(degree)]
    solution = sympy.solve(equations, coefficients)

    # Final slog approximation formula
    slog_formula = fu.subs(solution).subs(u, x - 1)

    # --- Newton-Raphson Solver ---
    # We want to find x such that slog_formula(x) = target_height
    target_function = slog_formula - target_height
    derivative = sympy.diff(target_function, x)

    current_x = float(initial_guess)
    for _ in range(10):
        # Numerical evaluation of the function and its derivative
        f_val = float(target_function.subs(x, current_x))
        df_val = float(derivative.subs(x, current_x))

        # update rule: x = x - f(x)/f'(x)
        current_x -= (f_val / df_val)

    return slog_formula, current_x


# Execution
DEGREE = 2
HEIGHT = 0.5
slog_expr, result_value = get_superlog_approximation(DEGREE, HEIGHT)

print(f"LaTeX Expression: {sympy.latex(slog_expr)}")
print(f"Calculated Value: {result_value}")