print ('''Это квест.
Вы находитесь в замке на котроый совершают нападение.
Вы в главном зале и его постепенно начинают заполнять войска.
Вы спрятались за трон
Выберите что хотите сделать:
1.Скрыться через тайный проход.
2.Аккуратно посмотреть сколько солдат в зале
3.С криком "В АТАКУ" выбежать на противников.''')
player =input("Введите номер выбраного варианта")
if player == "1":
    print('''Вам удается подобраться к тайному проходу незамеченным.
Но он оказывается заперт.
Рядом вы замечаете подозрительный шкаф
Подойдя к нему вы замечате 3 странные книги: красную, желтую и зеленую.
Выберите номер варианта:
1. Потянуть на себя красную книгу.
2. Потянуть на себя желтую книгу.
3. Потянуть на себя зеленую книгу.''')
    player =input("Введите номер выбраного варианта")
    if player == "1":
        print()
    elif player == "2":
        print()
    elif player == "3":
        print()
elif player == "2":
    print("Вы увидели солдата в метре от себя и с ужасом понимаете что вас заметили")
Вставить рандомность удачи оправдаться.
elif player == "3":
    print('''Вам в колено прилетает стрела.
Кажется это была плохая идея).''')
else:
    print("YOU DIED")