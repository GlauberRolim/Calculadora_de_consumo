# ⚡ Calculadora de Consumo de Energia Elétrica

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Energy](https://img.shields.io/badge/Energia-El%C3%A9trica-FFD700?style=for-the-badge&logo=lightning)

## 📌 Objetivo do Sistema

A **Calculadora de Consumo de Energia Elétrica** é um script em Python desenvolvido para calcular a estimativa de consumo mensal em quilowatt-hora ($kWh$) de qualquer aparelho doméstico. O objetivo é oferecer uma forma simples de monitorar e entender o consumo elétrico residencial.

## 🧮 Fórmula Utilizada

O consumo mensal é calculado a partir da potência do aparelho em Watts ($W$), do tempo diário de uso em horas e do período padrão de 30 dias:

$$
Consumo\ Mensal\ (kWh) = \frac{Potência\ (W) \times Tempo\ de\ Uso\ (horas) \times 30}{1000}
$$

> **Onde:**
> * **Potência ($W$):** Valor informado pelo usuário em Watts.
> * **Tempo de Uso:** Média de horas diárias que o aparelho permanece ligado.
> * **30:** Quantidade fixa de dias considerada para o mês.
> * **1000:** Fator de conversão de Watts ($W$) para Quilowatts ($kW$).

## 💻 Código Fonte (`consumo_energia.py`)

```python
# consumo de energia

# coletando os dados
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em Watts(W): "))
tempo_de_uso = float(input("Digite o tempo médio de uso diário em horas do aparelho: "))

# realizando os cálculos
consumoMensal = (potencia * tempo_de_uso * 30) / 1000

# saída dos dados
print("Aparelho:", nome_aparelho)
print("Consumo estimado:", consumoMensal, "KWh / mês")
```

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação para execução da lógica do script.
* **GitHub:** Plataforma para hospedagem e controle de versão do código.

## 🖥️ Exemplo de Execução

```text
Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em Watts(W): 150
Digite o tempo médio de uso diário em horas do aparelho: 24
Aparelho: Geladeira
Consumo estimado: 108.0 KWh / mês
```
