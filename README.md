# SwitchGuard

**Manutenção preditiva das máquinas de chave S700K (CBM)**
Enterprise Challenge FIAP – Turma 1TSCOR – Empresa parceira: Motiva (Motiva Trilhos)

| Integrante | RM |
|---|---|
| Mauri Schulz | 575330 |

---

## 1. Objetivo da solução

O SwitchGuard estima a **probabilidade de falha de cada máquina de chave S700K nos próximos 30 dias**, explica os fatores que levam a esse risco e recomenda a ação de manutenção (roteiros N1, N2 e N3). O objetivo é apoiar a transição da manutenção por calendário para a **manutenção baseada na condição (CBM)**.

Saídas principais:
- Ranking de máquinas por risco (verde, amarelo, vermelho)
- Detalhe da máquina com os fatores do risco (SHAP)
- Alertas e recomendações de ação
- Comparação com as faixas do fabricante e estimativa de custo corretivo

## 2. Estrutura do repositório

```
switchguard/
├── data/
│   ├── raw/          # dados originais (base simulada Motiva) - NÃO versionados
│   ├── processed/    # dados tratados (Parquet) - NÃO versionados
│   └── sample/       # pequena amostra fictícia para demonstrar a execução
├── notebooks/        # exploração (EDA) e experimentos de modelagem
├── src/              # código do pipeline
│   ├── config.py             # caminhos e parâmetros (ex.: horizonte de 30 dias)
│   ├── preparacao.py         # leitura, limpeza e validação dos dados
│   ├── features.py           # criação de variáveis
│   ├── modelo.py             # treino, avaliação e explicação (SHAP)
│   └── exportar_powerbi.py   # gera as tabelas consumidas pelo Power BI
├── models/           # modelos treinados
├── outputs/powerbi/  # tabelas de resultado (fato_risco, fato_fatores, ...)
├── powerbi/          # arquivo .pbix do painel
├── docs/
│   ├── sprint1/      # documento de ideação e arquitetura (Sprint 1)
│   ├── bizagi/       # diagramas BPMN (AS-IS / TO-BE)
│   └── imagens/      # diagramas de arquitetura e protótipos
├── requirements.txt
└── README.md
```

## 3. Tecnologias e ferramentas

| Tecnologia | Função |
|---|---|
| Python 3.11+ / pandas | Preparação dos dados e criação de variáveis |
| Parquet / DuckDB | Armazenamento leve e consultas SQL locais |
| scikit-learn / XGBoost | Treino e avaliação dos modelos |
| SHAP | Explicabilidade das previsões |
| Power BI | Painel de risco, alertas e recomendações |
| Bizagi Modeler | Modelagem dos processos (BPMN) |
| GitHub | Versionamento e documentação |

A solução não depende de nenhum provedor de nuvem específico.

## 4. Configuração e execução

```bash
# 1. clonar o repositório
git clone https://github.com/<seu-usuario>/switchguard.git
cd switchguard

# 2. criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# 3. instalar as dependências
pip install -r requirements.txt

# 4. colocar a base simulada em data/raw/ e executar o pipeline
python -m src.preparacao
python -m src.features
python -m src.modelo
python -m src.exportar_powerbi

# 5. abrir powerbi/SwitchGuard.pbix e atualizar os dados
```

> Pipeline em construção – as etapas serão implementadas na Sprint 2.

## 5. Dependências

Listadas em `requirements.txt`.

## 6. Principais códigos e artefatos

| Arquivo | Descrição |
|---|---|
| `src/config.py` | Caminhos das pastas e parâmetros do projeto |
| `src/preparacao.py` | Leitura, limpeza e validação da base |
| `src/features.py` | Variáveis: assinatura da manobra, tendências, desvios, idade, histórico |
| `src/modelo.py` | Regressão logística (baseline), Random Forest/XGBoost e SHAP |
| `src/exportar_powerbi.py` | Exporta fato_risco, fato_fatores, fato_medicoes e dimensões |
| `docs/sprint1/` | Documento de ideação e arquitetura (Sprint 1) |

## 7. Limitações conhecidas

- Desenvolvido com base de dados **simulada**; resultados não representam a operação real.
- O horizonte de 30 dias será recalibrado conforme a granularidade da base.
- Falhas são eventos raros (classes desbalanceadas); métricas priorizam recall.
- Algumas falhas mecânicas não aparecem na corrente do motor; o modelo depende das variáveis disponíveis.
- As previsões apoiam a decisão da engenharia e não substituem as inspeções obrigatórias.

## 8. Uso responsável dos dados

- Nenhum dado restrito da Motiva, senha ou credencial é versionado (ver `.gitignore`).
- As previsões servem para a confiabilidade dos equipamentos, não para avaliar equipes de campo.
- Registros com nomes de pessoas são anonimizados (LGPD).
