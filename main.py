"""
Gerador de dataset simulado para galpão avícola.
Sensores: temperatura do ar, umidade relativa, amônia, temperatura de globo negro.
Índice calculado: ITGU (Buffington et al., 1981).
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# ── Configurações gerais ──────────────────────────────────────────────────────

SEMENTE_ALEATORIA = 42          # Para reprodutibilidade
DIAS              = 7
INTERVALO_MIN     = 15          # Leituras a cada 15 minutos
INICIO            = datetime(2025, 1, 1, 0, 0, 0)

# ── Parâmetros do ciclo diário de temperatura do ar ───────────────────────────

TEMP_MEDIA     = 27.0   # °C — média diária
TEMP_AMPLITUDE = 7.0    # °C — variação entre madrugada e tarde
HORA_PICO_TEMP = 14.5   # hora do pico de temperatura (14h30)

# ── Parâmetros do ciclo diário de umidade relativa ────────────────────────────

UR_MEDIA     = 70.0   # % — média diária
UR_AMPLITUDE = 20.0   # % — variação (inversa à temperatura)
# O pico de umidade ocorre no momento de menor temperatura (~3h da manhã)

# ── Parâmetros do globo negro ─────────────────────────────────────────────────

# O globo negro fica alguns graus acima da temperatura do ar (absorve radiação)
GLOBO_OFFSET    = 3.5   # °C acima da temp. do ar em média
GLOBO_AMPLITUDE = 2.0   # variação adicional de amplitude no ciclo do globo

# ── Parâmetros da amônia ──────────────────────────────────────────────────────

AMONIA_MEDIA    = 12.0   # ppm — nível típico em galpão
AMONIA_STD      = 2.5    # ppm — desvio do ruído aleatório

# ── Ruído dos sensores ────────────────────────────────────────────────────────

RUIDO_TEMP  = 0.4   # °C — desvio padrão do ruído de temperatura
RUIDO_UR    = 1.5   # % — desvio padrão do ruído de umidade
RUIDO_GLOBO = 0.5   # °C — desvio padrão do ruído do globo negro

# ── Eventos de estresse térmico ───────────────────────────────────────────────
# Cada evento: (dia_do_ciclo, hora_inicio, hora_fim, delta_temperatura_max)
# dia_do_ciclo: 0 = primeiro dia, 6 = último

EVENTOS_ESTRESSE = [
    {"dia": 2, "hora_ini": 12, "hora_fim": 16, "delta_temp": 7.0},  # Dia 3
    {"dia": 5, "hora_ini": 13, "hora_fim": 17, "delta_temp": 6.0},  # Dia 6
]


# ── Funções auxiliares ────────────────────────────────────────────────────────

def ciclo_senoidal(hora_decimal, media, amplitude, hora_pico):
    """
    Retorna o valor de uma variável climática num dado momento do dia,
    usando uma senoide com PICO em 'hora_pico' e mínimo 12h depois.
    Equivalente a: media + amplitude * cos(2π/24 * (hora - hora_pico))
    """
    return media + amplitude * np.sin(
        2 * np.pi / 24 * (hora_decimal - hora_pico) + np.pi / 2
    )


def ponto_orvalho(temp_ar, umidade_relativa):
    """
    Calcula temperatura de ponto de orvalho pela fórmula de Magnus aproximada.
    Referência: Lawrence (2005), American Meteorological Society.
    """
    a = 17.27
    b = 237.3  # °C

    gamma = np.log(umidade_relativa / 100.0) + (a * temp_ar) / (b + temp_ar)
    tpo   = (b * gamma) / (a - gamma)
    return tpo


def itgu(temp_globo_negro, temp_ponto_orvalho):
    """
    Índice de Temperatura de Globo Negro e Umidade.
    Fórmula: ITGU = tgn + 0,36 * tpo + 41,5
    Fonte: Buffington et al. (1981).
    """
    return temp_globo_negro + 0.36 * temp_ponto_orvalho + 41.5


def envelope_estresse(hora_decimal, hora_ini, hora_fim):
    """
    Curva suave (trapézio cossenoidal) para entrada e saída do evento de estresse.
    Evita degrau abrupto — o calor sobe e cai gradualmente em ~1h nas bordas.
    Retorna valor entre 0 e 1.
    """
    ramp = 1.0  # duração da rampa em horas
    if hora_decimal < hora_ini or hora_decimal > hora_fim:
        return 0.0
    elif hora_decimal < hora_ini + ramp:
        return 0.5 * (1 - np.cos(np.pi * (hora_decimal - hora_ini) / ramp))
    elif hora_decimal > hora_fim - ramp:
        return 0.5 * (1 - np.cos(np.pi * (hora_fim - hora_decimal) / ramp))
    else:
        return 1.0


# ── Geração do dataset ────────────────────────────────────────────────────────

def gerar_dataset():
    np.random.seed(SEMENTE_ALEATORIA)

    # Cria série de timestamps a cada 15 minutos por 7 dias
    total_leituras = DIAS * 24 * (60 // INTERVALO_MIN)
    timestamps = [INICIO + timedelta(minutes=i * INTERVALO_MIN) for i in range(total_leituras)]

    registros = []

    for ts in timestamps:
        dia_do_ciclo = (ts - INICIO).days          # 0 a 6
        hora         = ts.hour + ts.minute / 60.0  # hora decimal (ex: 14.5 = 14h30)

        # ── Temperatura do ar ──
        temp_base = ciclo_senoidal(hora, TEMP_MEDIA, TEMP_AMPLITUDE, HORA_PICO_TEMP)
        temp_ar   = temp_base + np.random.normal(0, RUIDO_TEMP)

        # ── Umidade relativa (inversamente proporcional à temperatura) ──
        # Pico de UR ocorre ~12h depois do pico de temperatura (hora oposta no ciclo)
        ur_base = ciclo_senoidal(hora, UR_MEDIA, -UR_AMPLITUDE, HORA_PICO_TEMP)
        ur      = ur_base + np.random.normal(0, RUIDO_UR)
        ur      = np.clip(ur, 30, 99)  # limita a faixa fisicamente plausível

        # ── Temperatura de globo negro ──
        globo_base = ciclo_senoidal(hora, TEMP_MEDIA + GLOBO_OFFSET,
                                    TEMP_AMPLITUDE + GLOBO_AMPLITUDE, HORA_PICO_TEMP)
        globo      = globo_base + np.random.normal(0, RUIDO_GLOBO)

        # ── Amônia ──
        amonia = max(0, np.random.normal(AMONIA_MEDIA, AMONIA_STD))

        # ── Aplica eventos de estresse térmico (se houver neste momento) ──
        for evento in EVENTOS_ESTRESSE:
            if dia_do_ciclo == evento["dia"]:
                fator = envelope_estresse(hora, evento["hora_ini"], evento["hora_fim"])
                if fator > 0:
                    delta = evento["delta_temp"] * fator
                    temp_ar += delta
                    globo   += delta * 1.2   # globo aquece ainda mais sob estresse
                    ur      -= delta * 1.5   # umidade cai com o calor extra
                    ur       = np.clip(ur, 30, 99)

        # ── Variáveis derivadas ──
        tpo      = ponto_orvalho(temp_ar, ur)
        valor_itgu = itgu(globo, tpo)

        registros.append({
            "timestamp":              ts.strftime("%Y-%m-%d %H:%M:%S"),
            "temperatura_ar":         round(temp_ar,  2),
            "umidade_relativa":       round(ur,        2),
            "amonia":                 round(amonia,    2),
            "temperatura_globo_negro": round(globo,    2),
            "ponto_orvalho":          round(tpo,       2),
            "itgu":                   round(valor_itgu, 2),
        })

    df = pd.DataFrame(registros)
    return df


# ── Execução principal ────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = gerar_dataset()

    caminho_saida = "dataset_avicola_simulado.csv"
    df.to_csv(caminho_saida, index=False)

    # Resumo rápido para conferência
    print(f"Dataset gerado: {len(df)} linhas × {len(df.columns)} colunas")
    print(f"Período: {df['timestamp'].iloc[0]}  →  {df['timestamp'].iloc[-1]}")
    print(f"\nEstatísticas descritivas:")
    print(df.drop(columns="timestamp").describe().round(2))
    print(f"\nArquivo salvo em: {caminho_saida}")
