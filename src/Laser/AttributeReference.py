class AttributeReference:
    def __init__(self, callable_ref:callable):
        self._callable_ref = callable_ref

    def get(self):
        return self._callable_ref()
        