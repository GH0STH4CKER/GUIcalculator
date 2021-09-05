from tkinter import *

expression = ""
def display_zero() :
    equation.set("0")

# Update expression
def press(num):

    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression 
    equation.set(expression)


# Function to evaluate the expression
def equalpress():

    try:

        global expression

        # eval function evaluate the expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""

    # If error occured 
    except:

        equation.set("ERROR")
        expression = ""


# Function to clear the contents
def clear():
    global expression
    expression = ""
    equation.set("0")


if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # Background color of GUI window
    gui.configure(background="white")

    # Title of GUI window
    gui.title("Basic Calclator")

    # Size of GUI window
    gui.geometry("395x550")

    equation = StringVar()
    display_zero()
    
    expression_field = Label(gui,width=10,textvariable=equation,font=("ds-digital",35),bg='#dce6e2',fg='black',anchor='e')

    expression_field.grid(columnspan=4, ipadx=80, ipady=10)

    # Defining buttons in calculator
    button1 = Button(gui,font=("calibri",20), text=' 1 ', fg='black', bg='#7af5c8',
                    command=lambda: press(1),height=2,width=6)

    button1.grid(row=2, column=0,padx=2,pady=2)


    button2 = Button(gui,font=("calibri",20), text=' 2 ', fg='black', bg='#7af5c8',
                    command=lambda: press(2), height=2, width=6)
    button2.grid(row=2, column=1,padx=2)

    button3 = Button(gui,font=("calibri",20), text=' 3 ', fg='black', bg='#7af5c8',
                    command=lambda: press(3), height=2, width=6)
    button3.grid(row=2, column=2,padx=2)

    button4 = Button(gui,font=("calibri",20), text=' 4 ', fg='black', bg='#7af5c8',
                    command=lambda: press(4), height=2, width=6)
    button4.grid(row=3, column=0,pady=2)

    button5 = Button(gui,font=("calibri",20), text=' 5 ', fg='black', bg='#7af5c8',
                    command=lambda: press(5), height=2, width=6)
    button5.grid(row=3, column=1)

    button6 = Button(gui,font=("calibri",20), text=' 6 ', fg='black', bg='#7af5c8',
                    command=lambda: press(6), height=2, width=6)
    button6.grid(row=3, column=2)

    button7 = Button(gui,font=("calibri",20), text=' 7 ', fg='black', bg='#7af5c8',
                    command=lambda: press(7), height=2, width=6)
    button7.grid(row=4, column=0,pady=2)

    button8 = Button(gui,font=("calibri",20), text=' 8 ', fg='black', bg='#7af5c8',
                    command=lambda: press(8), height=2, width=6)
    button8.grid(row=4, column=1)

    button9 = Button(gui,font=("calibri",20), text=' 9 ', fg='black', bg='#7af5c8',
                    command=lambda: press(9), height=2, width=6)
    button9.grid(row=4, column=2)

    button0 = Button(gui,font=("calibri", 20), text=' 0 ', fg='black', bg='#7af5c8',
                    command=lambda: press(0), height=2, width=6)
    button0.grid(row=5, column=0,pady=2)

    plus = Button(gui,font=("calibri",20), text=' + ', fg='black', bg='#7af5c8',
                command=lambda: press("+"), height=2, width=6)
    plus.grid(row=2, column=3,padx=2)

    minus = Button(gui,font=("calibri",20), text=' − ', fg='black', bg='#7af5c8',
                command=lambda: press("-"), height=2, width=6)
    minus.grid(row=3, column=3)

    multiply = Button(gui,font=("calibri",20), text=' × ', fg='black', bg='#7af5c8',
                    command=lambda: press("*"), height=2, width=6)
    multiply.grid(row=4, column=3)

    divide = Button(gui,font=("calibri",20), text=' ÷ ', fg='black', bg='#7af5c8',
                    command=lambda: press("/"), height=2, width=6)
    divide.grid(row=5, column=3)

    equal = Button(gui,font=("calibri",20), text=' = ', fg='black', bg='#7af5c8',
                command=equalpress, height=2, width=6)
    equal.grid(row=5, column=2)

    clear = Button(gui,font=("calibri",20), text='Clear', fg='black', bg='#7af5c8',
                command=clear, height=2, width=6)
    clear.grid(row=6, column=0,pady=2)

    Decimal= Button(gui,font=("calibri",20), text='.', fg='black', bg='#7af5c8',
                    command=lambda: press('.'), height=2, width=6)
    Decimal.grid(row=5, column=1)

    gui.mainloop()
