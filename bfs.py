def bfs(graph,start):
    visit=set()
    queue=[start]
    visit.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end = ' ')
        for i in graph[node]:
            if i not in visit:
                visit.add(i)
                queue.append(i)
graph={0:[1,4],
       1:[0,2],
       2:[1,3],
       3:[2,4],
       4:[3,0],}
bfs(graph,0)
