import customtkinter
import tkinter
import ttg

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
tela_calculadora = customtkinter.CTk()
tela_calculadora.geometry("1000x700")
tela_calculadora.title("Calculadora Lógica")

tela_calculadora.columnconfigure(0, weight = 1)
tela_calculadora.rowconfigure(0, weight = 0)


frame_geral = customtkinter.CTkFrame(tela_calculadora)
frame_geral.grid(row=2, column=0, columnspan=2, pady=10)

equacao = customtkinter.CTkLabel(frame_geral, text = "")
equacao.grid(padx = 10, pady = 10)

frame_botao = customtkinter.CTkFrame(frame_geral)
frame_botao.grid(padx= 10, pady=10)


def agregar_na_equacao(letra_simbolo: str) -> None:
    
    equacao.configure(text= str(equacao.cget("text")) + letra_simbolo)


botaoA = customtkinter.CTkButton(frame_botao, text="A", command= lambda: agregar_na_equacao("A"))
botaoA.grid(row=0, column=1, padx=10, pady=5)


botaoB = customtkinter.CTkButton(frame_botao, text="B", command= lambda: agregar_na_equacao("B"))
botaoB.grid(row=0, column=2, padx=10, pady=5)


botaoC = customtkinter.CTkButton(frame_botao, text="C", command= lambda: agregar_na_equacao("C"))
botaoC.grid(row=0, column=3, padx=10, pady=5)


botaoD = customtkinter.CTkButton(frame_botao, text="D", command= lambda: agregar_na_equacao("D"))
botaoD.grid(row=0, column=4, padx=10, pady=5)

def apagar():
    equacao.configure(text= str(equacao.cget("text")[:-1]))

botao_apagar = customtkinter.CTkButton(frame_botao, text="⌫", command= apagar)
botao_apagar.grid(row=0, column=5, padx=10, pady=5)

botao_not = customtkinter.CTkButton(frame_botao, text="~", command = lambda: agregar_na_equacao("~"))
botao_not.grid(row=1, column=1, padx=10, pady=10)


botao_and = customtkinter.CTkButton(frame_botao, text="∧", command = lambda: agregar_na_equacao("^"))
botao_and.grid(row=1, column=2, padx=10, pady=10)


botao_or = customtkinter.CTkButton(frame_botao, text="V", command = lambda: agregar_na_equacao("v"))
botao_or.grid(row=1, column=3, padx=10, pady=10)


botao_condicional = customtkinter.CTkButton(frame_botao, text="→", command = lambda: agregar_na_equacao("→"))
botao_condicional.grid(row=1, column=4, padx=10, pady=10)


botao_bicondicional = customtkinter.CTkButton(frame_botao, text="↔", command = lambda: agregar_na_equacao("↔"))
botao_bicondicional.grid(row=1, column=5, padx=10, pady=10)


botao_xor = customtkinter.CTkButton(frame_botao, text="⊻", command = lambda: agregar_na_equacao("⊻"))
botao_xor.grid(row=2, column=1, padx=10, pady=10)


botao_nor = customtkinter.CTkButton(frame_botao, text="↓", command = lambda: agregar_na_equacao("↓"))
botao_nor.grid(row=2, column=2, padx=10, pady=10)


botao_nand = customtkinter.CTkButton(frame_botao, text="↑", command = lambda: agregar_na_equacao("↑"))
botao_nand.grid(row=2, column=3, padx=10, pady=10)


botao_abrir_parentese = customtkinter.CTkButton(frame_botao, text="(", command = lambda: agregar_na_equacao("("))
botao_abrir_parentese.grid(row=2, column=4, padx=10, pady=10)


botao_fechar_parentese = customtkinter.CTkButton(frame_botao, text=")", command = lambda: agregar_na_equacao(")"))
botao_fechar_parentese.grid(row=2, column=5, padx=10, pady=10)

def tela_erro(mensagem: str) -> None:

    tela_erro = customtkinter.CTkToplevel()
    tela_erro.attributes('-topmost', True)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    tela_erro.geometry("400x200")
    tela_erro.title("ERRO")

    erro = customtkinter.CTkLabel(tela_erro, text = mensagem)
    erro.grid(padx = 50, pady = 10)

    def fechar_tela_erro():
       tela_erro.destroy()

    botao_voltar = customtkinter.CTkButton(tela_erro, text = "OK!", command= fechar_tela_erro)
    botao_voltar.grid(padx = 50, pady = 10)

def tela_resultado(tabela: ttg):

    tela_resultado = customtkinter.CTkToplevel()
    tela_resultado.attributes('-topmost', True)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    tela_resultado.geometry("400x500")
    tela_resultado.title("Resultado")

    frame_resultado = customtkinter.CTkFrame(tela_resultado)
    frame_resultado.grid(padx = 100, pady = 10)

    resultado = customtkinter.CTkLabel(frame_resultado, text= tabela)
    resultado.grid(row=0, column=3, padx=10, pady=10)

    resposta_avaliacao_tcc = tabela.valuation().replace("Contingency", "Contingência").replace("Tautology", "Tautologia").replace("Contradiction", "Contradição")

    avaliacao_tcc = customtkinter.CTkLabel(frame_resultado, text= resposta_avaliacao_tcc)
    avaliacao_tcc.grid(row=1, column=3, padx=10, pady=10)

    def fechar_tela_resultado():
        tela_resultado.destroy()
            
    botao_fechar_tela_resultado = customtkinter.CTkButton(frame_resultado, text= "OK!", command= fechar_tela_resultado)
    botao_fechar_tela_resultado.grid(row=2, column=3, padx=10, pady=10)



def calcular(equacao: str) -> None:

    if "B" in equacao and "A" not in equacao:
        tela_erro("Porfavor, utilize a variável A antes da variável B")

    elif "C" in equacao and ("B" not in equacao or "A" not in equacao):
        tela_erro("Porfavor, utilize as variáveis A e B antes da variável C")

    elif "D" in equacao and ("C" not in equacao or "B" not in equacao or "A" not in equacao):
        tela_erro("Porfavor, utilize as variáveis A, B e C antes da variável D")

    else:
        
        equacao_formatada = equacao.replace("^", " and ").replace("v", " or ").replace("→", " => ").replace("↔", " = ").replace("⊻", " xor ").replace("↓", " nor ").replace("↑", " nand ")

        if "A" in equacao:
            variaveis = ["A"]
        if "B" in equacao:
            variaveis = ["A","B"]
        if "C" in equacao:
            variaveis = ["A","B","C"]
        if "D" in equacao:
            variaveis = ["A","B","C","D"]

        tabela_verdade = ttg.Truths(variaveis, [equacao_formatada])

        tela_resultado(tabela_verdade)
        

botao_calcular = customtkinter.CTkButton(frame_botao, text = "Calcular", command= lambda: calcular(equacao.cget("text")))
botao_calcular.grid(row=3, column=3, padx=10, pady=10)


tela_calculadora.mainloop()
