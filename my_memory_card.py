#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QVBoxLayout, QButtonGroup
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
text = QLabel("Какой национальности не существует?")

button1 = QRadioButton("Энцы")
button2 = QRadioButton("Чулымцы")
button3 = QRadioButton("Смурфы")
button4 = QRadioButton("Алеуты")

button5 = QPushButton("Ответить")

RadioGroupBox = QGroupBox("Варианты ответов")

layout_main = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()
layout15 = QHBoxLayout()
layout16 = QHBoxLayout()
layout17 = QHBoxLayout()

layout4.addWidget(text, alignment = Qt.AlignCenter)
layout2.addWidget(button1, alignment = Qt.AlignCenter)
layout2.addWidget(button2, alignment = Qt.AlignCenter)

layout3.addWidget(button3, alignment = Qt.AlignCenter)
layout3.addWidget(button4, alignment = Qt.AlignCenter)

layout6.addWidget(button5, alignment = Qt.AlignCenter)

layout1.addLayout(layout2)
layout1.addLayout(layout3)


RadioGroupBox.setLayout(layout1)

layout5.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)


layout_main.addLayout(layout4)
layout_main.addLayout(layout5)
layout_main.addLayout(layout6)



AnsGroupBox = QGroupBox("результат теста")
#text2 = QLabel("Самый сложный вопрос в мире!")
text3 = QLabel("Правильно/Неправильно")
text4 = QLabel("Правильный ответ")
layout7 = QVBoxLayout()

#layout15.addWidget(text2, alignment= Qt.AlignCenter)
layout16.addWidget(text3, alignment= Qt.AlignLeft)
layout17.addWidget(text4, alignment= Qt.AlignCenter)
layout7.addLayout(layout15)
layout7.addLayout(layout16)
layout7.addLayout(layout17)
AnsGroupBox.setLayout(layout7)
AnsGroupBox.hide()
layout5.addWidget(AnsGroupBox, alignment = Qt.AlignCenter)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button5.setText("Следующий вопрос")

QRadio = QButtonGroup()
QRadio.addButton(button1)
QRadio.addButton(button2)
QRadio.addButton(button3)
QRadio.addButton(button4)

def show_question():
    
    QRadio.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button5.setText("Ответить")

def start_test():
    if button5.text() == "Ответить":
        show_result()
    else:
        show_question()

answers = [button1, button2, button3, button4]


def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1) 
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    text4.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        text3.setText("Правильно!")
        main_win.score += 1
        show_result()
        print("Правильных ответов: ",main_win.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            text3.setText("Неправильно!")
            show_result()


def next_question():
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    main_win.total += 1
    print("Всего ответов: ",main_win.total)
    print("Рейтинг: ", main_win.score / main_win.total * 100)

def click_ok():
    if button5.text() == "Ответить":
        check_answer()
    else:
        next_question()

question_list = []

q1 = Question("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", "Итальянский")
q2 = Question("Какой национальности не существует?","Смурфы", "Энцы", "Чулымцы", "Алеуты")
q3 = Question("Как называется треугольник, у которого две стороны равны?", "равнобедренный", "равновеликий", "равноправный", "равнодушный")
q4 = Question("Что из перечисленного не является сортом груши?", "ренклод", "дюшес", "бергамот", "бере")
q5 = Question("От кого Суворов освободил Италию?", "Французов", "Австрийцев", "Испанцев", "Германцев")
q6 = Question("Какое из этих животных родом не из Австралии?", "Панда", "Динго", "утконос", "коала")
q7 = Question("К какому государству принадлежит крупнейший в мире остров Гренландия?", "Дания", "Норвегия", "Великобритания", "Швеция")
q8 = Question("Как по-другому называют койота?", "луговой волк", "тропичский волк", "лесной волк", "пустынный волк")
q9 = Question("В каком месте Земного шара сила тяжести больше?", "на полюсах", "на экваторе", "в средних широтах", "везде одинаковая")
q10 = Question("Какое из перечисленных государств возглавляет королева Великобритании?", "Ямайка", "Малайзия", "Коста-рика", "Шри-Ланка")

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)

main_win.total = 0
main_win.score = 0

button5.clicked.connect(click_ok)
check_answer()

main_win.setLayout(layout_main)
main_win.show()
app.exec_()