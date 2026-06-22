# 03 — Mineração de Dados

Disciplina **Mineração de Dados e Visualização** (Prof. Fernando S. de Aguiar Neto), cobrindo todo o fluxo de descoberta de conhecimento: do entendimento e pré-processamento dos dados às tarefas de associação, agrupamento e classificação, com aplicação em **Python** (pandas, numpy, scikit-learn, matplotlib, seaborn).

## 📚 Conteúdos estudados na disciplina

**Fundamentos**
- O que é Mineração de Dados; **dado, informação e conhecimento**
- Laço/ciclo de **descoberta de conhecimento (KDD)** e tipos de dados

**Pré-processamento e tratamento de dados**
- Vieses e qualidade dos dados, tipos de atributos
- **Discretização / binning**
- **Imputação de valores ausentes** (estatísticas descritivas, vizinhança/KNN)

**Tarefas de mineração**
- **Regras de associação** — algoritmo **A Priori** (suporte, confiança, lift)
- **Agrupamento (clustering)** particional — **K-Means**
- **Classificação supervisionada** — **Árvore de Decisão** e **Naive Bayes**

**Avaliação e visualização**
- **Avaliação de modelos** supervisionados (treino/teste, generalização, métricas)
- **Regressão linear** aplicada
- Visualização de dados (scatter plots, pairplots, heatmaps) com pandas/matplotlib/seaborn

**Business Intelligence**
- Conceitos de **BI** e metodologias **CRISP-DM** e **SEMMA**

## 🛠️ Projetos aplicados

### 🛒 Regras de Associação (T1)
Extração de **regras fortes** a partir de uma base de transações de supermercado, com interpretação das métricas de **suporte, confiança e lift** para propor cenários e intervenções de negócio.
- [`regras-associacao-t1.ipynb`](./regras-associacao-t1.ipynb)

### 🐧 Imputação de Dados — Palmer Penguins (T2)
Pipeline em Python para **tratar valores ausentes** combinando regressão **KNN** com seleção de `k`, regras determinísticas por **ilha** e *fallback* por **mediana** da espécie, com análise exploratória (pairplots e heatmaps) para validar as relações entre espécie e ilha.
- [`imputacao-penguins-t2.ipynb`](./imputacao-penguins-t2.ipynb)
- 📊 Resultado também visualizado em **dashboard de Power BI** → ver [`04-power-bi`](../04-power-bi)

> Projetos desenvolvidos em grupo.
