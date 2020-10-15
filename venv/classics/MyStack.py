

class MyStack:
    stack = []
    id = 0

    def __init__(self,id):
        self.stack = []
        self.id = id

    def push(self,disk_no):
        if self.is_valid(disk_no):
            return self.stack.append(disk_no)

    def last_disk(self):
        if len(self.stack)>0:
            return self.stack[0]

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(len(self.stack) - 1)
        else:
            return "empty stack!!"

    def is_valid(self, disk_no):
        if len(self.stack) == 0:
            return True
        if disk_no < self.stack[len(self.stack)-1]:
            return True
        return False

    def get_index(self,disk):
        for i in range(len(self.stack)):
            if self.stack[i] == disk:
                return len(self.stack) -i
        return -1

    def get_disk(self, idx):
        if len(self.stack) > idx:
            ret_idx = len(self.stack) - idx
            return self.stack[ret_idx]
        return -1

    def get_disk_before(self,disk):
        idx = self.get_index(disk)
        if idx > 0:
            return self.get_disk(idx-1)
        else:
            return -1

    def show(self):
        return self.stack


