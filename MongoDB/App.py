from AnalizadorLexico import AnalizadorLexico
import os
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import sys

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.archivo = None
        master.title("Analizador Léxico")
        self.analizador = AnalizadorLexico()

        # Crear el menú lateral
        self.menu = tk.Frame(master, bg="gray")
        self.menu.pack(side="left", fill="y", expand=True)

        self.btn1 = tk.Button(self.menu, text="nuevo", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.cargar_archivo, width=10)
        self.btn1.pack(pady=10)

        self.btn2 = tk.Button(self.menu, text="abrir archivo", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.abrir_archivo, width=10)
        self.btn2.pack(pady=10)

        self.btn3 = tk.Button(self.menu, text="Analizar", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.lexicosintactico, width=10)
        self.btn3.pack(pady=10)

        self.btn4 = tk.Button(self.menu, text="Ver tokens", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.mostrartokens, width=10)
        self.btn4.pack(pady=10)

        self.btn5 = tk.Button(self.menu, text="Ver errores", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.mostrarerrores, width=10)
        self.btn5.pack(pady=10)

        self.btn6 = tk.Button(self.menu, text="Guardar", font=('Roboto', 12), background='#4CAF50', foreground='white', width=10)
        self.btn6.pack(pady=10)

        self.btn7 = tk.Button(self.menu, text="Guardar Como", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.guardar_como, width=10)
        self.btn7.pack(pady=10)

        self.btn8 = tk.Button(self.menu, text="Limpiar", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.limpiar_text_areas, width=10)
        self.btn8.pack(pady=10)

        self.btn9 = tk.Button(self.menu, text="Salir", font=('Roboto', 12), background='#4CAF50', foreground='white', command=self.salir, width=10)
        self.btn9.pack(pady=10)

        # Crear las áreas de texto
        self.text1 = tk.Text(master, bg="white", fg="black", font=("Courier", 10), wrap="word")
        self.text1.pack(side="left", fill="both", expand=True, padx=10, pady=10, anchor="nw")
        self.text1.bind("<KeyRelease>", self.autoresize)

        self.text2 = tk.Text(master, bg="white", fg="black", font=("Courier", 10), height=10)
        self.text2.pack(side="left", fill="both", expand=True, padx=10, pady=10, anchor="nw")
        self.text2.bind("<KeyRelease>", self.autoresize)

    def autoresize(self):
        # Ajustar el ancho del TextArea
        self.text1.configure(width=1)
        self.text1.configure(width=self.text1.winfo_reqwidth() // self.text1['font'].measure('0'))

        # Ajustar la altura del TextArea
        num_lines = int(self.text1.index('end-1c').split('.')[0])
        self.text1.configure(height=num_lines)
        self.text1.yview_moveto(1.0)

    def limpiar_text_areas(self):
        # Limpiar el contenido de los TextArea
        self.text1.delete("1.0", "end")
        self.text2.delete("1.0", "end")

    def abrir_archivo(self):
        x = ""
        try:
            filename = askopenfilename(title='seleccionar archivo', filetypes=[('Archivos', '*.txt')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                print(x)
                self.entrada = x
                self.text1.insert(tk.END, self.entrada)
                self.archivo = filename # Guardar la ubicación del archivo en la variable de instancia
        except:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
            return 

    def mostrartokens(self): 
        if self.archivo is not None: # Verificar que se ha seleccionado un archivo
            lexico = AnalizadorLexico()
            with open(self.archivo, encoding='utf-8') as infile: # Abrir el archivo
                entrada = infile.read()
                if not entrada: # Check if input is empty
                    tk.messagebox.showerror("Error", "El archivo está vacío")
                    return
                lexico.analizar(entrada) # Analizar el contenido del archivo
                # Obtener la tabla de tokens en formato de cadena
                tokens_table_str = lexico.verTokens()
                # Insertar la cadena de la tabla en el widget Text
                self.text2.insert(tk.END, tokens_table_str)
                # Ajustar el tamaño del widget Text en función del número de líneas de texto
                num_lines = self.text2.get('1.0', 'end').count('\n') + 1
                self.text2.configure(height=num_lines)
        else:
            tk.messagebox.showerror("Error", "No se ha seleccionado un archivo para analizar")

    def mostrarerrores(self): 
        if self.archivo is not None: # Verificar que se ha seleccionado un archivo
            lexico = AnalizadorLexico()
            with open(self.archivo, encoding='utf-8') as infile: # Abrir el archivo
                entrada = infile.read()
                if not entrada: # Check if input is empty
                    tk.messagebox.showerror("Error", "El archivo está vacío")
                    return
                lexico.analizar(entrada) # Analizar el contenido del archivo
                # Obtener la tabla de tokens en formato de cadena
                errores_table_str = lexico.verErrores()
                self.text2.insert(tk.END, errores_table_str) 
                # Ajustar el tamaño del widget Text en función del número de líneas de texto
                num_lines = self.text2.get('1.0', 'end').count('\n') + 1
                self.text2.configure(height=num_lines)
        else:
            tk.messagebox.showerror("Error", "No se ha seleccionado un archivo para analizar")

                              
    def guardar_auto(self):
        # Obtener el contenido del área de texto
        texto = self.text1.get("1.0", "end-1c")

        # Definir la ubicación y el nombre del archivo
        filename = os.path.join(os.getcwd(), "202112012.txt")

        # Guardar el contenido del área de texto en el archivo
        with open(filename, "w") as f:
            f.write(texto)

    def guardar_como(self):
        # Obtener el contenido del área de texto
        texto = self.text1.get("1.0", "end-1c")

        # Pedir al usuario la ubicación y el nombre del archivo
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

        # Guardar el contenido del área de texto en el archivo
        if filename:
            with open(filename, "w") as f:
                f.write(texto)

    def lexicosintactico(self):
        pass

    def guardar_texto(self):
        # Obtener el contenido del área de texto
        texto = self.text1.get("1.0", "end-1c")

        # Si hay texto, preguntar al usuario si desea guardarlo
        if texto:
            respuesta = messagebox.askyesno("Guardar texto", "¿Desea guardar el texto en un archivo de texto?")
            if respuesta:
                # Abrir un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo
                filename = filedialog.asksaveasfilename(defaultextension=".txt")
                if filename:
                    # Guardar el contenido del área de texto en el archivo
                    with open(filename, "w") as f:
                        f.write(texto)

        # Limpiar el área de texto
        self.text1.delete("1.0", "end")    

    def cargar_archivo(self):
        if self.text1.get('1.0', tk.END).strip() == '':
            return
        if self.archivo is not None and self.text1.edit_modified():
            guardar = messagebox.askyesno("Guardar Cambios", "¿Desea guardar los cambios?")
            if guardar:
                self.guardar()
        self.text1.delete('1.0', tk.END)
        self.archivo = None
        self.text1.edit_modified(False)

    def salir(self):
        respuesta = messagebox.askyesno("Salir", "¿Estás seguro que quieres salir del programa?")
        if respuesta == 1:
            messagebox.showinfo("Adiós", "¡Gracias por usar el programa!")
            sys.exit()

root = tk.Tk()
ventana_principal = VentanaPrincipal(root)
root.mainloop()