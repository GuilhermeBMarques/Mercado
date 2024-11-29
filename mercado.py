import tkinter as tk
from tkinter import  ttk
import random

class Mercado:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Mercado")
        self.dados = []
        self.codigoBarra = 0
        self.Interface()

    def Interface(self):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
            
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
        ttk.Button(self.janela, text="Voltar", command=self.Interface).pack(pady=5)
        
        self.cadastrado = tk.Label(janela, text="")
        self.cadastrado.pack()
        
    def cadastroProduto(self): 
        nome = self.nomeProduto.get()
        preco = float(self.precoProduto.get())
        quantidade = int(self.quantidadeProduto.get())
        codigo = self.codigoBarra
        codigo += 1
        
        self.dados.append((nome, preco, quantidade, codigo))   
        self.cadastrado.config(text=f"Item: {nome} cadastrado com sucesso!") 
             
    def exibir_produtos(self):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        self.tree = ttk.Treeview(janela, columns=("Nome", "Preco", "Quantidade", "Codigo"), show="headings", height=5)
        self.tree.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preço")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.column("Nome", width=150, anchor=tk.CENTER)
        self.tree.column("Preco", width=100, anchor=tk.CENTER)
        self.tree.column("Quantidade", width=100, anchor=tk.CENTER)
        self.tree.column("Codigo", width=100, anchor=tk.CENTER)
        
        for nome, preco, quantidade, codigo in self.dados:
            self.tree.insert("", tk.END, values=(nome, preco, quantidade, codigo))
        
        ttk.Button(self.janela, text="Voltar", command=self.Interface).place(relx = 0.5, rely = 0.7, anchor = "center")
    
    def realizar_venda(self):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
            
        self.tree = ttk.Treeview(janela, columns=("Nome", "Preco", "Quantidade", "Codigo"), show="headings", height=5)
        self.tree.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preço")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.column("Nome", width=150, anchor=tk.CENTER)
        self.tree.column("Preco", width=100, anchor=tk.CENTER)
        self.tree.column("Quantidade", width=100, anchor=tk.CENTER)
        self.tree.column("Codigo", width=100, anchor=tk.CENTER)
        
        for nome, preco, quantidade, codigo in self.dados:
            self.tree.insert("", tk.END, values=(nome, preco, quantidade, codigo))

        ttk.Label(janela, text="Digite o codigo do produto").pack()
        self.codigoProduto = ttk.Entry(janela)
        self.codigoProduto.pack(pady=10)
        
        ttk.Label(janela, text="Digite a quantidade do produto").pack()
        self.quantidadeProduto = ttk.Entry(janela)
        self.quantidadeProduto.pack(pady=10)
        
        self.botao = ttk.Button(janela, text="Comprar", command=self.compra_realizada)
        self.botao.pack()
        
        ttk.Button(self.janela, text="Voltar", command=self.Interface).pack()
        
        self.resultado = tk.Label(janela, text="")
        self.resultado.pack()

    def compra_realizada(self):
        try:
            cb = int(self.codigoProduto.get())
            quantidadeSocilicitada = int(self.quantidadeProduto.get())
            
            for self.nome, self.preco, self.quantidade, self.codigo in self.dados:
            
                if self.codigo == cb:
                    if quantidadeSocilicitada > self.quantidade:
                        self.resultado.config(text=f"O numero é maior que a quantidade")
                    else:
                        self.quantidade -= quantidadeSocilicitada
                        self.resultado.config(text=f"Compra realizada")
                else:
                    self.resultado.config(text=f"Esse codigo não existe!")
                
        except ValueError as error:
            self.resultado.config(text=f"Insira um numero!")
            print(f"Erro: {error}")
        
if __name__ == "__main__":
    janela = tk.Tk()
    janela.state("zoomed")
    app = Mercado(janela)
    janela.mainloop()
