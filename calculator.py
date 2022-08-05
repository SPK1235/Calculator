import pygame
import sys
import numexpr
import datetime


def frame(screen):
    pygame.draw.line(screen, (0, 0, 128), (0, 0), (470, 0), 10)
    pygame.draw.line(screen, (0, 0, 128), (0, 0), (0, 650), 10)
    pygame.draw.line(screen, (0, 0, 128), (0, 650), (470, 650), 10)
    pygame.draw.line(screen, (0, 0, 128), (470, 0), (470, 650), 10)
    text(screen, 15, 'Minsk 2022 SPK Version 2.01', (150, 608), (0, 0, 205))


def text(screen, size, content, point, color_content):
    txt = pygame.font.SysFont('serif', size)
    text_1 = txt.render(content, True, color_content)
    screen.blit(text_1, point)


def button(screen, x, y, length, h, title, x_a, y_a, height):
    pygame.draw.rect(screen, (128, 128, 128), (x, y, length, h), 0)
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + length, y), 3)
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + h), 3)
    pygame.draw.line(screen, (255, 255, 255), (x, y + h), (x + length, y + h), 3)
    pygame.draw.line(screen, (255, 255, 255), (x + length, y), (x + length, y + h), 3)
    el = pygame.font.SysFont('serif', height)
    text_1 = el.render(title, True, (0, 0, 0))
    screen.blit(text_1, (x + x_a, y + y_a))


def display(screen):
    pygame.draw.rect(screen, (128, 128, 128), (15, 15, 440, 120), 0)
    pygame.draw.line(screen, (255, 255, 255), (15, 15), (455, 15), 3)
    pygame.draw.line(screen, (255, 255, 255), (15, 135), (455, 135), 3)
    pygame.draw.line(screen, (255, 255, 255), (15, 15), (15, 135), 3)
    pygame.draw.line(screen, (255, 255, 255), (455, 15), (455, 135), 3)


def keyboard(screen):
    button(screen, 15, 150, 80, 80, '', 30, 0, 65)
    button(screen, 105, 150, 80, 80, '/', 30, 5, 65)
    button(screen, 195, 150, 80, 80, 'x', 30, 5, 55)
    button(screen, 285, 150, 80, 80, '-', 30, 0, 65)
    button(screen, 375, 150, 80, 80, '%', 20, 10, 55)
    button(screen, 15, 240, 80, 80, '7', 23, 5, 65)
    button(screen, 105, 240, 80, 80, '8', 23, 5, 65)
    button(screen, 195, 240, 80, 80, '9', 23, 5, 65)
    button(screen, 285, 240, 80, 170, '+', 20, 50, 70)
    button(screen, 375, 240, 80, 80, ':', 32, 10, 60)
    button(screen, 15, 330, 80, 80, '4', 23, 5, 65)
    button(screen, 105, 330, 80, 80, '5', 23, 5, 65)
    button(screen, 195, 330, 80, 80, '6', 23, 5, 65)
    button(screen, 375, 330, 80, 80, '', 27, 10, 55)
    button(screen, 15, 420, 80, 80, '1', 23, 5, 65)
    button(screen, 105, 420, 80, 80, '2', 23, 5, 65)
    button(screen, 195, 420, 80, 80, '3', 23, 5, 65)
    button(screen, 285, 420, 80, 170, '=', 20, 50, 65)
    button(screen, 15, 510, 170, 80, '0', 68, 5, 65)
    button(screen, 195, 510, 80, 80, '.', 35, 5, 55)
    button(screen, 375, 420, 80, 170, '', 30, 0, 65)
    text(screen, 30, 'Del', (395, 490), (0, 0, 0))
    text(screen, 40, 'X', (402, 350), (0, 0, 0))
    text(screen, 25, 'y', (430, 340), (0, 0, 0))
    text(screen, 25, 'Clear', (27, 180), (0, 0, 0))
    text(screen, 20, 'Time', (392, 245), (0, 0, 0))


