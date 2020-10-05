
from scipy.optimize import linprog

# fx = [-3, -5]                             ;Funcion a optimizar igualada a cero
# restrictions = [[1, 0], [0, 2], [3, 2]]   ;Lado izquierdo de las restricciones
# [4, 12, 18]                               ;Lado derecho de las restricciones
def simplex(fx, restrictions, result_restrictions):
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    # Solve the problem by Simplex method in Optimization (method='revised simplex', method='simplex', )
    res = linprog(fx, A_ub=restrictions, b_ub=result_restrictions,  bounds=(x0_bounds, x1_bounds), method='simplex', options={"disp": True})
    print(res)
    # X = Funcion objetivo
    # Fun = resultado de optimizacion
    return res






# Probando el metodo simplex
fx = [-3, -5]
restrictions = [[1, 0], [0, 2], [3, 2]]
result_restrictions = [4, 12, 18]
simplex(fx, restrictions, result_restrictions)

