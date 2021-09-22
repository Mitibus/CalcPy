import tkinter as tk

window = tk.Tk()
window.title('Calculatrice')
window.geometry('325x440')
window.configure(bg='#1f1f1f')
window.resizable(width=False, height=False)

a = ""
result = 0
operators = []
numbers = []


def AddNumber(nb):
    global a
    a += str(nb)
    resultLabel['text'] = a


menu = tk.Label(window, text='Standard', font=(
    'Arial', 15), bg='#1f1f1f', fg='#fff')
menu.grid(row=0, column=0, padx=40, pady=15, columnspan=2)

resultLabel = tk.Label(window, text="0", font=(
    'Arial', 35), fg='#fff', bg='#1f1f1f', justify="right")
resultLabel.grid(row=1, column=0, columnspan=5, padx=30, pady=16)

ButtonWidth = 10
ButtonHeight = 3


def clear():
    global a, result, operators, numbers, resultLabel
    a = ""
    result = 0
    operators = []
    numbers = []
    resultLabel['text'] = ""


def clearLast():
    global a, result, operators, numbers, resultLabel
    a = ""
    resultLabel['text'] = ""


def equal():
    global numbers, operators, result, a
    numbers.append(a)
    i = 0
    # [20, 34, 44 34]
    # ["+", "*", "+"]
    print(numbers)
    print(operators)
    for nb in numbers:
        nb = float(nb)
        if i == 0:
            result += nb
            i += 1
        else:
            if operators[i-1] == "+":
                result += nb
                i += 1
            elif operators[i-1] == "-":
                result -= nb
                i += 1
            elif operators[i-1] == '*':
                result = result * nb
                i += 1
            elif operators[i-1] == '/':
                result = result / nb
                i += 1
    resultLabel['text'] = round(result, 3)
    a = ''


def backSpace():
    global a, resultLabel
    a = a[0:len(a)-1]
    resultLabel['text'] = a


def dot():
    global a, resultLabel, operators
    a += "."
    resultLabel['text'] = a


def changeSign():
    global a, numbers, operators
    if float(a) > 0:
        a = '-' + a
        resultLabel['text'] = a
    else:
        a = a[1:]
        resultLabel['text'] = a


def plus():
    global a, numbers, operators
    numbers.append(a)
    operators.append("+")
    resultLabel['text'] = '+'
    a = ''


def minus():
    global a, numbers, operators
    numbers.append(a)
    operators.append("-")
    resultLabel['text'] = '-'
    a = ''


def divide():
    global a, numbers, operators
    numbers.append(a)
    operators.append("/")
    resultLabel['text'] = '/'
    a = ''


def multiply():
    global a, numbers, operators
    numbers.append(a)
    operators.append("*")
    resultLabel['text'] = '*'
    a = ''


def put7():
    AddNumber(7)


def put8():
    AddNumber(8)


def put9():
    AddNumber(9)


def put4():
    AddNumber(4)


def put5():
    AddNumber(5)


def put6():
    AddNumber(6)


def put1():
    AddNumber(1)


def put2():
    AddNumber(2)


def put3():
    AddNumber(3)


def put0():
    AddNumber(0)


buttonCE = tk.Button(window, text="CE", width=ButtonWidth, bg="#060606", fg="#fff", command=clearLast,
                     height=ButtonHeight).grid(row=2, column=0)

buttonC = tk.Button(window, text="C",  width=ButtonWidth, bg="#060606", fg="#fff", command=clear,
                    height=ButtonHeight).grid(row=2, column=1)

button9 = tk.Button(window, text="<-", width=ButtonWidth, bg="#060606", fg="#fff", command=backSpace,
                    height=ButtonHeight).grid(row=2, column=2)
buttonD = tk.Button(window, text="/", width=ButtonWidth, bg="#060606", fg="#fff", command=divide,
                    height=ButtonHeight).grid(row=2, column=3)


button7 = tk.Button(window, text="7", command=put7, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=3, column=0)

button8 = tk.Button(window, text="8", command=put8,  width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=3, column=1)

button9 = tk.Button(window, text="9", command=put9, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=3, column=2)
buttonX = tk.Button(window, text="x", width=ButtonWidth, bg="#060606", fg="#fff", command=multiply,
                    height=ButtonHeight).grid(row=3, column=3)

button4 = tk.Button(window, text="4", command=put4, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=4, column=0)
button5 = tk.Button(window, text="5", command=put5, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=4, column=1)
button6 = tk.Button(window, text="6", command=put6, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=4, column=2)
buttonM = tk.Button(window, text="-", width=ButtonWidth, bg="#060606", fg="#fff", command=minus,
                    height=ButtonHeight).grid(row=4, column=3)

button1 = tk.Button(window, text="1", command=put1, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=5, column=0)
button2 = tk.Button(window, text="2", command=put2, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=5, column=1)
button3 = tk.Button(window, text="3", command=put3, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=5, column=2)
buttonP = tk.Button(window, text="+", width=ButtonWidth, bg="#060606", fg="#fff", command=plus,
                    height=ButtonHeight).grid(row=5, column=3)

buttonS = tk.Button(window, text="+/-", width=ButtonWidth, bg="#060606", fg="#fff", command=changeSign,
                    height=ButtonHeight).grid(row=6, column=0)
button0 = tk.Button(window, text="0", command=put0, width=ButtonWidth, bg="#060606", fg="#fff",
                    height=ButtonHeight).grid(row=6, column=1)
buttonV = tk.Button(window, text=",", width=ButtonWidth, bg="#060606", fg="#fff", command=dot,
                    height=ButtonHeight).grid(row=6, column=2)
buttonE = tk.Button(window, text="=", width=ButtonWidth, bg="#060606", fg="#fff", command=equal,
                    height=ButtonHeight).grid(row=6, column=3)

window.mainloop()
