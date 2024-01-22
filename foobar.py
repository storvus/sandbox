def foo_bar(num):
    try:
        num = int(num)
    except ValueError:
        print("error")
        return
    fb = ""
    if num % 3 == 0:
        fb += "foo"
    if num % 5 == 0:
        fb += "bar"
    if fb:
        print(fb, end=" ")


print("введите аргумент")
num1 = int(input())

for i in range(num1):
    foo_bar(i)
