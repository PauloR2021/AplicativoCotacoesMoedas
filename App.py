
from tkinter import *
import tkinter.messagebox as MSG
import requests

class CotacaoMoeda:
    
    def __init__(self):
        janela = self.janela_principal()
        
########################################################################## Iniciando a Aplciação ##################################################################### 
    #Comado para Chamar a Tela Principal do Menu
    def janela_principal(self):
        
        #Criando as Propriedades da Telas
        self.janela = Tk()
        self.janela.title("APP COTAÇÃO")
        self.janela.geometry("400x200")
        self.janela.config(background="#37383b")
        self.janela.iconbitmap('Icones/iconeJanela.ico')
        self.janela.resizable(width=False,height=False)
                
        textoBotaoMoeda=Label(self.janela,text="COTAÇÃO MOEDAS",anchor=CENTER,font='Arial,20,bold',foreground="#4169E1",background="#37383b",bd=4)
        textoBotaoMoeda.place(y=20,x=10)
        
        iconeMoeda = PhotoImage(file='Icones/iconeMoeda.png',master=self.janela)
        botao = Button(self.janela, command=self.chamarProgramaMoeda,image=iconeMoeda,bg="#4169E1",activebackground="#4169E1",bd=3,highlightthickness=0)
        botao.place(y=20,x=220)
        
        
        textoBotaoSelic=Label(self.janela,text="COTAÇÃO SELIC E CDI",anchor=CENTER,font='Arial,20,bold',foreground="#4169E1",background="#37383b",bd=4)
        textoBotaoSelic.place(y=100,x=10) 
        
        iconeSelic = PhotoImage(file='Icones/iconeCotacao.png',master=self.janela)
        self.botao_selic = Button(self.janela, command=self.chamarProgramaSelic,image=iconeSelic,bg="#4169E1",activebackground="#4169E1",bd=3,highlightthickness=0)
        self.botao_selic.place(y=100 ,x= 220)
        
        texto=Label(self.janela,text="By-Paulo Ricardo",font='arial,02,bold',anchor=CENTER,foreground="#4169E1",background="#37383b",bd=1)
        texto.place(y=170,x=260)
    
        self.janela.mainloop()
    #Comando para chamar a Janela de Cotações de Moeda
    def chamarProgramaMoeda(self):
        self.janela.withdraw()
        self.telaCotacao()
    #Comando para chamar a Janela de Cotações da Selic e CDI
    def chamarProgramaSelic(self):
        self.janela.withdraw()
        self.telaSelic()

