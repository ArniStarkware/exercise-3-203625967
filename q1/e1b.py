def dfs(tree):
    stack = [tree]
    while stack:
        cur = stack.pop()
        yield cur[0]
        for child in cur[1][::-1]:
            stack.append(child)