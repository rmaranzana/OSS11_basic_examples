import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na, get_usage_string, get_min_cut

# IMPORT THE DATA:
NN = np.array([[0, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0]])

# DATA MANIPULATION:
Aeq, arc_idxs = nn2na(NN)
C = np.array([0, 0, 0, 0, 0, 0, 0, -1])
beq = np.array([0, 0, 0, 0, 0, 0])
max_q = [7, 1, 2, 3, 2, 1, 2, None]
bounds = tuple([(0, max_q[arcs]) for arcs in range(0, Aeq.shape[1])])

print('## Optimizer inputs ## \n'
      'Cost vector: %s \n '
      'A_eq Node-Arc matrix:\n%s \n'
      'b_eq demand-supply vector: %s \n'
      'Bounds of each X arc variable: %s \n' % (C, Aeq, beq, bounds))

# OPTIMIZE:
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method='simplex')

# GET THE SOLUTION:
usage = get_usage_string(arc_idxs, res.x.astype(int), max_q)
min_cut = get_min_cut(arc_idxs, res.x, np.array(max_q))
max_flow = res.fun * -1
print('## Results ## \n'
      'The usage of each arc will be (from, to): %s \n'
      'The arcs that produce the minimum cut (from, to): %s \n'
      'The maximum flow will be: %0.2f ' % (usage, min_cut , max_flow))