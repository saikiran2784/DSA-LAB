adj_list={'A':['B','C'],'B':['A'],'C':['A','D'],'D':['C']}
#adj_list={'1':['2','3'],'2':['1','4'],'3':['1','4'],'4':['2','3','5','6','7'],'5':['7','4'],'6':['4'],'7':['4','5']}
output=[]
visited={}
for node in adj_list.keys():
    visited[node]=False
def dfs(visited,adj_list,n):
    if n not in adj_list.keys():
        print("Node is not present in graph")
        return
    if not visited[n]:
        print(n,end=' ')
        visited[n]=True
        for node in adj_list[n]:
            dfs(visited,adj_list,node)


def dfsiterative(visited,adj_list,n):
    if n not in adj_list.keys():
        print("Node is not present in graph")
        return
    stack=[]
    stack.append(n)
    while stack:
        current=stack.pop()
        if not visited[current]:
            print(current,end=' ')
            visited[current]=True
            for i in adj_list[current]:
                stack.append(i)
    
    

#dfs(visited,adj_list,'A')
dfsiterative(visited,adj_list,'A')

            
