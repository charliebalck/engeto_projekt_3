# engeto_projekt_3
Třetí projekt do Engeto Online Python Akademie
## Popis projektu
Tento projekt slouží k načtení výsledků z parlamentních voleb v roce 2017.
Odkaz k nahlédnutí [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102).
## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru `requirements.txt`.
Pro instalaci použijte nové virtuální prostředí s Python 3.12.0.
## Spuštení programu
Spuštění souboru `project_3.py` v příkazovém řádku požaduje dva povinné argumenty.

`python project_3.py -u "<odkaz-uzemniho-celku>" -f "<název-souboru.csv>"`

Výsledky se pak stáhnou jako soubor `.csv`.
## Ukázka projektu
Výsledky pro okres Beroun:
1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102`
2. argument: `beroun.csv`

Spuštění programu:

`python project_3.py -u "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" -f "beroun.csv"`

Průběh stahování:

`Stahuji data u url: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102`

`Ukládám stažená data do souboru: beroun.csv`

`Ukončuji progam`

Částečný výstup:
`code,location,registred,envelopes,valid,...
534421,Bavoryně,239,151,150,18,0,0,6,0,8,7,5,2,4,0,0,16,0,0,11,55,0,2,3,0,0,0,2,11,0
531057,Beroun,14804,9145,9076,1363,16,11,576,1,433,651,140,78,205,8,12,1290,4,6,641,2433,3,13,279,2,61,17,12,800,21
...`
