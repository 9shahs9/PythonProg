
from MyStack import MyStack
from Move import Move


class TowerOfHanoi:

    '''
    simple case of 3 stacks and 5 disks
    Hard coding can be removed after core logic is in place.
    '''

    stacks = []
    moves_stack =[]

    def __init__(self):
        self.moves_stack = []
        for i in range(0,3):
            self.stacks.append(MyStack(i))
        stack1 = self.stacks[0]
        for j in range(5,0,-1):
            stack1.push(j)

    def display(self):
        for i in range(0,3,1):
            print(f'stack {i} :')
            print(self.stacks[i].show())

    def start_game(self):
        move = Move(5,0,2)
        self.make_move2(move)

    def get_dest_stack(self, move):
        stacks_list = [0,1,2]
        stacks_list.remove(move.from_stack)
        stacks_list.remove(move.to_stack)
        return stacks_list[0]


    def make_move2(self, move):
        disk_above = 0
        dest_stack = 0
        # move.disk -1 disk to be moved from src to spare
        if move.disk > 1:
            disk_above = self.stacks[move.from_stack].get_disk_before(move.disk)
            dest_stack = self.get_dest_stack(move)
            self.make_move2(Move(disk_above, move.from_stack, dest_stack))

        # move.disk from src to dest
        self.stacks[move.from_stack].pop()
        self.stacks[move.to_stack].push(move.disk)
        print(f' Stack {move.from_stack} latest position is : {self.stacks[move.from_stack].show()}')
        print(f' Stack {move.to_stack} latest position is : {self.stacks[move.to_stack].show()}')

        # move.disk-1 disks to be moved from spare to dest.
        if move.disk > 1:
            self.make_move2(Move(disk_above, dest_stack, move.to_stack))



    def make_move(self,move):
        self.moves_stack.append(move)
        if self.stacks[move.to_stack].is_valid(move.disk):
            if self.stacks[move.from_stack].peek() == move.disk:
                self.stacks[move.from_stack].pop()
                self.stacks[move.to_stack].push(move.disk)
                print(f' Stack {move.from_stack} latest position is : {self.stacks[move.from_stack].show()}')
                print(f' Stack {move.to_stack} latest position is : {self.stacks[move.to_stack].show()}')
                this_move = self.moves_stack.pop(len(self.moves_stack) - 1)
                if len(self.moves_stack) > 0:
                    next_move = self.moves_stack.pop(len(self.moves_stack) - 1)
                    self.make_move(next_move)
            else:
                dest_stack = self.get_dest_stack(move)
                src_stack = move.from_stack
                move_disk = self.stacks[src_stack].get_disk_before(move.disk)
                new_move = Move(move_disk, src_stack, dest_stack)
                self.make_move(new_move)
        else:
            to_stack_top = self.stacks[move.to_stack].last_disk()
            dest_stack = self.get_dest_stack(move)
            src_stack = move.to_stack
            shuffle_move = Move(to_stack_top,src_stack,dest_stack)
            self.make_move(shuffle_move)




game = TowerOfHanoi()
game.start_game()



