import tkinter as tk
from tkinter import ttk

class Mercado:
    def __init__(self, janela):
        self.janela = janela  
        self.janela.title("Mercado")  
        self.dados = []  
        self.codigoBarra = 0  
        self.Loja()  

    def Loja(self):
        
        # "Limpa" a janela e cria a interface dos botões
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        # Botões das opções da loja
        self.cadastroProdutos = ttk.Button(janela, text="🏷️ Cadastro de produtos", command=self.adicionar_produto)
        self.listaProdutos = ttk.Button(janela, text="📋 Exibição da lista de produtos cadastrados", command=self.exibir_produtos)
        self.vendasProdutos = ttk.Button(janela, text="💸 Realização de vendas, com cálculo do total e atualização do estoque", command=self.realizar_venda)
        
        # Css
        self.cadastroProdutos.place(relx=0.5, rely=0.4, anchor="center") 
        self.cadastroProdutos.configure(cursor='hand2')  
        self.listaProdutos.place(relx=0.5, rely=0.5, anchor="center")  
        self.listaProdutos.configure(cursor='hand2')       
        self.vendasProdutos.place(relx=0.5, rely=0.6, anchor="center") 
        self.vendasProdutos.configure(cursor='hand2')

    def adicionar_produto(self):
        
        # "Limpa" a janela e cria a interface de cadastro de produto
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Inserir os dados do produto
        ttk.Label(janela, text="Digite nome do produto:").place(relx=0.4, rely=0.4, anchor="center")
        self.nomeProduto = ttk.Entry(janela)
        self.nomeProduto.place(relx=0.5, rely=0.4, anchor="center")
        
        ttk.Label(janela, text="Digite preco do produto:").place(relx=0.4, rely=0.5, anchor="center")
        self.precoProduto = ttk.Entry(janela)
        self.precoProduto.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(janela, text="Digite quantidade do produto:").place(relx=0.4, rely=0.6, anchor="center")
        self.quantidadeProduto = ttk.Entry(janela)
        self.quantidadeProduto.place(relx=0.5, rely=0.6, anchor="center")
        
        # Botão para cadastrar o produto 
        self.cadastrar = ttk.Button(janela, text="Cadastrar", command=self.cadastroProduto)
        self.cadastrar.place(relx=0.5, rely=0.7, anchor="center")
        self.cadastrar.configure(cursor='hand2')
        
        # Botão para voltar 
        self.voltar = ttk.Button(janela, text="Voltar", command=self.Loja)
        self.voltar.place(relx=0.5, rely=0.8, anchor="center")
        self.voltar.configure(cursor='hand2')

        # Mostrar se o produto foi cadastrado com sucesso
        self.cadastrado = tk.Label(janela, text="")
        self.cadastrado.pack()

    def cadastroProduto(self):
        # Obtém os dados do produto inserido
        nome = self.nomeProduto.get()
        preco = float(self.precoProduto.get()) 
        quantidade = int(self.quantidadeProduto.get())  
        self.codigoBarra += 1 
        codigo = self.codigoBarra
        
        # Adiciona o produto à lista de produtos cadastrados
        self.dados.append((nome, preco, quantidade, codigo))   
        self.cadastrado.config(text=f"Item: {nome} cadastrado com sucesso!") 

    def exibir_produtos(self):
        
        # "Limpa" a janela e cria a interface para exibir a lista de produtos
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Cria a tabela
        self.tree = ttk.Treeview(janela, columns=("Nome", "Preco", "Quantidade", "Codigo"), show="headings", height=5)
        self.tree.place(relx=0.5, rely=0.5, anchor="center")

        # Define os cabeçalhos da tabela
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preço")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Codigo", text="Código")
        
        # Css
        self.tree.column("Nome", width=150, anchor=tk.CENTER)
        self.tree.column("Preco", width=100, anchor=tk.CENTER)
        self.tree.column("Quantidade", width=100, anchor=tk.CENTER)
        self.tree.column("Codigo", width=100, anchor=tk.CENTER)
        
        # Insere os dados dos produtos na tabela
        for nome, preco, quantidade, codigo in self.dados:
            self.tree.insert("", tk.END, values=(nome, preco, quantidade, codigo))
        
        # Botão para voltar 
        self.voltar = ttk.Button(janela, text="Voltar", command=self.Loja)
        self.voltar.place(relx=0.5, rely=0.6, anchor="center")
        self.voltar.configure(cursor='hand2')

    def realizar_venda(self):
        
        # "Limpa" a janela e cria a interface para realizar uma venda
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Cria a tabela de produtos
        self.tree = ttk.Treeview(janela, columns=("Nome", "Preco", "Quantidade", "Codigo"), show="headings", height=5)
        self.tree.place(relx=0.5, rely=0.5, anchor="center")

        # Define os cabeçalhos da tabela
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preço")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Codigo", text="Código")
        
        # Css
        self.tree.column("Nome", width=150, anchor=tk.CENTER)
        self.tree.column("Preco", width=100, anchor=tk.CENTER)
        self.tree.column("Quantidade", width=100, anchor=tk.CENTER)
        self.tree.column("Codigo", width=100, anchor=tk.CENTER)
        
        # Insere os produtos cadastrados na tabela
        for nome, preco, quantidade, codigo in self.dados:
            self.tree.insert("", tk.END, values=(nome, preco, quantidade, codigo))

        # Insere o código e quantidade do produto a ser comprado
        ttk.Label(janela, text="Digite o código do produto").pack()
        self.codigoProduto = ttk.Entry(janela)
        self.codigoProduto.pack(pady=10)
        
        ttk.Label(janela, text="Digite a quantidade do produto").pack()
        self.quantidadeProduto = ttk.Entry(janela)
        self.quantidadeProduto.pack(pady=10)
        
        # Botão para finalizar a compra
        self.comprar = ttk.Button(janela, text="Comprar", command=self.compra_realizada)
        self.comprar.pack()
        self.comprar.configure(cursor='hand2')
        
        # Botão para voltar
        self.voltar = ttk.Button(janela, text="Voltar", command=self.Loja)
        self.voltar.place(relx=0.5, rely=0.6, anchor="center")
        self.voltar.configure(cursor='hand2')
        
        # Mostra o resultado da compra
        self.resultado = tk.Label(janela, text="")
        self.resultado.pack()

    def compra_realizada(self):
        try:
            cb = int(self.codigoProduto.get())  
            quantidadeSolicitada = int(self.quantidadeProduto.get())  
            
            produto_encontrado = False
            for i, (nome, preco, quantidade, codigo) in enumerate(self.dados):
                if codigo == cb: 
                    produto_encontrado = True
                    if quantidadeSolicitada > quantidade:  
                        self.resultado.config(text="A quantidade solicitada é maior que o estoque disponível")
                    else:
                        # Atualiza o estoque após a compra
                        self.dados[i] = (nome, preco, quantidade - quantidadeSolicitada, codigo)
                        self.resultado.config(text="Compra realizada!")
                    break
                
            if not produto_encontrado:
                self.resultado.config(text="Código do produto não encontrado!")
      
        except ValueError:
            self.resultado.config(text="Insira um número válido!")

if __name__ == "__main__":
    janela = tk.Tk()  
    janela.state("zoomed")  
    app = Mercado(janela) 
    janela.mainloop()  
