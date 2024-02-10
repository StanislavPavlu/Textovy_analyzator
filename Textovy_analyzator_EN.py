# Identifikace:
"""
Textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Stanislav Pavlů
email: standic@seznam.cz
discord: Standa P. (standa_40063)
"""

# Texty na výběr (list):
TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Seznam uživatelů:
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

caradvoj_kratka = 35*"="
carajedno_kratka = 35*"-"
caradvoj_dlouha = 50*"="
carajedno_dlouha = 50*"-"

# Přihlášení uživatele - zadání údajů:
print(f"{caradvoj_kratka}\nTEXT ANALYZER\n{caradvoj_kratka}")
jmeno = input(f"Enter your username:\n")
print(carajedno_kratka)
heslo = input(f"Enter your password:\n")
print(caradvoj_dlouha)

# Přihlášení uživatele - vyhodnocení zadaných údajů:
if uzivatele.get(jmeno) == heslo:
    print(f"Welcome to the TEXT ANALYZER application, {jmeno}.")
else:
    print("Incorrect user name or password.\nThe program will be terminated.")
    print(caradvoj_dlouha)
    exit()

# Výběr jednoho z textů:
print(f"Select one of the texts to analyze and enter its number:\n{carajedno_dlouha}")
for poradi, text in enumerate(TEXTS, 1):
    print(f"{poradi}:\n\n{text}\n{carajedno_dlouha}")

pripustne_vstupy = []
for dvojice in enumerate(TEXTS, 1):
    pripustne_vstupy.append(dvojice[0])
    # print(pripustne_vstupy)

vybrany_text = input()
if vybrany_text.isnumeric():
    vybrany_text = int(vybrany_text)
    if vybrany_text in pripustne_vstupy:
        TEXT_FINAL_LIST = TEXTS[vybrany_text - 1].split( )
    else:
        print(caradvoj_dlouha)
        print(f"Input '{vybrany_text}' is incorrect.\nInput needs to be number between {pripustne_vstupy[0]} and {pripustne_vstupy[-1]}.\nThe program will be terminated.")
        print(caradvoj_dlouha)
        exit()
else:
    print(caradvoj_dlouha)
    print(f"Input '{vybrany_text}' is incorrect.\nInput needs to be number between {pripustne_vstupy[0]} and {pripustne_vstupy[-1]}.\nThe program will be terminated.")
    print(caradvoj_dlouha)
    exit()
# print(TEXT_FINAL_LIST)    # Kontrolní print

# Záhlaví vyhodnocení:
print(caradvoj_dlouha)
print(f"TEXT ANALYSIS OF TEXT NR. {vybrany_text}:")
print(caradvoj_dlouha)

# Analyzované parametry textu:
# Počet slov textu:
pocet_slov = len(TEXT_FINAL_LIST)
print(f"Number of words in text: {pocet_slov}\n{carajedno_dlouha}")

pocet_slov_Title = 0    # Počet slov začínajících velkým písmenem:
pocet_slov_UPPER = 0    # Počet slov psaných velkými písmeny:
pocet_slov_lower = 0    # Počet slov psaných malými písmeny:
pocet_cisel = 0         # Počet čísel:
soucet_cisel = 0        # Součet všech čísel:
delky_slov = []

for slovo in TEXT_FINAL_LIST:
    if slovo.istitle() and slovo[0].isalpha:
        pocet_slov_Title += 1
        if slovo.isupper() and slovo.isalpha:
            pocet_slov_UPPER += 1
    elif slovo.islower() and slovo.isalpha:
        pocet_slov_lower += 1
    elif slovo.isnumeric():
        pocet_cisel += 1
        slovo = int(slovo)
        soucet_cisel += slovo
    
print(f"Number of titlecase words: {pocet_slov_Title}\n{carajedno_dlouha}")
print(f"Number of uppercase words: {pocet_slov_UPPER}\n{carajedno_dlouha}")
print(f"Number of lowercase words: {pocet_slov_lower}\n{carajedno_dlouha}")       
print(f"Number of numeric strings: {pocet_cisel}\n{carajedno_dlouha}")      
print(f"The sum of all the numbers: {soucet_cisel}\n{carajedno_dlouha}")        

# Četnost délek slov:
for slovo in TEXT_FINAL_LIST:
    ciste_slovo = slovo.strip(".,!? ")
    delky_slov.append(len(ciste_slovo))
vycet_delek_slov = set(delky_slov)

print("Occurrences of word lengths:")
print("+---------------------------------------+")
print(f"| LEN\t| OCCURRENCES\t\t| NR.\t|")
print("+---------------------------------------+")
for cislo in vycet_delek_slov:
    cetnost = delky_slov.count(cislo)
    print(f"| {cislo}\t| {cetnost * '*': <20}\t| {cetnost}\t|")
print("+---------------------------------------+")
print(caradvoj_dlouha)