def display_output(screen, expression, upper_expression, flag_point, flag_calculation_time):
    display(screen)
    if len(expression) < 14:
        txt = pygame.font.SysFont('serif', 65)
        text_1 = txt.render(expression, True, (0, 0, 0))
        if len(expression) > 2 and expression[-1] == '1':
            x = 450
            y = 65
            k = len(expression) * 32
        elif flag_point and expression not in ['+', '-', '/', 'x', '%', 'LIMIT']:
            x = 450
            y = 65
            k = len(expression) * 33
        elif expression in ['+', '-', '/', 'x']:
            x = 440
            y = 65
            k = len(expression) * 33
        elif expression == '%':
            x = 427
            y = 65
            k = len(expression) * 33
        elif expression == 'LIMIT':
            x = 430
            y = 65
            k = len(expression) * 33
        else:
            x = 460
            y = 65
            k = len(expression) * 33
        screen.blit(text_1, (x - k, y))
        txt_2 = pygame.font.SysFont('serif', 30)
        text_2 = txt_2.render(upper_expression, True, (0, 0, 0))
        x_1 = 440
        y_1 = 25
        k_1 = len(upper_expression) * 15
        if 14 < len(upper_expression) < 25:
            x_1 = 465
        elif len(upper_expression) > 25:
            x_1 = 475
        screen.blit(text_2, (x_1 - k_1, y_1))
        if not flag_calculation_time:
            txt_3 = pygame.font.SysFont('serif', 15)
            text_3 = txt_3.render(' " TIME " ', True, (0, 0, 0))
            screen.blit(text_3, (25, 20))
        pygame.display.update((15, 15, 440, 120))


def result(screen, upper_expression, flag_point, flag_calculation_time):
    try:
        temp = []
        list_upper_expression = list(upper_expression)
        for i in range(len(list_upper_expression)):
            if list_upper_expression[i] == ' ':
                continue
            elif list_upper_expression[i] == 'x':
                temp.append('*')
            elif list_upper_expression[i] == '^':
                temp.append('**')
            else:
                temp.append(list_upper_expression[i])
        temp = ''.join(temp)
        res_1 = numexpr.evaluate(temp)
        res_1 = float(res_1)
        k = 12 - len(str(int(res_1)))
        res_1 = round(res_1, k)
        if res_1 - int(res_1) == 0:
            res_1 = int(res_1)
        if res_1 > 9999999999999:
            res_1 = 'LIMIT'
        expression = str(res_1)
        upper_expression_1 = upper_expression + ' = ' + str(res_1)
        if len(upper_expression_1) > 25:
            upper_expression = upper_expression + ' = '
        else:
            upper_expression = upper_expression + ' = ' + str(res_1)
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
        return str(res_1)
    except ArithmeticError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
    except SyntaxError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)


def interest(screen, upper_expression, flag_point, flag_calculation_time):
    try:
        temp = []
        list_upper_expression = upper_expression.split()
        for i in range(len(list_upper_expression)):
            if list_upper_expression[i] == ' ':
                continue
            else:
                temp.append(list_upper_expression[i])
        if temp[1] == '%':
            res = (float(temp[2]) / 100) * float(temp[0])
            k = 12 - len(str(int(res)))
            res = round(res, k)
            if res - int(res) == 0:
                res = int(res)
            expression = str(res)
            upper_expression = temp[0] + ' % ' + 'от ' + temp[2] + ' = '
            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
            return str(res)
        elif temp[3] == '%':
            res = str(temp[0]) + str(temp[1]) + str(float(temp[0]) / 100 * float(temp[2]))
            res = numexpr.evaluate(res)
            res = float(res)
            k = 12 - len(str(int(res)))
            res = round(res, k)
            if res - int(res) == 0:
                res = int(res)
            expression = str(res)
            upper_expression = upper_expression + ' = '
            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
            return str(res)
        else:
            expression = 'ERROR  '
            upper_expression = '0'
            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
            return 0
    except LookupError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
    except ArithmeticError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
    except SyntaxError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)


