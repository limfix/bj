import sys
import math
import random

gameplay = bool
debug_mode = bool
#проверка наличия файла в котором хранится информация о текущем количестве фишек
try:
    afterload = open('chips.txt','r')
    afterload.close()
except IOError:
    afterload = open('chips.txt','w')
    afterload.write('20000')
    afterload.close()

def print_main_menu():
    print('1 - начать новую игру (сброс до 20000 фишек)')
    print('2 - загрузить игру')
    print('3 - помощь и информация')
    print('4 - выход')

print('Black Jack by limfx. vk.com/lim_f_x')
loop = True
while loop:
    print_main_menu()
    choice = str(input())
    if choice == '1':
        gameplay = True
        chips = open('chips.txt','w')
        chips.write('20000')
        chips.close()
        break;
    elif choice == '2':
        gameplay = True
        break;
    elif choice == '3':
        print('Отображение руки дилера:')
        print('первая карта 2,3,4,5,6,7,8,9,10,J,Q,K,A, вторая скрытая в виде диеза')
        print('Python 3.5. Разработал Аверьев А.О., 2016г. Основы программирования\n')
    elif choice == '4':
        print('See ya!')
        break;
    else:
        print('Введите корректное значение')
        continue

while gameplay == True:
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4
    random.shuffle(deck)
    chips = open('chips.txt','r')
    current_chips = chips.readline()
    chips.close()
    if int(current_chips) <= 0:
        print('У вас не осталось фишек. Счёт восстановлен до 20000')
        current_chips = 20000
    if int(current_chips) > 0:
        bet = input('В данный момент у вас ' + str(current_chips) + ' фишек. Сделайте вашу ставку\n')
        if int(bet) > int(current_chips):
            print('У вас нет столько фишек. Сделайте другую ставку\n')
            continue
        else:
            current_chips = int(current_chips) - int(bet)
    max_parts_of_game = 10
    i = 0
    dealer_count = 0
    dealer_ace_count = 0

    dealer_first_card = deck.pop()
    if dealer_first_card == 2:
        dealer_count += 2;
    if dealer_first_card == 3:
        dealer_count += 3;
    if dealer_first_card == 4:
        dealer_count += 4;
    if dealer_first_card == 5:
        dealer_count += 5;
    if dealer_first_card == 6:
        dealer_count += 6;
    if dealer_first_card == 7:
        dealer_count += 7;
    if dealer_first_card == 8:
        dealer_count += 8;
    if dealer_first_card == 9:
        dealer_count += 9;
    if dealer_first_card == 10 or dealer_first_card == 'J' or dealer_first_card == 'Q' or dealer_first_card == 'K':
        dealer_count += 10;
    if dealer_first_card == 'A':
        dealer_count += 11;
        dealer_ace_count += 1;

    dealer_second_card = deck.pop()
    if dealer_second_card == 2:
        dealer_count += 2;
    if dealer_second_card == 3:
        dealer_count += 3;
    if dealer_second_card == 4:
        dealer_count += 4;
    if dealer_second_card == 5:
        dealer_count += 5;
    if dealer_second_card == 6:
        dealer_count += 6;
    if dealer_second_card == 7:
        dealer_count += 7;
    if dealer_second_card == 8:
        dealer_count += 8;
    if dealer_second_card == 9:
        dealer_count += 9;
    if dealer_second_card == 10 or dealer_second_card == 'J' or dealer_second_card == 'Q' or dealer_second_card == 'K':
        dealer_count += 10;
    if dealer_second_card == 'A':
        dealer_count += 11;
        dealer_ace_count += 1;

    user_count = 0
    user_ace_count = 0
    user_first_card = deck.pop()
    if user_first_card == 2:
        user_count += 2;
    if user_first_card == 3:
        user_count += 3;
    if user_first_card == 4:
        user_count += 4;
    if user_first_card == 5:
        user_count += 5;
    if user_first_card == 6:
        user_count += 6;
    if user_first_card == 7:
        user_count += 7;
    if user_first_card == 8:
        user_count += 8;
    if user_first_card == 9:
        user_count += 9;
    if user_first_card == 10 or user_first_card == 'J' or user_first_card == 'Q' or user_first_card == 'K':
        user_count += 10;
    if user_first_card == 'A':
        user_count += 11;
        user_ace_count += 1;

    user_second_card = deck.pop()
    if user_second_card == 2:
        user_count += 2;
    if user_second_card == 3:
        user_count += 3;
    if user_second_card == 4:
        user_count += 4;
    if user_second_card == 5:
        user_count += 5;
    if user_second_card == 6:
        user_count += 6;
    if user_second_card == 7:
        user_count += 7;
    if user_second_card == 8:
        user_count += 8;
    if user_second_card == 9:
        user_count += 9;
    if user_second_card == 10 or user_second_card == 'J' or user_second_card == 'Q' or user_second_card == 'K':
        user_count += 10;
    if user_second_card == 'A':
        user_count += 11;
        user_ace_count += 1;

    main_user_cards_string = ('Ваши карты: ' + str(user_first_card) + ' ' + str(user_second_card) + ' ')
    main_dealer_cards_string = ('Карты дилера: ' + str(dealer_first_card) + ' ' + str(dealer_second_card) + ' ')
    print('Карты дилера: ' + str(dealer_first_card) + '#')
    print('Ваши карты: ' + str(user_first_card) + ' ' + str(user_second_card)+ '. Текущий счёт: ' + str(user_count));
    answer = input(str('Берём карту? Y/N\n'))
    if ((answer == 'Y') or (answer == 'y')):
        user_gameplay = True
        user_other_cards = []
        while user_gameplay == True:
            for i in range(max_parts_of_game):
                user_other_cards.append(deck.pop())
                main_user_cards_string = str(main_user_cards_string) + str(user_other_cards[i]) + ' '
                if user_other_cards[i] == 2:
                    user_count += 2
                if user_other_cards[i] == 3:
                    user_count += 3
                if user_other_cards[i] == 4:
                    user_count += 4
                if user_other_cards[i] == 5:
                    user_count += 5
                if user_other_cards[i] == 6:
                    user_count += 6
                if user_other_cards[i] == 7:
                    user_count += 7
                if user_other_cards[i] == 8:
                    user_count += 8
                if user_other_cards[i] == 9:
                    user_count += 9
                if user_other_cards[i] == 10 or user_other_cards[i] == 'J' or user_other_cards[i] == 'Q' or user_other_cards[i] == 'K':
                    user_count += 10
                if user_other_cards[i] == 'A':
                    user_count += 11
                    user_ace_count += 1
                if (user_count > 21) and (user_ace_count > 0):
                    user_count -= 10
                    user_ace_count -= 1
                    second_answer = input('Счёт: ' + str(user_count) + ' ' + (main_user_cards_string) + ' Играем дальше? Y/N \n')
                    if ((second_answer == 'Y') or (second_answer == 'y')):
                        i += 1
                        user_gameplay = True
                        continue
                    elif ((second_answer == 'N') or (second_answer == 'n')):
                        user_gameplay = False
                        dealer_gameplay = True
                        break
                    else:
                        print('Введите корректное значение')
                        continue
                if user_count > 21:
                    user_gameplay = False
                    dealer_gameplay = False
                    break;
                if user_count == 21:
                    user_gameplay = False
                    dealer_gameplay = True
                    break;
                if user_count < 21:
                    second_answer = input('Счёт: ' + str(user_count) + ' ' + (main_user_cards_string) + ' Играем дальше? Y/N \n')
                    if ((second_answer == 'Y') or (second_answer == 'y')):
                        i += 1
                        user_gameplay = True
                    elif ((second_answer == 'N') or (second_answer == 'n')):
                        user_gameplay = False
                        dealer_gameplay = True
                        break
                    else:
                        print('Введите корректное значение')
                        continue
    elif ((answer == 'N') or (answer == 'n')):
        user_gameplay = False
        if int(dealer_count) > int(user_count):
            dealer_gameplay = False
        else:
            dealer_gameplay = True
    else:
        print('Введите корректное значение')
        continue

    i = 0
    while dealer_gameplay == True:
        if (dealer_count >= 18) and (dealer_count <= 21):
            dealer_gameplay = False
        if (dealer_count > user_count):
            dealer_gameplay = False
        dealer_other_cards = []
        for i in range(max_parts_of_game):
            dealer_other_cards.append(deck.pop())
            main_dealer_cards_string = str(main_dealer_cards_string) + str(dealer_other_cards[i]) + ' '
            if dealer_other_cards[i] == 2:
                dealer_count += 2
            if dealer_other_cards[i] == 3:
                dealer_count += 3
            if dealer_other_cards[i] == 4:
                dealer_count += 4
            if dealer_other_cards[i] == 5:
                dealer_count += 5
            if dealer_other_cards[i] == 6:
                dealer_count += 6
            if dealer_other_cards[i] == 7:
                dealer_count += 7
            if dealer_other_cards[i] == 8:
                dealer_count += 8
            if dealer_other_cards[i] == 9:
                dealer_count += 9
            if dealer_other_cards[i] == 'J' or dealer_other_cards[i] == 'Q' or dealer_other_cards[i] == 'K':
                dealer_count += 10
            if dealer_other_cards[i] == 'A':
                dealer_count += 11
                dealer_ace_count += 1
            if (dealer_count > 21) and (dealer_ace_count > 0):
                dealer_count -= 10
                dealer_ace_count -= 1
                dealer_gameplay = True
                if (dealer_count > user_count):
                    dealer_gameplay = False
                    break;
                break;
            if (dealer_count >= 18) and (dealer_count <= 21) and (dealer_count >= user_count):
                dealer_gameplay = False
                break;
            if (dealer_count > user_count):
                dealer_gameplay = False
                break;

    while dealer_gameplay == False:
        if (user_count > dealer_count) and (user_count <= 21):
            print('Победа. У вас больше очков чем у дилера')
            print('Счёт дилера: ' + str(dealer_count) + ' ' + str(main_dealer_cards_string))
            print('Ваш счёт: ' + str(user_count) + ' ' + main_user_cards_string)
            current_chips = int(current_chips) + int(bet)*2
            break;
        if (user_count == dealer_count) and (user_count <= 21) and (dealer_count <= 21):
            print('Ничья.')
            print('Счёт дилера: ' + str(dealer_count) + ' ' + str(main_dealer_cards_string))
            print('Ваш счёт: ' + str(user_count) + ' ' + main_user_cards_string)
            current_chips = int(current_chips) + int(bet)
            break;
        if (user_count < dealer_count) and (dealer_count <= 21):
            print('Вы проиграли.')
            print('Счёт дилера: ' + str(dealer_count) + ' ' + str(main_dealer_cards_string))
            print('Ваш счёт: ' + str(user_count) + ' ' + main_user_cards_string)
            break;
        if (dealer_count > 21) and (user_count <= 21):
            print('Победа. У дилера перебор')
            print('Счёт дилера: ' + str(dealer_count) + ' ' + str(main_dealer_cards_string))
            print('Ваш счёт: ' + str(user_count) + ' ' + main_user_cards_string)
            current_chips = int(current_chips) + int(bet)*2
            break;
        if (user_count > 21):
            print('Перебор.')
            print('Ваш счёт: ' + str(user_count) + ' ' + main_user_cards_string)
            break;
        if (user_count == 22) and (user_first_card == 'A') and (user_second_card == 'A'):
            print('Победа! Black Jack!')
            current_chips = int(current_chips) + int(bet)*2
            break;

    chips_write = open('chips.txt','w')
    chips_write.write(str(current_chips))
    chips_write.close()
    repeat_game = input('Начать новую игру? Y/N\n')
    if ((repeat_game == 'Y') or (repeat_game == 'y')):
        new_game = True
    elif ((repeat_game == 'N') or (repeat_game == 'n')):
        gameplay = False
    else:
        print('Введите корректное значение')
        continue
while gameplay == False:
    print('See ya!')
    break;
