"""Etapa 4 - Exporta as tabelas de resultado consumidas pelo Power BI.

Tabelas (outputs/powerbi/):
- fato_risco:            máquina, data_ref, prob_falha_30d, nivel_risco, health_score
- fato_fatores:          máquina, variável, contribuição SHAP
- fato_medicoes:         máquina, data, variáveis monitoradas
- dim_maquina:           identificação, região, tipo de AMV, idade
- dim_faixas_fabricante: variável, limite mínimo, limite máximo
- dim_acoes:             nível, causa provável, ação recomendada, roteiro (N1/N2/N3)
"""
from src.config import LIMIAR_AMARELO, LIMIAR_VERMELHO, OUTPUT_POWERBI


def nivel_risco(prob: float) -> str:
    if prob >= LIMIAR_VERMELHO:
        return "Vermelho"
    if prob >= LIMIAR_AMARELO:
        return "Amarelo"
    return "Verde"


def main() -> None:
    """TODO Sprint 2: gerar e salvar as tabelas em CSV."""
    OUTPUT_POWERBI.mkdir(parents=True, exist_ok=True)
    print(f"Exportação pendente para {OUTPUT_POWERBI}")


if __name__ == "__main__":
    main()
