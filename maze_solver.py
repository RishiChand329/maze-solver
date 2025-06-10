from collections import deque

#You can change this map to your own custom maze
maze=[
    ['#','#','#','#','#','#','#'],
    ['#','S',' ',' ','#','E','#'],
    ['#',' ','#',' ','#',' ','#'],
    ['#',' ','#',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#']
]

rows,cols=len(maze),len(maze[0])
directions=[(-1, 0),(1, 0),(0, -1),(0, 1)]


def find_start():
    for i in range(rows):
        for j in range(cols):
            if maze[i][j]=='S':
                return (i, j)
    return None


def bfs(start):
    queue=deque([start])
    visited=set()
    parent={}

    while queue:
        x,y=queue.popleft()
        if maze[x][y]=='E':
            return reconstruct_path(parent,start,(x, y))

        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if(0<=nx<rows and 0<=ny<cols and
                maze[nx][ny]!='#' and (nx,ny) not in visited):
                queue.append((nx,ny))
                visited.add((nx,ny))
                parent[(nx, ny)]=(x, y)

    return None


def dfs(start):
    stack=[start]
    visited=set()
    parent={}

    while stack:
        x,y=stack.pop()
        if maze[x][y]=='E':
            return reconstruct_path(parent,start,(x,y))

        if (x,y) in visited:
            continue
        visited.add((x,y))

        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if (0<=nx<rows and 0<=ny<cols and
                maze[nx][ny]!='#' and (nx,ny) not in visited):
                stack.append((nx,ny))
                parent[(nx,ny)]=(x,y)

    return None


def reconstruct_path(parent,start,end):
    path=[]
    while end!=start:
        path.append(end)
        end=parent[end]
    path.append(start)
    return path[::-1]


# Run
start_pos=find_start()
print("BFS Path:",bfs(start_pos))
print("DFS Path:",dfs(start_pos))
