import Point as p
import GraphAdjList as g

'''
     求两点间的估算代价， 启发函数一（曼哈顿距离）： (Math.abs(x1 - x2) + Math.abs(y1 - y2))
     启发函数二（平方的欧几里得距离）：((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 -y1))
     启发函数三（欧几里得距离）：(int) Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) *(y2 -y1))
     启发函数四（对角线距离）：Math.max(Math.abs(x1 - x2), Math.abs(y1 -y2)) 
     不用启发函数：0
'''


def get_guess_length(x1, y1, x2, y2):
    # return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
    # return Math.max(Math.abs(x1 - x2), Math.abs(y1 - y2));
    # return 0;


class AStar:
    def __init__(self):
        # 打开的列表
        self.openMap = dict()
        # 关闭的列表
        self.closeMap = dict()
        # 障碍物
        self.barrier = set()
        # 起点
        self.startPoint = p.Point
        # 终点
        self.endPoint = p.Point
        # 当前使用节点
        self.currentPoint = p.Point
        # 循环次数，为了防止目标不可到达
        self.num = 0
        # 存储的数据结构
        self.graph_adj_list = g.GraphAdjList

    '''
      初始化并开始计算最佳路径
      @param x1 出发点x
      @param y1 出发点y
      @param x2 终止点x
      @param y2 终止点y
    '''
    def move(self, x1, y1, x2, y2, barrier):
        self.num = 0
        self.barrier = barrier
        self.startPoint = self.find_near_point(x1, y1)
        self.endPoint = self.find_near_point(x2, y2)
        self.endPoint = p.Point(x2, y2)
        self.closeMap[self.startPoint.get_key()] = self.startPoint
        self.currentPoint = self.startPoint
        self.toOpen(self.startPoint)
        return self.endPoint

    '''
    对用户输入的点坐标，寻找旁边最近的出发点
    '''
    def find_near_point(self, x1, y1):
        num_of_vexs = self.graph_adj_list.get_num_of_vertex()
        if num_of_vexs > 0:
            min_num = get_guess_length(x1, y1, self.graph_adj_list.vexs[1].x, self.graph_adj_list.vexs[1].y)
            index = 1
            for i in range(2,num_of_vexs + 1):
                temp_min = get_guess_length(x1, y1, self.graph_adj_list.vexs[i].x, self.graph_adj_list.vexs[i].y)
                if temp_min < min_num:
                    min_num = temp_min
                    index = i
            return p.Point(self.graph_adj_list.vexs[index].x, self.graph_adj_list.vexs[index].y, index)
        return p.Point(x1, y1, serial_number=0)

    '''
    把该节点相邻点加入计算
    '''
    def to_open(self, point):
        adj_point = set()
        if self.graph_adj_list.vexs[point.serial].firstadj is None:
            return
        else:
            current = self.graph_adj_list.vexs[point.serial].firstadj
            while current is not None:
                adj_point.add(current.adjvex)
                current = current.nextadj
        for serial in adj_point:
            self.add_open_point(p.Point(self.graph_adj_list.vexs[serial].x, self.graph_adj_list.vexs[serial].y, serial),
                                self.graph_adj_list.getEdge(self.currentPoint.serial, serial))

        self.num += 1
        if self.num <= 4000:
            self.to_close()

    '''
    把该节点相邻点加入关闭的列表
    '''
    def to_close(self):
        pass

    '''
        A*核心处理函数
        point currentPoint连接的点
        gCost 当前点到该点的消耗  
    '''
    def add_open_point(self, current_point, g_cost):
        pass


