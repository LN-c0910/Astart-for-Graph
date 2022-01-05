import math


class ENode:
    # 邻接顶点序号
    adj_vex = 0
    weight = math.inf
    next_adj = None

    def __init__(self, adj_vex, weight, **kwargs):
        self.adj_vex = adj_vex
        self.weight = weight
        if kwargs.get('next_adj'):
            self.next_adj = kwargs['next_adj']
        self.next_adj = None


class VNode:
    # 顶点信息
    data = None
    x = int
    y = int
    first_adj = ENode

    def __init__(self, data, first_adj):
        self.data = data
        self.first_adj = first_adj


class GraphAdjList:
    num_of_vexs = 0
    max_num_of_vexs = 0
    vexs = list()

    def __init__(self, max_num_of_vexs):
        self.max_num_of_vexs = max_num_of_vexs
        self.vexs = [VNode for i in range(max_num_of_vexs)]

    def get_num_of_vertex(self):
        return self.num_of_vexs

    def insert_vex(self, v, index, x, y):
        if self.num_of_vexs >= self.max_num_of_vexs:
            return False
        vex = VNode(v, None)
        vex.x = x
        vex.y = y
        self.vexs[index] = vex
        self.num_of_vexs += 1
        return True

    def delete_vex(self, v):
        for i in range(1, self.num_of_vexs + 1):
            if self.vexs[i].data == v:
                for j in range(i, self.num_of_vexs):
                    self.vexs[j] = self.vexs[j + 1]
                self.vexs[self.num_of_vexs] = None
                self.num_of_vexs -= 1
                for k in range(1, self.num_of_vexs):
                    if self.vexs[k].first_adj is None:
                        continue
                    if self.vexs[k].first_adj.adj_vex == i:
                        self.vexs[k].first_adj = None
                        continue
                    current = self.vexs[k].first_adj
                    while current is not None:
                        previous = current
                        current = current.next_adj
                        if current is not None and current.adj_vex == i:
                            previous.next_adj = current.next_adj
                            break
                # 对每一个ENode中的adjvex进行修改
                for h in range(1, self.num_of_vexs + 1):
                    current = self.vexs[h].first_adj
                    while current is not None:
                        if current.adj_vex > i:
                            current.adj_vex -= 1
                        current = current.next_adj
                return True
        return False

    # 定位顶点
    def index_of_vex(self, v):
        for i in range(1, self.num_of_vexs + 1):
            if self.vexs[i].data == v:
                return i
        return -1

    # 定位指定位置的顶点
    def value_of_vex(self, pos):
        if pos < 0 or pos > self.num_of_vexs:
            return None
        return self.vexs[pos].data

    # 插入边
    def insert_edge(self, v1, v2, weight):
        if v1 < 0 or v2 < 0 or v1 > self.num_of_vexs or v2 > self.num_of_vexs:
            raise IndexError
        vex1 = ENode(v2, weight)
        # 索引为index1的顶点没有邻接顶点
        if self.vexs[v1].first_adj is None:
            self.vexs[v1].first_adj = vex1
        # 索引为index1的顶点有邻接顶点
        else:
            vex1.next_adj = self.vexs[v1].first_adj
            self.vexs[v1].first_adj = vex1
        vex2 = ENode(v1, weight)
        # 索引为index2的顶点没有邻接顶点
        if self.vexs[v2].first_adj is None:
            self.vexs[v2].first_adj = vex2
        # 索引为index1的顶点有邻接顶点
        else:
            vex2.next_adj = self.vexs[v2].first_adj
            self.vexs[v2].first_adj = vex2
        return True

    @classmethod
    def getEdge(cls, serial, serial1):
        pass
