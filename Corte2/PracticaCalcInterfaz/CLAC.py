import tkinter as tk

def click_boton(valor):
    entrada_actual = entrada.get()
    entrada.set(entrada_actual + str(valor))

def borrar():
    entrada.set("")

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except:
        entrada.set("Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Campo de entrada
entrada = tk.StringVar()
campo_entrada = tk.Entry(ventana, textvariable=entrada, font=("Arial", 24), bd=10, relief="sunken", justify="right")
campo_entrada.pack(fill="both", padx=10, pady=10)

# Crear botones
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

marco_botones = tk.Frame(ventana)
marco_botones.pack()

for fila in botones:
    fila_frame = tk.Frame(marco_botones)
    fila_frame.pack(expand=True, fill="both")
    for btn in fila:
        if btn == '=':
            b = tk.Button(fila_frame, text=btn, font=("Arial", 18), command=calcular)
        else:
            b = tk.Button(fila_frame, text=btn, font=("Arial", 18), command=lambda x=btn: click_boton(x))
        b.pack(side="left", expand=True, fill="both")

# Botón de borrar
boton_borrar = tk.Button(ventana, text="C", font=("Arial", 18), bg="red", fg="white", command=borrar)
boton_borrar.pack(fill="both", padx=10, pady=5)

# Ejecutar interfaz
ventana.mainloop()