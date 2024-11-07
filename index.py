#Caluladora basica
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry("300x200")
def menu():
#MENU DE LA CALCULADORA
    signo1 = tk.Label(root, text='='*10)
    title = tk.Label(root, text="CALCULADORA BASICA")
    signo2 = tk.Label(root, text='='*10)
    plus_label = tk.Label(root, text="1- SUMA")
    rest_label = tk.Label(root, text="2- RESTA")
    mult_label = tk.Label(root, text="3- MULTIPLICACION")
    divi_label = tk.Label(root, text="4- DIVISION")
    

    signo1.pack()
    title.pack()
    signo2.pack()
    plus_label.pack()
    rest_label.pack()
    mult_label.pack()
    divi_label.pack()


#Proceso usan1do bucle if para opciones
def entrada():
    op = int(entry_op.get())
    return op

def abrir_ventana_operacion(op):
    # Crea una nueva ventana
    operacion_window = tk.Toplevel(root)
    operacion_window.title("Realizar Operación")

    # Etiquetas y entradas para los números
    tk.Label(operacion_window, text="Ingrese el primer número:").pack()
    entry_n1 = tk.Entry(operacion_window)
    entry_n1.pack()

    tk.Label(operacion_window, text="Ingrese el segundo número:").pack()
    entry_n2 = tk.Entry(operacion_window)
    entry_n2.pack()

    def calcular():
        n1 = int(entry_n1.get())
        n2 = int(entry_n2.get())
        resultado = None

        if op == 1:
            resultado = n1 + n2
            operacion = "Suma"
        elif op == 2:
            resultado = n1 - n2
            operacion = "Resta"
        elif op == 3:
            resultado = n1 * n2
            operacion = "Multiplicación"
        elif op == 4:
            if n2 != 0:
                resultado = n1 / n2
                operacion = "División"
            else:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return

        messagebox.showinfo("Resultado", f"El resultado de la {operacion} es: {resultado}")

    # Botón para calcular
    btn_calcular = tk.Button(operacion_window, text="Calcular", command=calcular)
    btn_calcular.pack()

def Resultado():  
    op = entrada()
    if op in [1, 2, 3, 4]:
        abrir_ventana_operacion(op)
    else:
        messagebox.showerror("Error", "Opción no válida. Por favor, elija una opción entre 1 y 4.")


entry_op = tk.Entry(root)
entry_op.pack()

boton = tk.Button(root, text="Obtener resultado", command=Resultado)
boton.pack()



menu()
root.mainloop()
