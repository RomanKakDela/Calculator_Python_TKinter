#простой калькулятор с TKinter, доделать клавишу 0

from tkinter import  *

window = Tk()
window.title('Калькулятор')
window.geometry('600x600+700+100')

def input_into_entry(symbol):
    entry.insert(END, symbol)

def cleare():
    entry.delete(0, END) #кнопка очистки

def count_result(): #кнопка подсчета итоговой суммы
    text = entry.get()
    result = 0
    if '+' in text:
        splitted_text = text.split('+')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first + second
        print(result)



    if '-' in text:
        splitted_text = text.split('-')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first - second
        print(result)

    if '*' in text:
            splitted_text = text.split('*')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first * second
            print(result)

    if '/' in text:
                splitted_text = text.split('/')
                first = float(splitted_text[0])
                second = float(splitted_text[1])
                result = first / second
                print(result)


    cleare()
    entry.insert(0, result)



entry = Entry(window, width=15, font=('',20))
entry.place(x = 100, y=50)

btn1 = Button(window, bg='black', fg='white',text='1', command=lambda: input_into_entry('1')) #цифра1
btn1.place(x = 100, y = 100, width=50, height=50)

btn2 = Button(window, bg='black', fg='white',text='2', command=lambda: input_into_entry('2')) #цифра2
btn2.place(x = 150, y = 100, width=50, height=50)

btn3 = Button(window, bg='black', fg='white',text='3', command=lambda: input_into_entry('3')) #цифра3
btn3.place(x = 200, y = 100, width=50, height=50)

btn4 = Button(window, bg='black', fg='white',text='4', command=lambda: input_into_entry('4')) #цифра4
btn4.place(x = 100, y = 150, width=50, height=50)

btn5 = Button(window, bg='black', fg='white',text='5', command=lambda: input_into_entry('5')) #цифра5
btn5.place(x = 150, y = 150, width=50, height=50)

btn6 = Button(window, bg='black', fg='white',text='6', command=lambda: input_into_entry('6')) #цифра6
btn6.place(x = 200, y = 150, width=50, height=50)

btn7 = Button(window, bg='black', fg='white',text='7', command=lambda: input_into_entry('7')) #цифра7
btn7.place(x = 100, y = 200, width=50, height=50)

btn8 = Button(window, bg='black', fg='white',text='8', command=lambda: input_into_entry('8') ) #цифра8
btn8.place(x = 150, y = 200, width=50, height=50)

btn9 = Button(window, bg='black', fg='white',text='9', command=lambda: input_into_entry('9')) #цифра9
btn9.place(x = 200, y = 200, width=50, height=50)

btn_plus = Button(window, bg='black', fg='white',text='+', command=lambda: input_into_entry('+')) #сложение
btn_plus.place(x = 250, y = 100, width=50, height=50)

btn_minus = Button(window, bg='black', fg='white',text='-', command=lambda: input_into_entry('-')) #вычитание
btn_minus.place(x = 250, y = 150, width=50, height=50)

btn_myltiply = Button(window, bg='black', fg='white',text='*', command=lambda: input_into_entry('*')) #умножение
btn_myltiply.place(x = 250, y = 250, width=50, height=50)

btn_divide = Button(window, bg='black', fg='white',text='/', command=lambda: input_into_entry('/')) #деление
btn_divide.place(x = 250, y = 200, width=50, height=50)

btn_result = Button(window, bg='black', fg='white',text='=', command=count_result ) #результат
btn_result.place(x = 200, y = 250, width=50, height=50)

btn_clear = Button(window, bg='black', fg='white',text='CE', command=cleare) #кнопка очистки
btn_clear.place(x = 150, y = 250, width=50, height=50)

btn_dot = Button(window, bg='black', fg='white',text='.', command=lambda: input_into_entry('.')) #добавление точки
btn_dot.place(x = 100, y = 250, width=50, height=50)






window.mainloop()