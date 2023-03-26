


mike = int(input('Капитал Мaйкла: '))
ivan = int(input('Капитал Ивана: '))
min_summ = int(input('Минимальная сумма инвестиций: '))

if (mike >= min_summ) and (ivan >= min_summ):
    print(2)
elif (mike >= min_summ) and (ivan < min_summ):
    print('Mike')
elif (ivan >= min_summ) and (mike < min_summ):
    print('Ivan')
elif (mike < min_summ) and (ivan < min_summ) and (mike + ivan >= min_summ):
    print(-1)
else:
    print(0)        
