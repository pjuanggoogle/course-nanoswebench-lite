class MultiValueDict(dict):
    def setlist(self, key, list_):
        super().__setitem__(key, list(list_))

    def getlist(self, key, default=None):
        try:
            return list(super().__getitem__(key))
        except KeyError:
            return []
