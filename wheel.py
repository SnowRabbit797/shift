import pulp
import igraph as g
import matplotlib.pyplot as plt

problem = pulp.LpProblem('LP', pulp.LpMinimize)

n = 100 # nを頂点数とする
x = [0] * n
G=g.Graph()

for i in range(n):
    x[i] = pulp.LpVariable('x' + str(i), cat='Integer')

for i in range(0,n-1):
    problem += x[i] + x[(i+1) % (n-1)] >= 1

for i in range(0,n-1):
    problem += x[n-1] + x[i] >= 1
    
for i in range(0,n):
    problem += 0 <= x[i] <= 1

obj = 0
for i in range(n):
    obj += x[i]


problem += obj 

status = problem.solve()

print('status:', pulp.LpStatus[status])

for i in range(n):
    print("x" + str(i) + "=", x[i].value())
    
print("obj", problem.objective.value())