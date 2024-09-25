first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y : x==y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open (file_name, mode='w', encoding='UTF-8') as file:
            for set in data_set:
                file.write (str (set)+'\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall:
    def __init__(self, *word):
        self.words = word
    def __call__(self):
        word = choice(self.words)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Никогда', 'Скорей всего', 'Не дождетесь')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())