"""Etapa 2 - Criação de variáveis (features).

Grupos previstos (ver docs/sprint1):
- Sinal elétrico: pico de partida, média do platô, subida no travamento, duração
- Mecânico: tempo e força de manobra, vibração
- Detecção e isolamento: perdas de correspondência, resistência de isolamento
- Ambiente: umidade / gabinete
- Uso e idade: idade da máquina, manobras acumuladas
- Histórico: dias desde a última N1/N2/N3, falhas nos últimos 12 meses
- Desvios: distância das faixas do fabricante e da tendência da própria máquina

Alvo: falha nos próximos HORIZONTE_DIAS (0/1).
"""
import pandas as pd

from src.config import DATA_PROCESSED, HORIZONTE_DIAS


def criar_features(df: pd.DataFrame) -> pd.DataFrame:
    """TODO Sprint 2: implementar conforme as colunas da base simulada."""
    return df


def criar_alvo(df: pd.DataFrame) -> pd.DataFrame:
    """TODO Sprint 2: marcar 1 quando houver falha em até HORIZONTE_DIAS."""
    return df


def main() -> None:
    df = pd.read_parquet(DATA_PROCESSED / "base_tratada.parquet")
    df = criar_alvo(criar_features(df))
    df.to_parquet(DATA_PROCESSED / "base_features.parquet", index=False)
    print(f"Features criadas (horizonte de {HORIZONTE_DIAS} dias)")


if __name__ == "__main__":
    main()
