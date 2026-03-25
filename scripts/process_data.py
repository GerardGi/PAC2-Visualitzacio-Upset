"""
Processament del Stack Overflow Developer Survey 2024
per generar la matriu binaria de llenguatges de programacio.

Requisits:
  - Python 3
  - Descarregar survey_results_public.csv de https://survey.stackoverflow.co/2024/
  - Posar-lo a la carpeta data/

Execucio:
  python scripts/process_data.py
"""

import csv
import os
from collections import Counter

# Configuracio
INPUT_FILE = os.path.join("data", "survey_results_public.csv")
OUTPUT_FILE = os.path.join("data", "languages_binary.csv")

# Els 7 llenguatges mes populars de l'enquesta 2024
TOP_LANGUAGES = ["JavaScript", "Python", "SQL", "TypeScript", "Java", "C#", "C++"]


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: no es troba {INPUT_FILE}")
        print("Descarrega'l de https://survey.stackoverflow.co/2024/")
        return

    print(f"Llegint {INPUT_FILE}...")
    respondents = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            langs = row.get("LanguageHaveWorkedWith", "")
            if langs and langs != "NA":
                lang_list = [l.strip() for l in langs.split(";")]
                respondents.append(lang_list)

    print(f"Total respostes amb dades de llenguatge: {len(respondents)}")

    # Comptar popularitat individual
    print("\nPopularitat individual:")
    for lang in TOP_LANGUAGES:
        count = sum(1 for r in respondents if lang in r)
        pct = count * 100 / len(respondents)
        print(f"  {lang}: {count} ({pct:.1f}%)")

    # Generar matriu binaria
    print(f"\nGenerant matriu binaria amb {len(TOP_LANGUAGES)} llenguatges...")
    rows_out = []
    for i, lang_list in enumerate(respondents):
        binary = {}
        for tl in TOP_LANGUAGES:
            binary[tl] = 1 if tl in lang_list else 0
        if sum(binary.values()) > 0:
            binary["name"] = f"dev_{i+1:05d}"
            rows_out.append(binary)

    print(f"Respostes amb almenys 1 dels top {len(TOP_LANGUAGES)}: {len(rows_out)}")

    # Escriure CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name"] + TOP_LANGUAGES
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows_out:
            writer.writerow(row)

    print(f"Fitxer escrit: {OUTPUT_FILE}")

    # Calcular i mostrar les 25 interseccions mes grans
    print("\nTop 25 interseccions:")
    intersection_counter = Counter()
    for row in rows_out:
        key = tuple(sorted(k for k in TOP_LANGUAGES if row[k] == 1))
        intersection_counter[key] += 1

    for combo, count in intersection_counter.most_common(25):
        pct = count * 100 / len(rows_out)
        print(f"  {' + '.join(combo)}: {count} ({pct:.1f}%)")


if __name__ == "__main__":
    main()
