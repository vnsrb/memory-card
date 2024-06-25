from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # todas las líneas deben ser dadas durante la creación del objeto y serán registradas como propiedades
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = [] 
questions_list.append(Question('El idioma nacional de Brasil', 'Portugués', 'Brasilero', 'Español', 'Italiano'))
questions_list.append(Question('¿Qué color no aparece en la bandera de Estados Unidos?', 'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(Question('Una residencia tradicional de los yakutos', 'Urasa', 'Yurta', 'Iglú', 'Choza'))
questions_list.append(Question('Cual es la marca de telefono mas vendida en el mundo?', 'Samsung', 'Apple', 'Xiaomi', 'Oppo'))
questions_list.append(Question('En que año se fundo el Imperio Romano?', '27 a. C.', '32 a. C.', '17 a. C.', '24 a. C.'))
app = QApplication([])


btn_OK = QPushButton('Responder') # botón de responder
lb_Question = QLabel('¡La pregunta más difícil del mundo!') # texto de pregunta


RadioGroupBox = QGroupBox("Opciones de respuesta") # grupo en pantalla para los botones de radio con respuestas


rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


RadioGroup = QButtonGroup() # este agrupa los botones de radio para poder controlar su comportamiento
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # las verticales estarán dentro de la horizontal 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # dos respuestas en la primera columna
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # dos respuestas en la segunda columna
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # colocar las columnas en la misma línea


RadioGroupBox.setLayout(layout_ans1) # un “panel” está listo con las opciones de respuesta 


AnsGroupBox = QGroupBox("Resultado de prueba")
lb_Result = QLabel('¿Es correcto o no?') # la palabra “correcto” o “incorrecto” estará escrita aquí
lb_Correct = QLabel('¡Aquí estará la respuesta!') # el texto de la respuesta correcta estará aquí


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() # pregunta
layout_line2 = QHBoxLayout() # opciones de respuesta o resultado de prueba
layout_line3 = QHBoxLayout() # botón “Responder”


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # esconde el panel de respuesta porque el panel de preguntas debe ser visible primero 


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # el botón debe ser grande
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # espacios entre los contenidos


def show_result():
    ''' Mostrar el panel de respuesta. '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Siguiente pregunta')


def show_question():
    ''' Mostrar el panel de pregunta. '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Responder')
    # limpia el botón de radio seleccionado
    RadioGroup.setExclusive(False) # remueve los límites para poder reiniciar los botones de radio 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # reinicia los límites para que solo un botón de radio pueda ser seleccionado a la vez 


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' Esta función escribe el valor de la pregunta y respuestas en los widgets correspondientes. Las opciones de respuesta son distribuidas aleatoriamente. '''
    shuffle(answers) # baraja la lista de botones; ahora un botón aleatorio es el primero en la lista
    answers[0].setText(q.right_answer) # llena el primer elemento de la lista con la respuesta correcta y los otros elementos con respuestas incorrectas
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # pregunta
    lb_Correct.setText(q.right_answer) # respuesta
    show_question() # muestra panel de pregunta 


def show_correct(res):
    ''' Mostrar el resultado – colocar el texto que fue pasado a esta función en la etiqueta de “resultado” y mostrar el panel relevante. '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' Si una de las opciones de respuesta es seleccionada, comprobarla y mostrar el panel de respuesta. '''
    if answers[0].isChecked():
        # ¡una respuesta correcta!
        show_correct('¡Correcto!')
        window.score += 1
        print('Estadisticas\n-Preguntas Totales:', window.total, '\n-Preguntas Correctas: ', window.score)
        print('Calificacion: ', (window.score /window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # ¡una respuesta incorrecta!
            show_correct('¡Incorrecto!')


def next_question():
    ''' Realiza la siguiente pregunta en la lista. '''
    window.total += 1 
    print('Estadisticas\n-Preguntas Totales:', window.total, '\n-Preguntas Correctas: ', window.score)
    # esta función necesita una variable que dé el número de la pregunta actual 
    # esta variable puede hacerse global o puede ser la propiedad de un “objeto global” (app o ventana)
    # crearemos la propiedad window.cur_question (la siguiente)
    window.cur_question = window.cur_question + 1 # pasa a la siguiente pregunta 
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # si la lista de preguntas ha terminado, se vuelve a comenzar 
    q = questions_list[window.cur_question] # toma una pregunta
    ask(q) # pregunta


def click_OK():
    ''' Esto determina si se muestra otra pregunta o se comprueba la respuesta a esta pregunta. '''
    if btn_OK.text() == 'Responder':
        check_answer() # comprueba la respuesta
    else:
        next_question() # siguiente pregunta


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')
# Hace la pregunta actual de la lista, una propiedad del objeto “ventana”. De esa forma, podemos cambiar fácilmente sus funciones:
window.cur_question = -1    # idealmente, las variables como esta deberían ser propiedades 
                            # tendríamos que escribir una clase cuyas instancias tengan estas propiedades,
                            # pero Python nos permite crear una propiedad para una sola instancia 


btn_OK.clicked.connect(click_OK) # cuando se hace clic en un botón, escogemos exactamente lo que sucede 

window.score = 0
window.total = 0

# Todo está preparado. Ahora hacemos la pregunta y mostramos la ventana:
next_question()
window.resize(400, 300)
window.show()
app.exec()
