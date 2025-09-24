from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

menu_win = QWidget()
menu_win.resize(550, 450)

# Создаем окно "menu_win" размером 550х450 пикселей


lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть правильну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь:')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь:')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь:')

# Метки (подсказки для ввода):
# - текст вопроса
# - правильный ответ
# - три неправильных ответа


le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

# Поля ввода:
# - для вопроса
# - для правильного ответа
# - для трех неправильных ответов


lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('font-size: 19px; font_weight: bold;')

lb_statistic = QLabel('')

# Заголовок и место для статистики:
# - надпись "Статистика" (увеличенным шрифтом)
# - пустая метка для вывода данных статистики


btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

# Кнопки:
# - "Назад"
# - "Добавить вопрос"
# - "Очистить"


vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

# Вертикальный контейнер для всех меток (подсказок).
# Создает левую колонку с текстами: вопрос и варианты ответов.


vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

# Вертикальный контейнер для полей ввода.
# Формирует правую колонку, где пользователь будет вводить текст для вопроса и ответов.


hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

# Горизонтальный контейнер объединяет две колонки.
# Слева метки, справа поля ввода, создавая строку формы для ввода вопроса.


hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

# Горизонтальный блок для кнопок под формой.
# Кнопки стоят в одной линии: "Добавить вопрос" и "Очистить".


vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_back)

# Главный вертикальный контейнер, который собирает все элементы окна:
# - верхняя часть: форма вопроса (hl_question)
# - средняя: кнопки (hl_buttons)
# - нижняя: статистика и кнопка "Назад"


menu_win.setLayout(vl_res)

# Применяем главный контейнер к окну menu_win.
# Все виджеты теперь отображаются в указанной структуре.