num_str = int(input("кол-во строк"))
numb = 0
while num_str!=0:
    lst = (list(map(str, input("введите текст").split())))
    numb += len(lst)
    num_str -= 1
print(numb)

