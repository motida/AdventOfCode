from collections import deque
LENGTH = 14
with open('input6.txt') as f:
    
    idx = LENGTH
    dq = deque(f.read(idx))
        
    while (l:=len(set(dq))) != LENGTH: 
    # read by character
        char = f.read(1)
        if not char:
            break
        dq.popleft()
        dq.append(char)
        idx+=1      

    if l == LENGTH:
        print(idx)

         
    
 