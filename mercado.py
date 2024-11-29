import tkinter as tk
from tkinter import  ttk

class Mercado:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Mercado")
        self.dados = []
        
        self.cadastroProdutos = ttk.Button(janela, text="🏷️ Cadastro de produtos", command=self.adicionar_produto)
        self.cadastroProdutos.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.listaProdutos = ttk.Button(janela, text="📋 Exibição da lista de produtos cadastrados", command=self.exibir_produtos)
        self.listaProdutos.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.vendasProdutos = ttk.Button(janela, text="💸 Realização de vendas, com cálculo do total e atualização do estoque", command=self.realizar_venda)
        self.vendasProdutos.place(relx = 0.5, rely = 0.6, anchor = "center")
        
    def adicionar_produto(self):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        ttk.Label(janela, text="Digite nome do produto").pack()
        self.nomeProduto = ttk.Entry(janela)
        self.nomeProduto.pack()
        
        ttk.Label(janela, text="Digite preco do produto").pack()
        self.precoProduto = ttk.Entry(janela)
        self.precoProduto.pack()
        
        ttk.Label(janela, text="Digite quantidade do produto").pack()
        self.quantidadeProduto = ttk.Entry(janela)
        self.quantidadeProduto.pack()
        
        self.botao = ttk.Button(janela, text="Cadastrar", command=self.cadastroProduto)
        self.botao.pack()
        ttk.Button(self.janela, text="Voltar", command=self.voltar_menu).pack(pady=5)
        
        
        self.cadastrado = ttk.Label(text="")
        self.cadastrado.pack()
        
        print(self.dados)
        
    def cadastroProduto(self):
        nome = self.nomeProduto.get()
        preco = float(self.precoProduto.get())
        quantidade = int(self.quantidadeProduto.get())
        
        self.dados.append((nome, preco, quantidade))   
        self.cadastrado.config(janela, text=f"{self.dados[nome]} cadastrado com sucesso!") 
        print(self.dados)  
             
    def exibir_produtos(self):

        for widget in self.janela.winfo_children():
            widget.destroy()
            
        print(self.dados)
        self.tree = ttk.Treeview(janela, columns=("Nome", "Preco", "Quantidade"), show="headings", height=5)
        self.tree.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preço")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.column("Nome", width=150, anchor=tk.CENTER)
        self.tree.column("Preco", width=100, anchor=tk.CENTER)
        self.tree.column("Quantidade", width=100, anchor=tk.CENTER)
        
        ttk.Button(self.janela, text="Voltar", command=self.voltar_menu).place(relx = 0.5, rely = 0.7, anchor = "center")
    
    def realizar_venda(self):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        ttk.Button(self.janela, text="Voltar", command=self.voltar_menu).pack(pady=5)
  
  
    
    
    def voltar_menu(self):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
        self.__init__(self.janela)
        
          

if __name__ == "__main__":
    janela = tk.Tk()
    janela.state("zoomed")
    app = Mercado(janela)
    janela.mainloop()