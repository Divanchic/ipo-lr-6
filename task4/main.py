lst = (list(map(str, input("введите текст").split())))
txt = open(r"C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr6\task4\text.txt", "r", encoding = "UTF-8") 
rd = txt.read()
if rd == lst:
    print(rd)