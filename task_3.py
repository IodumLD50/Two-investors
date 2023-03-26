

#Задание №3

#Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать
#можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут 
#вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

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
