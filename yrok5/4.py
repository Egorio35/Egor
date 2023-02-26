x, y = input().split()
if not x.isalpha() and not y.isalpha():
    if x == y:
        print("Формируем массив")
        lst = [["👺"]]*int(x)
        print(lst)