class Move:
    disk = 0
    from_stack = 0
    to_stack = 0

    def __init__(self, disk, from_stack, to_stack):
        self.disk = disk
        self.from_stack = from_stack
        self.to_stack = to_stack
