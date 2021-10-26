class TransformDict:
    def __init__(self, transFunc) -> None:
        self.transFunc = transFunc
        self.dict = {}
    def __repr__(self) -> str:
        return self.dict.__repr__()
    def __eq__(self, o: object) -> bool:
        return isinstance(o, TransformDict) and self.dict.__eq__(o.dict)
    def __bool_(self) -> bool:
        return self.dict.__bool__()
    def __getitem__(self, key):
        return self.dict[self.transFunc(key)]
    def __setitem__(self, key, value):
        self.dict[self.transFunc(key)] = value
    def __delitem__(self, key: str) -> None:
        del self.dict[self.transFunc(key)]
    def __contains__(self,key):
        return self.dict.__contains__(self.transFunc(key))
    def __len__(self) -> int:
        return self.dict.__len__()
    def __iter__(self):
        return self.dict.__iter__()
    
    
