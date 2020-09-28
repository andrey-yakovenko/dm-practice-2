from pulp import *

prob = LpProblem('Toy Factory', LpMaximize)
x = LpVariable('Toy_A_Type', 0, None, LpInteger)
y = LpVariable('Toy_B_Type', 0, None, LpInteger)
prob += 25 * x + 20 * y, 'Total profit; to be maximized'
prob += 20 * x + 12 * y <= 2000, 'Units constraint'
prob += 5 * (x + y) <= 540, 'Time constraint'  # 9 h = 540 min
prob.writeLP('ToyFactory.lp')
prob.solve()

print('Status:', LpStatus[prob.status])
for v in prob.variables():
    print(v.name, '=', v.varValue)
print('Total profit that could be earned =', value(prob.objective))
