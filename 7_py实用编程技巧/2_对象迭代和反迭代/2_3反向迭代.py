class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    # 正向迭代器
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    # 反向迭代器
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


if __name__ == '__main__':
    print("正向序列")
    for x in FloatRange(1.0, 4.0, 0.5):
        print(x)

    print("反向序列")
    for x in reversed(FloatRange(1.0, 4.0, 0.5)):
        print(x)