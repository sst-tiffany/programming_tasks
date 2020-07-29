class Magic:
    def __init__(self):
        self.value = 0
        self.pos_cnt = 0
        self.neg_cnt = 0

    def __eq__(self, other):
        return self.value == other

    def __pos__(self):
        if self.pos_cnt == 1:
            self.pos_cnt = 0
            self.value += 1
            return self.value
        else:
            self.pos_cnt += 1
            return self

    def __neg__(self):
        if self.neg_cnt == 1:
            self.neg_cnt = 0
            self.value -= 1
            return self.value
        else:
            self.neg_cnt += 1
            return self


i = Magic()

assert i == 0
assert ++i == 1
assert ++i == 2
assert --i == 1
assert --i == 0
assert --i == -1
