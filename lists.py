if __name__ == '__main__':    
    N = int(input())
    list =[]
    for i in range(N):
        commands=input().split()
        
        if commands[0]=='insert':
           list.insert(int(commands[1]),int(commands[2]))
        if commands[0]=='print':
            print(list)
        if commands[0]=='remove':
            list.remove(int(commands[1]))
        if commands[0]=='append':
            list.append(int(commands[1]))
        if commands[0]=='sort':
            list.sort()
        if commands[0]=='pop':
            list.pop()
        if commands[0]=='reverse':
            list.reverse()
