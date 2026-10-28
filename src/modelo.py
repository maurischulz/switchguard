"""Etapa 3 - Treino, avaliação e explicação do modelo de risco.

Plano:
1. Separação temporal (treino no passado, teste no período mais recente)
2. Baseline: regressão logística
3. Modelo principal: Random Forest ou XGBoost
4. Métricas: recall da classe falha (prioridade), precisão, PR-AUC, matriz de confusão
5. Explicabilidade: SHAP
"""
from src.config import DATA_PROCESSED, MODELS, SEED


def main() -> None:
    """TODO Sprint 2: implementar treino e avaliação."""
    print(f"Modelagem pendente. Dados: {DATA_PROCESSED} | Modelos: {MODELS} | seed={SEED}")


if __name__ == "__main__":
    main()
