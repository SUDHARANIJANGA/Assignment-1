previous_num = 0
current_num = 1
next_num = 0
lis = [1]
while(current_num+previous_num<51):
    next_num = previous_num + current_num
    previous_num = current_num
    current_num =next_num
    lis.append(next_num)
print(lis)