n = int(input())
s = set(map(int, input().split()))
no_of_Ops = int(input())
valid_ops = ['pop', 'remove', 'discard']
for _ in range(no_of_Ops):
    line = input().split()
    if(len(line) == 2):
        op = line[0]
        key = int(line[1])
    elif (len(line) == 1):
        op = line[0]
    if op in valid_ops:
        try:
            if op == 'pop':
                print(f'pop {s.pop()} - completed')
            if op == 'remove':
                s.remove(key)
                print('remove - completed')
            if op == 'discard':
                s.discard(key)
                print('discard - completed')
        except:
            sorry = 'do nothing'
print(sum(s))