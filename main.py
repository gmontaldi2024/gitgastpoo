import customtkinter as ctk

class CalculadoraImpuestos:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("IMP%")
        self.ventana.geometry('350*250')
        self.ventana.resizable(width=False, height=False)
        self.ventana.config(bg='black')
        self.padding: dict = {'padx': 20 , 'pady': 10}
        self.font = ("Arial", 12)
        #ingreso de impuesto
        self.impuesto = ctk.CTkLabel(self.ventana, text='Impuesto', font= self.font)
        self.impuesto.grid(row=0, column=0, **self.padding)
        self.impuesto = ctk.CTkEntry(self.ventana, font=self.font)
        self.impuesto.grid(row=0, column=1, **self.padding)
        #ingreso de porcentaje
        self.porcentaje = ctk.CTkLabel(self.ventana, text='Porcentaje', font= self.font)
        self.porcentaje.grid(row=1, column=0, **self.padding)
        self.porcentaje = ctk.CTkEntry(self.ventana, font=self.font)
        self.porcentaje.grid(row=1, column=1, **self.padding)
        #resultado final
        self.resultado = ctk.CTkLabel(self.ventana, text='Resultado', font= self.font)
        self.resultado.grid(row=2, column=0, **self.padding)
        self.resultado = ctk.CTkEntry(self.ventana, font=self.font)
        self.resultado.insert(index=0, string='0')
        self.resultado.grid(row=2, column=1, **self.padding)
        #calcular porcentaje
        self.calcular = ctk.CTkButton(self.ventana, text='Calcular' , font=self.font, command=self.calculo_imp)
        self.calcular.grid(row=3, column=1, **self.padding)
    
    def resultado_final(self, text):
        self.resultado.insert(0, text)
    
    def calculo_imp(self):
        self.resultado.delete(0, "end")
        try:
            ingreso: float = float(self.impuesto.get())
            porcentaje: float = float(self.porcentaje.get())
            self.resultado_final(f"${ingreso*(porcentaje/100)}")
        except ValueError:
            self.resultado_final("Calculo invalido")
    
    def ejecutar(self):
        "Ejecuta TKInter."
        self.ventana.mainloop()

calculadora = CalculadoraImpuestos()
calculadora.ejecutar()