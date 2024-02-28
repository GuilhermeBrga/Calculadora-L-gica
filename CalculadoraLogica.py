#-Imports----------------------------------------------------------------------------------------------------------------------

import customtkinter
import tkinter as tk
import ttg

#-Configurações da tela---------------------------------------------------------------------------------------------------------

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
tela_calculadora = customtkinter.CTk()
tela_calculadora.geometry("1000x700")
tela_calculadora.title("Calculadora Lógica")

#-Configurações de linhas e colunas---------------------------------------------------------------------------------------------


tela_calculadora.columnconfigure(0, weight = 1)
tela_calculadora.rowconfigure(0, weight = 0)

#-Texto da Equação--------------------------------------------------------------------------------------------------------------


equacao = customtkinter.CTkLabel(tela_calculadora, text = " ")
equacao.grid(padx = 10, pady = 10)


#-Funções------------------------------------------------------------------------------------------------------------------------


def c1():
    equacao.configure(text = str(equacao._text) + "A")

def c2():
    equacao.configure(text = str(equacao._text) + "B")

def c3():
    equacao.configure(text = str(equacao._text) + "C")

def c4():
    equacao.configure(text = str(equacao._text) + "D")

def apagar():
    texto_atual = equacao.cget("text")
    novo_texto = texto_atual[:-1]
    equacao.configure(text=novo_texto)

def cO1():
    equacao.configure(text = str(equacao._text) + " ~ ")

def cO2():      
    equacao.configure(text = str(equacao._text) + " ∧ ")

def cO3():
    equacao.configure(text = str(equacao._text) + " V ")

def cO4():
    equacao.configure(text = str(equacao._text) + " → ")

def cO5():
    equacao.configure(text = str(equacao._text) + " ↔ ")

def cO6():
    equacao.configure(text = str(equacao._text) + " ⊻ ")

def cO7():
    equacao.configure(text = str(equacao._text) + " ↓ ")

def cO8():
    equacao.configure(text = str(equacao._text) + " ↑ ")

def cO9():
    equacao.configure(text = str(equacao._text) + "(")

def cO10():
    equacao.configure(text = str(equacao._text) + ")")

def calcular():

    try:
        if 'B' in equacao._text and 'A' not in equacao._text:
            tela_erro1 = customtkinter.CTkToplevel()
            tela_erro1.attributes('-topmost', True)
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")
            tela_erro1.geometry("400x200")
            tela_erro1.title("ERRO")

            erro1 = customtkinter.CTkLabel(tela_erro1, text = "Porfavor, utilize a variável A antes da variável B")
            erro1.grid(padx = 50, pady = 10)

            def fechar1():
                tela_erro1.destroy()

            okB1 = customtkinter.CTkButton(tela_erro1, text = "OK!", command= fechar1)
            okB1.grid(padx = 50, pady = 10)

        elif 'C' in equacao._text and ('B' not in equacao._text or 'A' not in equacao._text):
            tela_erro2 = customtkinter.CTkToplevel()
            tela_erro2.attributes('-topmost', True)
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")
            tela_erro2.geometry("400x200")
            tela_erro2.title("ERRO")


            erro2 = customtkinter.CTkLabel(tela_erro2, text = "Porfavor, utilize as variáveis A ou B antes da variável C")
            erro2.grid(padx = 50, pady = 10)

            def fechar2():
                tela_erro2.destroy()
                
            okB2 = customtkinter.CTkButton(tela_erro2, text = "OK!", command= fechar2)
            okB2.grid(padx = 50, pady = 10)
            
        elif 'D' in equacao._text and ('C' not in equacao._text or 'B' not in equacao._text or 'A' not in equacao._text):
            tela_erro3 = customtkinter.CTkToplevel()
            tela_erro3.attributes('-topmost', True)
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")
            tela_erro3.geometry("400x200")
            tela_erro3.title("ERRO")


            erro3 = customtkinter.CTkLabel(tela_erro3, text = "Porfavor, utilize as variáveis A, B ou C antes da variável D")
            erro3.grid(padx = 50, pady = 10)

            def fechar3():
                tela_erro3.destroy()
                
            okB3 = customtkinter.CTkButton(tela_erro3, text = "OK!", command= fechar3)
            okB3.grid(padx = 50, pady = 10)

        else:

            tela_resultado = customtkinter.CTkToplevel()
            tela_resultado.attributes('-topmost', True)
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")
            tela_resultado.geometry("400x500")
            tela_resultado.title("Resultado")

            expressao = str(equacao._text)

            expressao = expressao.replace("∧", "and").replace("V", "or").replace("→", "=>").replace("↔", "=").replace("⊻", "xor").replace("↓", "nor").replace("↑", "nand")

            variaveis = ""

            if "A" in str(equacao._text):
                variaveis = ["A"]
            if "B" in str(equacao._text):
                variaveis = ["A","B"]
            if "C" in str(equacao._text):
                variaveis = ["A","B","C"]
            if "D" in str(equacao._text):
                variaveis = ["A","B","C","D"]

            tabela_vdd = ttg.Truths(variaveis, [expressao])
            
            frame5 = customtkinter.CTkFrame(tela_resultado)
            frame5.grid(padx = 100, pady = 10)

            label_resultado = customtkinter.CTkLabel(frame5, text= tabela_vdd)
            label_resultado.grid(row=0, column=3, padx=10, pady=10)

            text_tcc = tabela_vdd.valuation().replace("Contingency", "Contingência").replace("Tautology", "Tautologia").replace("Contradiction", "Contradição")

            tcc = customtkinter.CTkLabel(frame5, text= text_tcc)
            tcc.grid(row=1, column=3, padx=10, pady=10)

            def fechar_r():
                tela_resultado.destroy()
            
            but_sair = customtkinter.CTkButton(frame5, text= "Voltar", command= fechar_r)
            but_sair.grid(row=2, column=3, padx=10, pady=10)

    except:
        
        tela_erro4 = customtkinter.CTkToplevel()
        tela_erro4.attributes('-topmost', True)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue") 
        tela_erro4.geometry("400x200")
        tela_erro4.title("ERRO")


        erro4 = customtkinter.CTkLabel(tela_erro4, text = "Porfavor verifique a sintaxe da formula digitada")
        erro4.grid(padx = 50, pady = 10)

        def fechar4():
            tela_erro4.destroy()

        okB4 = customtkinter.CTkButton(tela_erro4, text = "OK!", command= fechar4)
        okB4.grid(padx = 50, pady = 10)


