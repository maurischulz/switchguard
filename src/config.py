"""Caminhos e parâmetros do projeto SwitchGuard."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_SAMPLE = ROOT / "data" / "sample"
MODELS = ROOT / "models"
OUTPUT_POWERBI = ROOT / "outputs" / "powerbi"

# Horizonte de previsão (dias) - recalibrar quando a base simulada chegar
HORIZONTE_DIAS = 30

# Níveis de risco (limiares provisórios - calibrar na Sprint 2, priorizando recall)
LIMIAR_AMARELO = 0.30
LIMIAR_VERMELHO = 0.60

SEED = 42