def cal_time(screen, upper_expression, flag_point, flag_calculation_time):
    try:
        rez = 0
        a = upper_expression.split()
        time_1_hours = int(a[0][0] + a[0][1])
        time_1_minutes = int(a[0][3] + a[0][4])
        time_2_hours = int(a[2][0] + a[2][1])
        time_2_minutes = int(a[2][3] + a[2][4])
        time_1 = datetime.timedelta(hours=time_1_hours, minutes=time_1_minutes)
        time_2 = datetime.timedelta(hours=time_2_hours, minutes=time_2_minutes)
        if a[1] == '+':
            rez = time_1 + time_2
        elif a[1] == '-':
            rez = time_1 - time_2
        rez = str(rez)
        rez = rez[:-3]
        expression = rez
        upper_expression = upper_expression + ' = '
        display(screen)
        txt = pygame.font.SysFont('serif', 60)
        text_1 = txt.render(expression, True, (0, 0, 0))
        if len(expression) < 6:
            x = 470
            y = 65
            k = len(expression) * 33
        else:
            x = 550
            y = 65
            k = len(expression) * 33
        screen.blit(text_1, (x - k, y))
        txt_2 = pygame.font.SysFont('serif', 30)
        text_2 = txt_2.render(upper_expression, True, (0, 0, 0))
        x_1 = 440
        y_1 = 25
        k_1 = len(upper_expression) * 15
        if 14 < len(upper_expression) < 25:
            x_1 = 465
        elif len(upper_expression) > 25:
            x_1 = 475
        screen.blit(text_2, (x_1 - k_1, y_1))
        txt_3 = pygame.font.SysFont('serif', 15)
        text_3 = txt_3.render(' " TIME " ', True, (0, 0, 0))
        screen.blit(text_3, (25, 20))
        pygame.display.update((15, 15, 440, 120))
    except ArithmeticError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
    except SyntaxError:
        expression = 'ERROR  '
        upper_expression = '0'
        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)


