import sys
import time
from quick_find import QuickFind
from quick_union import QuickUnion
from weighted_quick_union import WeightedQuickUnion

option = input('(t)iny, (m)edium, (l)arge: ')
f = open('./data/' + option + '.txt', 'r')
points = int(f.readline())
network = WeightedQuickUnion(points);

begin = time.time()

for line in f:
    p, q = list(map((lambda x: int(x)), line.split()))
    network.union(p, q);

end = time.time()

print("groups: {0}; time: {1}".format(network.groups, end - begin))
