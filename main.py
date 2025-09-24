from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep
app = QApplication([])

# Импортируем нужные библиотеки:
# - PyQt5 для создания графического интерфейса
# - choice, shuffle для работы со случайным выбором
# - sleep для задержки
# Создаем приложение (app), которое запускает интерфейс


from main_window import*
from menu_window import*

# Импортируем окна интерфейса: главное окно и меню


class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True
        self.count_ask = 0
        self.count_right = 0
        
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    
    def got_wrong(self):
        self.count_ask += 1

# Класс Question хранит:
# - сам вопрос и варианты ответов
# - флаг активности
# - количество заданных вопросов и правильных ответов
# В нем есть методы для учета правильного и неправильного ответа


q1 = Question('Яблуко', 'apple', 'apply', 'pineapple', 'application')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]

# Создаем несколько вопросов и собираем их в список questions


radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Список кнопок с вариантами ответов


def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_Question.setText(cur_q.question)
    lb_Corect.setText(cur_q.answer)
    
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.answer)
    radio_buttons[1].setText(cur_q.wrong_answer1)
    radio_buttons[2].setText(cur_q.wrong_answer2)
    radio_buttons[3].setText(cur_q.wrong_answer3)
    
    RadioGroup.setExclusive(False)
    for button in radio_buttons:
        button.setChecked(False)
    RadioGroup.setExclusive(True)

    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')

# Функция new_question:
# - выбирает случайный вопрос
# - ставит его текст в интерфейс
# - перемешивает кнопки и назначает ответы
# - сбрасывает выбор
# - показывает блок с вопросом и кнопку "Ответить"


def check():
    RadioGroup.setExclusive(False)
    for button in radio_buttons:
        if button.isChecked():
            if button.text() == lb_Corect.text():
                cur_q.got_right()
                lb_Result.setText('Вірно!')
            else:
                cur_q.got_wrong()
                lb_Result.setText('Невірно!')
        break
    
    RadioGroup.setExclusive(True)
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')

# Функция check:
# - проверяет, какая кнопка выбрана
# - если ответ правильный — записывает успех
# - если неправильный — фиксирует ошибку
# - показывает результат и меняет кнопку на "Следующий вопрос"


def click_ok():
    if btn_OK.text() == 'Відповісти':
        check()
    else:
        new_question()

# Функция click_ok:
# - если кнопка "Ответить" → запускает проверку
# - если кнопка "Следующий вопрос" → загружает новый вопрос


def rest():
    win_card.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    win_card.show()

# Функция rest:
# - скрывает окно с вопросами
# - ждет выбранное количество минут
# - возвращает окно обратно

def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right / cur_q.count_ask) * 100 
    text = f'Кількість відповідей: {cur_q.count_ask}\n'\
            f'Вірних відповідей: {cur_q.count_right}\n'\
            f'Успішність: {round(c, 2)} %'
    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()
    
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
    
btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())
    
    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)



    
def back_menu():
    menu_win.hide()
    win_card.show()

# Функции для переключения между меню и главным окном


btn_Menu.clicked.connect(menu_generation)
btn_back.clicked.connect(back_menu)
btn_Sleep.clicked.connect(rest)
btn_OK.clicked.connect(click_ok)

# Подключаем кнопки к соответствующим функциям


new_question()

# Загружаем первый вопрос при старте


app.exec_()

# Запускаем приложение