def work():
    pygame.init()
    pygame.display.set_caption(' МОЙ КАЛЬКУЛЯТОР ')
    screen = pygame.display.set_mode((470, 650))
    pygame.Surface.fill(screen, (0, 0, 0))
    pygame.display.set_icon(pygame.image.load('icon.png'))
    pygame.mixer.music.load('click.mp3')
    frame(screen)
    display(screen)
    keyboard(screen)
    expression = '0'
    upper_expression = '0'
    flag_point = True
    flag_input = True
    flag_calculation = True
    flag_degree = True
    flag_interest = True
    flag_calculation_time = True
    display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
    pygame.display.update()
    expression = ''
    sign = ''
    rez = ''
    sign_1 = ''
    col_del = 0
    col_minus = 0
    col_col_minus = 0
    col_time = 0
    col_sign = 0
    upper_expression = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos_mouse = event.pos
                    if 15 <= pos_mouse[0] <= 95 and 150 <= pos_mouse[1] <= 230:
                        """Клавиша Clear """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(15, 150, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((15, 150, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 455, 520))
                        expression = '0'
                        upper_expression = '0'
                        flag_point = True
                        flag_calculation = True
                        flag_degree = True
                        flag_interest = True
                        flag_calculation_time = True
                        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        expression = ''
                        upper_expression = ''
                        col_del = 0
                        col_minus = 0
                        col_col_minus = 0
                        col_time = 0
                        rez = ''
                    elif 105 <= pos_mouse[0] <= 185 and 150 <= pos_mouse[1] <= 230:
                        """Клавиша деление / """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(105, 150, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((105, 150, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 455, 520))
                        if len(expression) != 0 and flag_calculation \
                                and flag_degree and flag_interest and flag_calculation_time:
                            upper_expression = upper_expression + ' / '
                            expression = '/'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            expression = ''
                            flag_point = True
                            flag_input = True
                            flag_calculation = False
                            col_del = 0
                            col_minus += 1
                        elif not flag_calculation and flag_degree and flag_interest and flag_calculation_time:
                            if upper_expression[-1] != ' ':
                                rez = result(screen, upper_expression, flag_point, flag_calculation_time)
                                upper_expression = rez + ' / '
                                expression = ''
                                flag_point = True
                                flag_input = True
                    elif 195 <= pos_mouse[0] <= 275 and 150 <= pos_mouse[1] <= 230:
                        """Клавиша умножения * """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(195, 150, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((195, 150, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 455, 520))
                        if len(expression) != 0 and flag_calculation and flag_degree \
                                and flag_interest and flag_calculation_time:
                            upper_expression = upper_expression + ' x '
                            expression = 'x'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            expression = ''
                            flag_point = True
                            flag_input = True
                            flag_calculation = False
                            col_del = 0
                            col_minus += 1
                        elif not flag_calculation and flag_degree and flag_interest and flag_calculation_time:
                            if upper_expression[-1] != ' ':
                                rez = result(screen, upper_expression, flag_point, flag_calculation_time)
                                upper_expression = rez + ' x '
                                expression = ''
                                flag_point = True
                                flag_input = True
                    elif 285 <= pos_mouse[0] <= 365 and 150 <= pos_mouse[1] <= 230:
                        """Клавиша вычитание - """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(285, 150, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((285, 150, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 455, 520))
                        if flag_calculation_time:
                            if col_minus == 0 and flag_calculation and flag_degree and flag_interest:
                                upper_expression = upper_expression + ' - '
                                expression = '-'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = '-'
                                col_minus += 1
                                col_col_minus += 1
                                if col_col_minus == 2:
                                    flag_calculation = False
                            elif not flag_calculation and flag_degree and flag_interest and flag_calculation_time:
                                if upper_expression[-1] != ' ':
                                    rez = result(screen, upper_expression, flag_point, flag_calculation_time)
                                    upper_expression = rez + ' - '
                                    expression = ''
                            elif not flag_calculation and not flag_degree and col_minus < 1 \
                                    and flag_interest and flag_calculation_time:
                                upper_expression = upper_expression + ' - '
                                expression = '-'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = '-'
                                col_minus += 1
                            flag_point = True
                            flag_input = True
                            col_del = 0
                        elif not flag_calculation_time:
                            if len(expression) == 5 and col_sign == 0:
                                expression = '-'
                                upper_expression += ' - '
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                                col_sign += 1
                    elif 375 <= pos_mouse[0] <= 455 and 150 <= pos_mouse[1] <= 230:
                        """Клавиша проценты % """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(375, 150, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((375, 150, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        flag_interest = False
                        if 0 < len(expression) < 14 and flag_calculation_time:
                            upper_expression += ' % '
                            expression = '%'
                        display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        expression = ''
                    elif 15 <= pos_mouse[0] <= 95 and 240 <= pos_mouse[1] <= 320:
                        """Клавиша 7 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(15, 240, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((15, 240, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '7'
                                upper_expression += '7'
                            else:
                                expression = '7'
                                upper_expression = '7'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 4] and expression[0] in ['0', '1']:
                                expression += '7'
                                upper_expression += '7'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            elif len(expression) == 4 and expression[0] == '2':
                                expression += '7'
                                upper_expression += '7'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 105 <= pos_mouse[0] <= 185 and 240 <= pos_mouse[1] <= 320:
                        """Клавиша 8 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(105, 240, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((105, 240, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '8'
                                upper_expression += '8'
                            else:
                                expression = '8'
                                upper_expression = '8'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 4] and expression[0] in ['0', '1']:
                                expression += '8'
                                upper_expression += '8'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            elif len(expression) == 4 and expression[0] == '2':
                                expression += '8'
                                upper_expression += '8'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 195 <= pos_mouse[0] <= 275 and 240 <= pos_mouse[1] <= 320:
                        """Клавиша 9 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(195, 240, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((195, 240, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '9'
                                upper_expression += '9'
                            else:
                                expression = '9'
                                upper_expression = '9'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 4] and expression[0] in ['0', '1']:
                                expression += '9'
                                upper_expression += '9'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            elif len(expression) == 4 and expression[0] == '2':
                                expression += '9'
                                upper_expression += '9'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 285 <= pos_mouse[0] <= 365 and 240 <= pos_mouse[1] <= 410:
                        """Клавиша сложение + """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(285, 240, 80, 170))
                        pygame.mixer.music.play()
                        pygame.display.update((285, 240, 80, 170))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) != 0 and flag_calculation and flag_degree \
                                    and flag_interest and flag_calculation_time:
                                col_minus += 1
                                upper_expression = upper_expression + ' + '
                                expression = '+'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                                flag_point = True
                                flag_input = True
                                flag_calculation = False
                                col_del = 0
                            elif not flag_calculation and flag_degree and flag_interest and flag_calculation_time:
                                if upper_expression[-1] != ' ':
                                    rez = result(screen, upper_expression, flag_point, flag_calculation_time)
                                    upper_expression = rez + ' + '
                                    expression = ''
                                    flag_point = True
                                    flag_input = True
                        elif not flag_calculation_time:
                            if len(expression) == 5 and col_sign == 0:
                                expression = '+'
                                upper_expression += ' + '
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                                col_sign += 1
                    elif 375 <= pos_mouse[0] <= 455 and 240 <= pos_mouse[1] <= 320:
                        """Вычесление времени"""
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(375, 240, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((375, 240, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        flag_calculation_time = False
                        if col_time == 0:
                            expression = '0'
                            upper_expression = '0'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            expression = ''
                            upper_expression = ''
                            col_time += 1
                        elif col_time == 1 and len(expression) == 2:
                            expression += ':'
                            upper_expression += ':'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 15 <= pos_mouse[0] <= 95 and 330 <= pos_mouse[1] <= 410:
                        """Клавиша 4 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(15, 330, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((15, 330, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '4'
                                upper_expression += '4'
                            else:
                                expression = '4'
                                upper_expression = '4'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 3, 4] and expression[0] in ['0', '1']:
                                expression += '4'
                                upper_expression += '4'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            elif len(expression) in [3, 4] and expression[0] == '2':
                                expression += '4'
                                upper_expression += '4'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 105 <= pos_mouse[0] <= 185 and 330 <= pos_mouse[1] <= 410:
                        """Клавиша 5 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(105, 330, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((105, 330, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '5'
                                upper_expression += '5'
                            else:
                                expression = '5'
                                upper_expression = '5'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 3, 4] and expression[0] in ['0', '1']:
                                expression += '5'
                                upper_expression += '5'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            elif len(expression) in [3, 4] and expression[0] == '2':
                                expression += '5'
                                upper_expression += '5'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 195 <= pos_mouse[0] <= 275 and 330 <= pos_mouse[1] <= 410:
                        """Клавиша 6 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(195, 330, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((195, 330, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '6'
                                upper_expression += '6'
                            else:
                                expression = '6'
                                upper_expression = '6'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 4] and expression[0] in ['0', '1']:
                                expression += '6'
                                upper_expression += '6'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            elif len(expression) == 4 and expression[0] == '2':
                                expression += '6'
                                upper_expression += '6'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 375 <= pos_mouse[0] <= 455 and 330 <= pos_mouse[1] <= 410:
                        """Возведение в степень """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(375, 330, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((375, 330, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if len(expression) != 0 and flag_calculation and flag_calculation_time:
                            upper_expression = upper_expression + ' ^ '
                            expression = '^'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                            expression = ''
                            flag_point = True
                            flag_input = True
                            flag_calculation = False
                            flag_degree = False
                            col_del = 0
                        elif not flag_calculation and not flag_degree and flag_calculation_time:
                            if upper_expression[-1] != ' ':
                                rez = result(screen, upper_expression, flag_point, flag_calculation_time)
                                upper_expression = rez + ' ^ '
                                expression = ''
                                flag_point = True
                                flag_input = True
                    elif 15 <= pos_mouse[0] <= 95 and 420 <= pos_mouse[1] <= 500:
                        """Клавиша 1 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(15, 420, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((15, 420, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '1'
                                upper_expression += '1'
                            else:
                                expression = '1'
                                upper_expression = '1'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [0, 1, 3, 4]:
                                expression += '1'
                                upper_expression += '1'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 105 <= pos_mouse[0] <= 185 and 420 <= pos_mouse[1] <= 500:
                        """Клавиша 2 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(105, 420, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((105, 420, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '2'
                                upper_expression += '2'
                            else:
                                expression = '2'
                                upper_expression = '2'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [0, 1, 3, 4]:
                                expression += '2'
                                upper_expression += '2'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 195 <= pos_mouse[0] <= 275 and 420 <= pos_mouse[1] <= 500:
                        """Клавиша 3 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(195, 420, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((195, 420, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if len(expression) < 14 and flag_input:
                                expression += '3'
                                upper_expression += '3'
                            else:
                                expression = '3'
                                upper_expression = '3'
                                flag_input = True
                            col_del = 0
                            col_minus = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [1, 3, 4]:
                                expression += '3'
                                upper_expression += '3'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 285 <= pos_mouse[0] <= 365 and 420 <= pos_mouse[1] <= 590:
                        """Клавиша равно = """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(285, 420, 80, 170))
                        pygame.mixer.music.play()
                        pygame.display.update((285, 420, 80, 170))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if flag_interest:
                                rez = result(screen, upper_expression, flag_point, flag_calculation_time)
                            elif not flag_interest:
                                rez = interest(screen, upper_expression, flag_point, flag_calculation_time)
                                flag_interest = True
                            upper_expression = rez
                            expression = rez
                        elif not flag_calculation_time:
                            cal_time(screen, upper_expression, flag_point, flag_calculation_time)
                            expression = ''
                            upper_expression = ''
                            col_sign = 0
                        if expression is None and upper_expression is None:
                            expression = ''
                            upper_expression = ''
                        flag_input = False
                        flag_calculation = True
                        flag_degree = True
                    elif 15 <= pos_mouse[0] <= 185 and 510 <= pos_mouse[1] <= 590:
                        """Клавиша 0 """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(15, 510, 170, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((15, 510, 170, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if (expression == '' and upper_expression == '') or not flag_input:
                                expression = '0'
                                upper_expression = '0'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                                upper_expression = ''
                                flag_input = True
                            elif expression == '' and len(upper_expression) > 1:
                                expression = '0'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                            elif len(expression) < 14 and flag_input:
                                expression += '0'
                                upper_expression += '0'
                                col_del = 0
                                col_minus = 0
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        elif not flag_calculation_time:
                            if len(expression) in [0, 1, 3, 4]:
                                expression += '0'
                                upper_expression += '0'
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 195 <= pos_mouse[0] <= 275 and 510 <= pos_mouse[1] <= 590:
                        """Клавиша точка"""
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(195, 510, 80, 80))
                        pygame.mixer.music.play()
                        pygame.display.update((195, 510, 80, 80))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        if flag_calculation_time:
                            if expression == '' and upper_expression == '' and flag_point:
                                expression = '0.'
                                upper_expression = '0.'
                                flag_point = False
                            elif expression == '' and len(upper_expression) > 1 and flag_point:
                                expression = '0.'
                                upper_expression = upper_expression + '0.'
                            elif len(expression) <= 11 and flag_point:
                                expression += '.'
                                flag_point = False
                                upper_expression += '.'
                            col_del = 0
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                    elif 375 <= pos_mouse[0] <= 455 and 420 <= pos_mouse[1] <= 590:
                        """Клавиша Del"""
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(375, 420, 80, 170))
                        pygame.mixer.music.play()
                        pygame.display.update((375, 420, 80, 170))
                        pygame.time.wait(300)
                        keyboard(screen)
                        pygame.display.update((15, 150, 445, 520))
                        flag_input = True
                        if len(expression) >= 2:
                            sign = expression[-1]
                        sign_1 = upper_expression
                        expression = expression[:-1]
                        upper_expression = upper_expression[:-1]
                        if len(expression) == 0:
                            expression = '0'
                            if len(upper_expression) == 0:
                                upper_expression = '0'
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                                upper_expression = ''
                            else:
                                if col_del == 0:
                                    col_del += 1
                                    upper_expression = sign_1[:-1]
                                else:
                                    upper_expression = sign_1
                                display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                                expression = ''
                        elif len(expression) >= 1 and sign == '.':
                            flag_point = True
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)
                        else:
                            display_output(screen, expression, upper_expression, flag_point, flag_calculation_time)


if __name__ == '__main__':
    work()
