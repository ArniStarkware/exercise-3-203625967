class MultiDict:
    def __init__(self) -> None:
        self.dict = {}
    def __repr__(self) -> str:
        return self.dict.__repr__()
    def __eq__(self, o: object) -> bool:
        return isinstance(o, MultiDict) and self.dict.__eq__(o.dict)
    def __bool_(self) -> bool:
        return self.dict.__bool__()
    def __getitem__(self, key):
        return self.dict[key][0]
    def __setitem__(self, key, value):
        if key in self.dict:
            self.dict[key].append(value)
        else:
            self.dict[key] = [value]
    def __delitem__(self, key: str) -> None:
        lst = self.dict[key]
        if len(lst) > 1:
            lst.pop(0)
        else:
            del self.dict[key]
    def __contains__(self,key):
        return self.dict.__contains__(key)
    def __len__(self) -> int:
        return self.dict.__len__()
    def __iter__(self):
        return self.dict.__iter__()
    def get_all(self, key):
        return self.dict[key]
    def delete_all(self, key):
        del self.dict[key]
