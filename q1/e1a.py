def bfs(tree):
    queue = [tree]
    while queue:
        cur = queue.pop(0)
        yield cur[0]
        for child in cur[1]:
            queue.append(child)