# UpSet Plot — Stack Overflow Developer Survey 2024

Visualització interactiva de les combinacions de llenguatges de programació més populars, basada en les respostes de 57.321 desenvolupadors de l'[Stack Overflow Annual Developer Survey 2024](https://survey.stackoverflow.co/2024/).

Treball realitzat per a la PAC 2 de l'assignatura de Visualització de Dades.

## Descripció

L'enquesta del Stack Overflow 2024 pregunta als desenvolupadors quins llenguatges han usat extensivament durant l'últim any, permetent seleccions múltiples. He agafat els 7 llenguatges més populars (JavaScript, Python, SQL, TypeScript, Java, C#, C++) i he analitzat com es combinen entre ells amb un diagrama UpSet.

## Estructura del repositori

```
├── index.html                  ← Visualització (GitHub Pages)
├── data/
│   ├── survey_results_public.csv    ← Dataset original SO 2024 (no inclòs per mida, descarregar de la font)
│   └── languages_binary.csv         ← Matriu binària generada
├── scripts/
│   └── process_data.py              ← Script de processament de dades
└── README.md
```

## Fonts de dades

- **Dataset**: Stack Overflow Annual Developer Survey 2024
- **URL**: https://survey.stackoverflow.co/2024/
- **Llicència**: Open Database License (ODbL)
- **Descàrrega**: El CSV original (`survey_results_public.csv`) es pot descarregar directament des de la pàgina de l'enquesta. No l'he inclòs al repositori per la seva mida (~90MB).

## Com s'han processat les dades

El script `scripts/process_data.py` fa el següent:

1. Llegeix el CSV original de l'enquesta (`survey_results_public.csv`)
2. Extreu la columna `LanguageHaveWorkedWith` (llista de llenguatges separats per `;`)
3. Selecciona els 7 llenguatges més populars
4. Genera una matriu binària (1 = l'enquestat usa el llenguatge, 0 = no)
5. Calcula les interseccions i les ordena per mida

Per reproduir el processament:

```bash
# Descarregar l'enquesta de https://survey.stackoverflow.co/2024/
# Descomprimir i posar survey_results_public.csv a data/
python scripts/process_data.py
```

## Tècnica: UpSet Plot

L'UpSet Plot va ser creat el 2014 per Alexander Lex, Nils Gehlenborg, Hendrik Strobelt, Romain Vuillemot i Hanspeter Pfister (Universitat de Harvard).

- **Paper**: Lex, A. et al. *UpSet: Visualization of Intersecting Sets.* IEEE TVCG (InfoVis), 20(12):1983-1992, 2014.
- **DOI**: 10.1109/TVCG.2014.2346248
- **Web oficial**: https://upset.app/
