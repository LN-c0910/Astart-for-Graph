class Point:
    serial = None

    def __init__(self, x, y: int, **kwargs):
        super()
        self.x = x
        self.y = y
        self.gCost = int
        self.hEstimate = int
        self.fTotal = int
        # Point 类型
        self.prev = Point
        self.level = 1
        if kwargs.get('serial_number'):
            self.serial = kwargs['serial_number']

    def get_key(self):
        return self.x + "_" + self.y

    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + self.x
        result = prime * result + self.y
        return result

    def __eq__(self, obj):
        if self == obj:
            return True
        if obj is None:
            return False
        if type(obj()) != Point:
            return False
        other = obj
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        return True




