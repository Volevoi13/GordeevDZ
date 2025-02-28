class MyList:
    def __init__(self, size):
        self.n = size if size > 0 else 1
        self.lst = [0] * self.n
        self.w_count = 0
        self.r_count = 0

    def show(self):
        print(self.lst)

    def counts(self):
        return self.w_count, self.r_count

    def set(self, i, v):
        if -100 <= v <= 100 and 0 <= i < self.n:
            self.lst[i] = v
            self.w_count += 1
        else:
            print("Ошибка неправильный индекс или значение")

    def get(self, i):
        if 0 <= i < self.n:
            self.r_count += 1
            return self.lst[i]
        print("Ошибка индекс вне диапазона")
        return None

    def append(self, v):
        if -100 <= v <= 100:
            self.lst.append(v)
            self.n += 1
        else:
            print("Ошибка неправильное значение")

    def add(self, other):
        max_n = max(self.n, other.n)
        new_lst = [(self.get(i) or 0) + (other.get(i) or 0) for i in range(max_n)]
        res = MyList(max_n)
        res.lst = new_lst
        return res

    def sub(self, other):
        max_n = max(self.n, other.n)
        new_lst = [(self.get(i) or 0) - (other.get(i) or 0) for i in range(max_n)]
        res = MyList(max_n)
        res.lst = new_lst
        return res


if __name__ == "__main__":
    a = MyList(int(input("Размер A: ")))
    for i in range(a.n):
        a.set(i, int(input(f"A[{i}]: ")))

    b = MyList(int(input("Размер B: ")))
    for i in range(b.n):
        b.set(i, int(input(f"B[{i}]: ")))

    print("A:")
    a.show()
    print("B:")
    b.show()

    c = a.add(b)
    print("A + B:")
    c.show()

    d = a.sub(b)
    print("A - B:")
    d.show()

    print("Счетчики A:", a.counts())
    print("Счетчики B:", b.counts())
