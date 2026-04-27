import pandas as pd
import matplotlib.pyplot as plt
import os

# Carrega os dados
caminho = os.path.join('data', 'transacoes.csv')
df = pd.read_csv(caminho)

# Entradas e saídas
entradas = df[df['tipo'] == 'entrada']['valor'].sum()
saidas = df[df['tipo'] == 'saida']['valor'].sum()
saldo = entradas - saidas

print(f"Total de entradas: R$ {entradas:.2f}")
print(f"Total de saídas: R$ {saidas:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")

# Exibe os gastos por categoria
gastos_categoria = df[df['tipo'] == 'saida'].groupby('categoria')['valor'].sum()
gastos_categoria = gastos_categoria.sort_values(ascending=False)

print("\nGastos por categoria:")
print(gastos_categoria)

# Exibe um gráfico dos resultados
plt.figure(figsize=(8,5))
gastos_categoria.plot(kind='bar', color='skyblue')
plt.title("Gastos por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
