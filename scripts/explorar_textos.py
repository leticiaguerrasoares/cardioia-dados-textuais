#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CardioIA - Fase 1 (Parte 2: Dados Textuais / NLP)
Exploracao inicial do corpus: contagem, vocabulario e termos mais frequentes.
Usa apenas a biblioteca padrao do Python 3 (sem dependencias externas).

Uso:
    python3 scripts/explorar_textos.py
"""
import os
import re
import glob
from collections import Counter

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")

# Stopwords minimas (PT + EN) para a estatistica de termos nao virar "the/de/and".
STOP = set("""
a o e de da do das dos que em um uma para com nao por os as no na se ao sua seu
mais como ser sao foi pode apos esta este seus suas pela pelo ou entre sobre quando
muito cada nos nas dos das seja ja tem tambem sem seu ella eles essa esse aos das dos
the of and to in is that as it be by for with was were are this his which from on or an at
not have has been they these their than which who will can may our we all one
""".split())

def carregar(caminho):
    txt = open(caminho, encoding="utf-8").read()
    # Remove o cabecalho de metadados (bloco entre linhas de '=') das ESTATISTICAS,
    # para nao "vazar" titulo/tema (label leakage). O arquivo entregue segue integro.
    delim = "=" * 80
    if delim in txt:
        txt = txt.split(delim)[-1]
    # Remove tambem o rodape de citacao (apos a linha de tracos), se houver.
    corte = txt.rfind("\n" + "-" * 80)
    if corte != -1:
        txt = txt[:corte]
    return txt

def tokens(texto):
    return [w for w in re.findall(r"[a-zA-Zà-úÀ-Ú]+", texto.lower()) if len(w) > 2]

def main():
    arquivos = sorted(glob.glob(os.path.join(DOCS, "*.txt")))
    if not arquivos:
        print("Nenhum .txt encontrado em docs/.")
        return

    total = Counter()
    print("=" * 72)
    print(f"{'ARQUIVO':52} {'PALAVRAS':>9} {'VOCAB':>7}")
    print("=" * 72)
    for f in arquivos:
        corpo = carregar(f)
        toks = tokens(corpo)
        total.update(w for w in toks if w not in STOP)
        vocab = len(set(toks))
        print(f"{os.path.basename(f):52} {len(toks):>9} {vocab:>7}")

    print("\n" + "-" * 72)
    print("20 termos mais frequentes no corpus (fora stopwords):")
    print("-" * 72)
    for termo, n in total.most_common(20):
        print(f"  {termo:20} {n:>6}")

    # Amostra de termos de interesse clinico (contagem insensivel a acento)
    import unicodedata
    def sem_acento(s):
        return "".join(c for c in unicodedata.normalize("NFD", s)
                       if unicodedata.category(c) != "Mn")
    total_norm = Counter()
    for termo, n in total.items():
        total_norm[sem_acento(termo)] += n
    alvo = ["heart", "blood", "pressure", "artery", "ventricle", "disease",
            "pain", "hypertension", "hipertensao", "pressao", "coracao", "tratamento"]
    print("\n" + "-" * 72)
    print("Ocorrencias de termos clinicos de interesse (acento-insensivel):")
    print("-" * 72)
    for t in alvo:
        print(f"  {t:16} {total_norm.get(sem_acento(t), 0):>6}")

if __name__ == "__main__":
    main()
