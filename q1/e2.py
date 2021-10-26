from os import listdir
from os.path import isfile, isdir, join, basename

class entry:
    def __init__(self, path) -> None:
        self.name = basename(path)
        if isdir(path):
            self.type = 'directory' 
        elif isfile(path):
            self.type = 'file'
        else:
            self.type = 'other'
        if self.type == 'directory':
            self.skip_flag = False
    
    def skip(self) -> None:
        if self.type == 'directory':
            self.skip_flag = True

def walk(root):
    queue = [join(root, file) for file in sorted(listdir(root))]
    while queue:
        cur = queue.pop(0)
        ent = entry(cur)
        yield ent
        if ent.type == 'directory' and not ent.skip_flag:
            queue += [join(cur, file) for file in sorted(listdir(cur))]
