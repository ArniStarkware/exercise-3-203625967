def dfs(tree):
    yield tree[0]
    for child in tree[1]:
        yield from dfs(child)