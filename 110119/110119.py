import matplotlib.pyplot as plt
import random
from statistics import mean

n_trials = 10000000
order = [1,2,3,4,5,6,7,8,9,10]
accepted_rank = []

trial = 0
while trial < n_trials:
    random.shuffle(order)
    for i in range(10):
        so_far = order[:i+1]
        so_far.sort()
        rsf = so_far.index(order[i]) + 1
        if (i > 2 and rsf == 1) or (i > 4 and rsf == 2) or (i > 6 and rsf == 3) or (i > 7 and rsf == 4) or (i > 8):
            accepted_rank.append(order[i])
            trial += 1
            break

plt.hist(accepted_rank, rwidth=0.6, align='left', bins=range(1, 12))
plt.xticks(range(1,11))
plt.title('Expected rank: %.4f (%i trials)' % (mean(accepted_rank), len(accepted_rank)))
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.show()
