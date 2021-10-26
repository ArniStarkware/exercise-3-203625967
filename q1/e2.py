from _typeshed import Self
from os import listdir
from os.path import isfile, isdir, join, basename

class entry:
    
    def __init__(self, path) -> None:
        # self.path = path
        self.name = basename(path)
        if isdir(path):
            self.type = 'dir' 
        elif isfile(path):
            self.type = 'file'
        else:
            self.type = 'other'
        if self.type == 'file':
            self.skip = False

def walk(root):
    queue = [join(root, file) for file in sorted(listdir(root))]
    while queue:
        cur = queue.pop(0)
        ent = entry(cur)
        yield ent
        if ent.type == 'file':
            queue.append([join(cur, file) for file in sorted(listdir(root))])
