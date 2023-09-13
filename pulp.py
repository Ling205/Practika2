import pulp
import time

from pulp import value

start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += x1 + 4 * x2 >= 4, "Функция цели"
problem += x1 + x2 <= 6, "1"
# problem +=x1 >= 2, "2"
problem += x2 >= 0, "2"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Прибыль:")
print(value(problem.objective))
stop = time.time()
print("Время :")
print(stop - start)