#-Frame------------------------------------------------------------------------------------------------------------------------

  
frame = customtkinter.CTkFrame(tela_calculadora)
frame.grid(row=2, column=0, columnspan=2, pady=10) 


#-Class HINT-------------------------------------------------------------------------------------------------------------------


class Hint:
    
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 50
        y += self.widget.winfo_rooty() + 50

       
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        
        label = tk.Label(self.tooltip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()

def botão_Dica(root, text, tooltip_text, command = None):
    button = customtkinter.CTkButton(root, text=text, command = command)
    tooltip = Hint(button, tooltip_text)

    button.bind("<Enter>", tooltip.show_tooltip)
    button.bind("<Leave>", tooltip.hide_tooltip)

    return button



#-Botões---------------------------------------------------------------------------------------------------------------------

        
b1 = customtkinter.CTkButton(frame, text="A", command = c1)
b1.grid(row=0, column=1, padx=10, pady=5)


b2 = customtkinter.CTkButton(frame, text="B", command = c2)
b2.grid(row=0, column=2, padx=10, pady=5)


b3 = customtkinter.CTkButton(frame, text="C", command = c3)
b3.grid(row=0, column=3, padx=10, pady=5)


b4 = customtkinter.CTkButton(frame, text="D", command = c4)
b4.grid(row=0, column=4, padx=10, pady=5)

b_apagar = customtkinter.CTkButton(frame, text="⌫", command = apagar)
b_apagar.grid(row=0, column=5, padx=10, pady=5)


bO1 = botão_Dica(frame, "~", "Negação", command = cO1)
bO1.grid(row=1, column=1, padx=10, pady=10)


bO2 = botão_Dica(frame, "∧", "Conjunção (e)", command = cO2)
bO2.grid(row=1, column=2, padx=10, pady=10)


bO3 = botão_Dica(frame, "V", "Disjunção (ou)", command = cO3)
bO3.grid(row=1, column=3, padx=10, pady=10)


bO4 = botão_Dica(frame, "→", "Condicional (se... então) - Implicação", command = cO4)
bO4.grid(row=1, column=4, padx=10, pady=10)


bO5 = botão_Dica(frame, "↔", "Bicondicional (se e somente se) - Equivalência", command = cO5)
bO5.grid(row=1, column=5, padx=10, pady=10)


bO6 = botão_Dica(frame, "⊻", "XOR - Disjunção exclusiva (ou um ou outro)", command = cO6)
bO6.grid(row=2, column=1, padx=10, pady=10)


bO7 = botão_Dica(frame, "↓", "NOR - Negação da Disjunção", command = cO7)
bO7.grid(row=2, column=2, padx=10, pady=10)


bO8 = botão_Dica(frame, "↑", "NAND - Negação da Conjunção", command = cO8)
bO8.grid(row=2, column=3, padx=10, pady=10)


bO9 = botão_Dica(frame, "(", "Parêntese de abertura", command = cO9)
bO9.grid(row=2, column=4, padx=10, pady=10)


bO10 = botão_Dica(frame, ")", "Parêntese de fechamento", command = cO10)
bO10.grid(row=2, column=5, padx=10, pady=10)


bRe = customtkinter.CTkButton(frame, text = "Calcular", command = calcular)
bRe.grid(row=3, column=3, padx=10, pady=10)

tela_calculadora.mainloop()
