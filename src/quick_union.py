class QuickUnion:
    def __init__(self, n):
        self.groups = n
        self.points = [x for x in range(n)]
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    def find(self, p):
        while p != self.points[p]:
            p = self.points[p]

        return p
    def union(self, p, q):
        parent = self.find(p)
        child = self.find(q)
        if parent == child: return

        self.groups -= 1
        self.points[child] = parent
    def __str__(self):
        return "groups: {0}; points: {1}".format(self.groups, self.points)
    def __repr__(self):
        return str(self)
