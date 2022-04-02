a = "Первое значение"

def test1():
    a = "Второе"
    print(a)
    def test2():
        nonlocal a
        a = "test2"
        print(a)
    test2()
    print(a)

print(a)
test1()
print(a)