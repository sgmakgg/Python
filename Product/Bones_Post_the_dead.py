#coding=utf-8
import random

# Правила игры

def rules():
    print("Игра в кости: Отложи мертвую\n"
          "Правила игры:\n"
          "Количество участников - двое.\n"
          "В игре используется пять костей. В начале жребий определяет очередность ходов.\n"
          "Игрок бросает одновременно все пять костей. Сумма очков записывается за ним,\n"
          "если ни на одной из пяти костей не выпало двоек или пятерок.\n"
          "Если же выпала хотя бы одна двойка или пятерка, то сумма очков игроку не записывается.\n"
          "Та кость, что показала пятерку или двойку, объявляется мертвой: ее откладывают в сторону.\n"
          "Если таких костей несколько, то в сторону откладываются все.\n"
          "Игру продолжает тот же самый участник. При каждом удачном броске его очки плюсуют к записанным прежде.\n"
          "Он выбрасывает кости до тех пор, пока все пять костей не окажутся в мертвых.\n"
          "В таком случае кости передаются следующему игроку, который продолжает игру по тем же правилам.\n"
          "Выигравшим считается тот, кто наберет больше очков. Удачи!")

# Функция ввода имен игроков

def players_name():
    print("Введите свои имена?:\n")
    name=input()
    return name

# Функция бросания кубика

def cube(side=6):
    for i in range(random.randrange(5, 50, 1)):
        number=random.randint(1, side)
    return number

# Кто бросает первым

def who_is_first(players1,players2):
    x = 10
    side1 = 0
    side2 = 0
    while x > 0:
        print(players1, "нажмите 1 для броска или 0 для окончания игры")
        x=int(input())
        if x==1:
            side1=print(cube())
            break
        else:
            print("Введено неверное значение")
    while x > 0:
        print(players2, "нажмите 1 для броска или 0 для окончания игры")
        x = int(input())
        if x == 1:
            side2 = print(cube())
            break
        else:
            print("Введено неверное значение")
    if side1>side2:
        return players1
    elif side2>side1:
        return players2
    else:
        continue



# Игра

#def games():



def main():
    rules()
    players1=players_name()
    players2=players_name()
    print("Здравствуйте, ", players1,"!")
    print("Здравствуйте, ", players2,"!")
    print("Давайте определим кто будет бросать кости первый...")
    who_is_first(players1, players2)
#   print(cube())



main()