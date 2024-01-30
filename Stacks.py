class MinStack:
    def __init__(self):
        self.container = []
        self.min_val = 0

    def push(self, val: int) -> None:
        if not self.container:
            self.container.append(0)
            self.min_val = val
        else:
            diff = val - self.min_val
            self.container.append(diff)
            if diff < 0:
                self.min_val = val

    def pop(self) -> None:
        if not self.container:
            raise IndexError("Poping from an empty MinStack", stacklevel=2)
        else:
            diff = self.container.pop()
            if diff < 0:
                top = self.min_val
                self.min_val = self.min_val - diff
            else:
                top = diff + self.min_val
            return top

    def top(self) -> int:
        if not self.container:
            raise IndexError("Toping from an empty MinStack", stacklevel=2)
        else:
            diff = self.container[-1]
            if diff < 0:
                top = self.min_val
            else:
                top = diff + self.min_val
            return top

    def getMin(self) -> int:
        if not self.container:
            raise IndexError(
                "Requesting minimal value from an empty MinStack", stacklevel=2
            )
        return self.min_val