#################################################################### Criando a Janela das Cotações de Moedas ##################################################################### 
    #Comando para chamar a Tela de Cotações
    def telaCotacao(self):
        
        try:
            
            #definindo as Propriedades da Janela
            self.tela_Cotacao = Tk()
            self.tela_Cotacao.title("COTAÇÃO DE MOEDAS")
            self.tela_Cotacao.geometry("450x450")
            self.tela_Cotacao.config(background="#4169E1")
            self.tela_Cotacao.iconbitmap('Icones/iconeJanela.ico')
            self.tela_Cotacao.resizable(width=False,height=False)
            
            #Criando o Layout e as Informações da Janela:
            
            #Txt Para colocar a Moeda que deseja Buscar
            texto_buscar = Label(self.tela_Cotacao,text="Buscar Moeda:",font="arial,14,bold",background="#4169E1")
            texto_buscar.place(y=50,x=20)
            
            self.get_buscar = Entry(self.tela_Cotacao,text="",width=20,font='arial,10,bold')
            self.get_buscar.place(y=50,x=200)
            
            
            #Txt Para Retornar o Nome da Moeda
            texto_nomeMoeda = Label(self.tela_Cotacao,text="Nome Moeda:",font="arial,14.bold",background="#4169E1",)
            texto_nomeMoeda.place(y=100,x=20)
            
            self.get_nome = Entry(self.tela_Cotacao,text="",width=20,font='arial,10,bold',background='white')
            self.get_nome.place(y=100,x=200)
            
            
            #Txt Para Retornar o Valor de Compra da Moeda
            text_valorCompra = Label(self.tela_Cotacao,text="Valor Compra:",font="arial,14.bold",background="#4169E1")
            text_valorCompra.place(y=150,x=20)
            
            self.get_valorCompra = Entry(self.tela_Cotacao,text="",width=20,font='arial,10,bold',background='white')
            self.get_valorCompra.place(y=150,x=200)
            
            #Txt para Retornar o Valor de Venda da Moeda
            
            txt_valorVenda = Label(self.tela_Cotacao,text="Valor Venda:",font="arial,14.bold",background="#4169E1")
            txt_valorVenda.place(y=200,x=20)
            
            self.get_valorVenda = Entry(self.tela_Cotacao,text="",width=20,font='arial,10,bold',background='white')
            self.get_valorVenda.place(y=200,x=200)
            
            #Txt para Retornar a Variação de Valores da Moeda
            
            txt_valorVariacao = Label(self.tela_Cotacao,text="Valor da Variação:",font="arial,14.bold",background="#4169E1")
            txt_valorVariacao.place(y=250,x=20)
            
            self.get_Variacao = Entry(self.tela_Cotacao,text="",width=20,font='arial,10,bold',background='white')
            self.get_Variacao.place(y=250, x=200)
            
            
            #Botão para Chamar o Menu
            self.iconeMenu = PhotoImage(file='Icones/iconeMenu.png',master=self.tela_Cotacao)
            botao_Menu = Button(self.tela_Cotacao,command=self.comandoMenu,image=self.iconeMenu,bg="#4169E1",activebackground="#4169E1",bd=3,highlightthickness=0)
            botao_Menu.place(y=10,x=400) 
            
            #Botão para Chamar a Função de Cotação
            iconePesquisa = PhotoImage(file='Icones/iconePesquisa.png',master=self.tela_Cotacao)
            botao = Button(self.tela_Cotacao,image=iconePesquisa,command=self.comandoBuscarCotacao,bg="#4169E1",activebackground="#4169E1",bd=3,highlightthickness=0)
            botao.place(y=300,x=100) 
            
            #Botão para Limpar as Label
            iconeLimpar = PhotoImage(file='Icones/iconeLimpar.png',master=self.tela_Cotacao)
            botao_Limpar = Button(self.tela_Cotacao,image=iconeLimpar,command=self.comandoLimpar,bg="#4169E1",activebackground="#4169E1",bd=3,highlightthickness=0)
            botao_Limpar.place(y=300,x=300)
            
            self.tela_Cotacao.mainloop()
            
        except Exception as erro:
            MSG.showerror(title="Erro",message=f"Erro >: {erro}") 
    #Comando para Chamar o Menu       
    def comandoMenu(self):
        self.tela_Cotacao.withdraw()
        self.janela_principal()    
    #Função para Buscar os dados lá da API das Moedas
    def comandoBuscarCotacao(self):
        
        try:
            
            #Instanciando a moeda          
            moeda = self.get_buscar.get().upper()
            
            #Verificação para ver se a Moeda não está vazia
            if not moeda:
                MSG.showerror(title="Error", message="Erro: Coloque uma moeda para realizar a busca")
            else:
                
                #Link com a Requisição para o Request
                
                link = f"https://api.hgbrasil.com/finance?array_limit=1&fields=only_results,{moeda}&key=625e9891"
                
                requisicao = requests.get(link).json()
                
                #Verificando se a Requisição está vazia 
                if not requisicao:
                    MSG.showerror(title="Error", message=f"Erro: Moeda Não Encontrada! -- {moeda}")
                    
                else:
                    self.comandoLimpar()
                    #Atribuindo os valores do Request
                    nome = requisicao['currencies']['name']
                    compra = requisicao['currencies']['buy']
                    venda = requisicao['currencies']['sell']
                    variacao = requisicao['currencies']['variation']
                    
                    if not compra:
                        MSG.showerror(title="Compra Vázia",message="Não Existe Valor de Compra")
                    if not venda:
                        MSG.showerror(title="Venda Vázia",message="Não Existe Valor de Venda")
                    else:
                        pass
                    
                    #Mostrando os Valores nas Labels
                    self.get_nome.insert('insert',nome)
                    self.get_valorCompra.insert('insert',f"{compra:,.2f}")
                    self.get_valorVenda.insert('insert',f"{venda:,.2f}")
                    self.get_Variacao.insert('insert',"{0:.2f}%".format(variacao))
                    
        except:
            MSG.showerror(title="Erro",message=f"Erro na Busca")
    #Função para Limpar as Entry(entrada de Texto) do Programa
    def comandoLimpar(self):
        
        self.get_buscar.delete(0,END)
        self.get_nome.delete(0,END)
        self.get_valorCompra.delete(0,END)
        self.get_valorVenda.delete(0,END)
        self.get_Variacao.delete(0,END)

