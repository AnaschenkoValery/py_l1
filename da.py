from datetime import datetime
# -*- coding: utf-8 -*-
def pricetime (price1):
    if 12 <= (datetime.now()).hour < 22:
        print ('Стоимость со скидкой:'), price1*0.8
    else:
        print ('Стоимость без скидки:'), price1
x=float(input('Введи стоимость товара:'))
pricetime (x)
