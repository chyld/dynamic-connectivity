class QuickFind:
    def __init__(self, n):
        self.groups = n
        self.points = [x for x in range(n)]
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    def find(self, p):
        return self.points[p]
    def union(self, p, q):
        src = self.find(p)
        tgt = self.find(q)
        if src == tgt: return

        self.groups -= 1
        for i, v in enumerate(self.points):
            if v == tgt: self.points[i] = src
    def __str__(self):
        return "groups: {0}; points: {1}".format(self.groups, self.points)
    def __repr__(self):
        return str(self)