####################################################################### Criando a Jenela das Cotações Selic E CDI #######################################################################
    #Comando para chamar a Tela da CDI
    def telaSelic(self):
        
        self.tela_Selic = Tk()
        self.tela_Selic.title("COTAÇÃO DA SELIC e CDI")
        self.tela_Selic.geometry("450x500")
        self.tela_Selic.config(background="#4169E1")
        self.tela_Selic.iconbitmap('Icones/iconeJanela.ico')
        self.tela_Selic.resizable(width=False,height=False)
        
        #Txt para Mostrar a Data da Consulta
        texto_data = Label(self.tela_Selic,text="Data:",font="arial,14,bold",background="#4169E1")
        texto_data.place(y=50,x=30)
        
        self.data_get =Entry(self.tela_Selic,text="",width=20,font='arial,10,bold',background='white')
        self.data_get.place(y=50, x=200)
        
        #Txt para mostrar o Valor da CDI
        texto_cdi = Label(self.tela_Selic,text="CDI:",font="arial,14,bord",background="#4169E1")
        texto_cdi.place(y=100, x=30)
        
        self.cdi_get = Entry(self.tela_Selic,text="",width=20,font="arial,10,bold",background='white')
        self.cdi_get.place(y=100,x=200)
        
        #Txt para mostra o Valor da Selic
        
        texto_selic = Label(self.tela_Selic,text="Selic:",font='arial,14,bold',background="#4169E1")
        texto_selic.place(y=150,x=30)
        
        self.selic_get=Entry(self.tela_Selic,text="",width=20,font="arial,10,bold",background="white")
        self.selic_get.place(y=150,x=200)
        
        #Txt Selic diária
        
        texto_selicDiaria = Label(self.tela_Selic,text="Selic Diária:",font='arial,14,bold',background="#4169E1")   
        texto_selicDiaria.place(y=200,x=30)
        
        self.selicDiaria_get=Entry(self.tela_Selic,text="",font="arial,10,bold",background="white")
        self.selicDiaria_get.place(y=200,x=200)
        
        #Txt CDI diária

        texto_cdiDiaria= Label(self.tela_Selic,text="CDI Diária:",font="arial,14,bold",background="#4169E1")
        texto_cdiDiaria.place(y=250,x=30)        
        
        self.cdiDiaria_get=Entry(self.tela_Selic,text="",width=20,font="arial,10",background="white")
        self.cdiDiaria_get.place(y=250,x=200)
        
        
        #Botão para Chamar o Menu
        iconeMenu = PhotoImage(file='Icones/IconeMenu.png',master=self.tela_Selic)
        botao_menu = Button(self.tela_Selic,command=self.comandoMenuSelic,font='arial,12,bold',image=iconeMenu,bg="#4169E1",activebackground='#4169E1',bd=3,highlightthickness=0)
        botao_menu.place(y=10,x=400) 
       
        #Botão para Chamar a Função de Cotação
        iconePesquisa = PhotoImage(file='Icones/iconePesquisa.png',master=self.tela_Selic)
        botao_Consultar = Button(self.tela_Selic,command=self.comandoBuscarSeli,border="2",font='arial,12,bold',image=iconePesquisa,bg="#4169E1",activebackground='#4169E1',bd=3,highlightthickness=0)
        botao_Consultar.place(y=300,x=100) 
        
        #Botão para Limpar as Label 
        iconeLimpar = PhotoImage(file='Icones/iconeLimpar.png',master=self.tela_Selic)
        botao_Limpar = Button(self.tela_Selic,command=self.comandoLimparSelic,border="2",font='arial,12,bold',image=iconeLimpar,bg="#4169E1",activebackground="#4169E1",bd=3,highlightthickness=0)      
        botao_Limpar.place(y=300,x=300)
        
        
        
        self.tela_Selic.mainloop()  
    #Comando para Chamar a Buscar de Dados dentro da API
    def comandoBuscarSeli(self):
        
       try:
           
            #Link para requisição da API
            link = f"https://api.hgbrasil.com/finance/taxes?key=625e9891"
                
            requisicao = requests.get(link).json()
            
            #Verificando se a Requisição Vai retornar algum valor
            if not requisicao:
                MSG.showerror(title="Erro",message="Não Foi Encontrado a Requisição")
            else:
                #Lipando as Entrys da Tela
                self.comandoLimparSelic()
                
                #Buscando os dados da API e mostrando para o Usário
                data = requisicao["results"][0]['date']
                cdi=requisicao['results'][0]['cdi']
                selic =requisicao["results"][0]['selic']
                selicDiaria=requisicao["results"][0]['selic_daily']
                cdiDiaria =requisicao["results"][0]['cdi_daily']              

                self.data_get.insert('insert',data)
                self.cdi_get.insert('insert',"{0:.2f}%".format(cdi))
                self.selic_get.insert('insert',"{0:.2f}%".format(selic))
                self.selicDiaria_get.insert('insert',"{0:.2f}%".format(selicDiaria))
                self.cdiDiaria_get.insert('insert',"{0:.2f}%".format(cdiDiaria))
                
        #Caso se der algum erro na Busca da API 
       except Exception as erro:
            MSG.showerror(title="Erro",message=f"Erro na Busca: {erro}")
    #Comando para Chamar o Menu na Tela das Informações da Selic e CDI
    def comandoMenuSelic(self):
        self.tela_Selic.withdraw()
        self.janela_principal()      
    #Comando para Limpara as Entrys da Tela  
    def comandoLimparSelic(self):
        self.data_get.delete(0,END)
        self.cdi_get.delete(0,END)
        self.selic_get.delete(0,END)
        self.selicDiaria_get.delete(0,END)
        self.cdiDiaria_get.delete(0,END)



if __name__ == "__main__":
    chamar = CotacaoMoeda()
   


