import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na, get_selected_arcs

# IMPORT THE DATA:
NN = np.array([[0, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0]])

# DATA MANIPULATION:
C = np.array([2, 2, 2, 5, 2, 1, 2])
Aeq, arc_idxs = nn2na(NN)
beq = np.array([1, 0, 0, 0, 0, -1])
bounds = tuple([(0, None) for arcs in range(0, Aeq.shape[1])])

print('## Optimizer inputs ## \n'
      'Cost vector: %s \n '
      'A_eq Node-Arc matrix:\n%s \n'
      'b_eq demand-supply vector: %s \n'
      'Bounds of each X arc variable: %s \n' % (C, Aeq, beq, bounds))

# OPTIMIZE:
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds)

# GET THE SOLUTION:
selarcs = get_selected_arcs(arc_idxs, res.x)
print('## Results ##')
print('The raw solution will be: %s' % res.x)
print('The arcs that make the shortest path will be (from, to): %s' % selarcs)
print('The minimum cost will be: %0.2f ' % res.fun)