"""Etapa 1 - Leitura, limpeza e validação da base simulada.

Entrada: arquivos em data/raw/
Saída:   data/processed/base_tratada.parquet
"""
import pandas as pd

from src.config import DATA_RAW, DATA_PROCESSED


def carregar_base() -> pd.DataFrame:
    """Lê os arquivos da base simulada (ajustar quando a base for liberada)."""
    arquivos = sorted(DATA_RAW.glob("*.csv"))
    if not arquivos:
        raise FileNotFoundError(f"Nenhum CSV encontrado em {DATA_RAW}")
    return pd.concat((pd.read_csv(a) for a in arquivos), ignore_index=True)


def limpar(df: pd.DataFrame) -> pd.DataFrame:
    """TODO Sprint 2: tipos, datas, valores ausentes, duplicados e outliers."""
    return df.drop_duplicates()


def main() -> None:
    df = limpar(carregar_base())
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_parquet(DATA_PROCESSED / "base_tratada.parquet", index=False)
    print(f"Base tratada: {len(df):,} linhas")


if __name__ == "__main__":
    main()
