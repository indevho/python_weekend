with open('D:\\python\\workspace\\p221105\\gugudan.txt', 'a', encoding='utf8') as gugudan:
    with open('D:\\python\\workspace\\p221105\\number2.txt', 'r', encoding='utf8') as hundred:
        gugudan.write(hundred.read())