# Identifikace:
"""
Textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Stanislav Pavlů
email: standic@seznam.cz
discord: Standa P. standa_40063
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

# Přihlášení uživatele - zadání údajů:
print(35*"=")
print("TEXT ANALYZER")
print(35*"=")
jmeno = input("Enter your username:\n")
print(35*"-")
heslo = input("Enter your password:\n")
print(50*"=")

# Přihlášení uživatele - vyhodnocení zadaných údajů:
if uzivatele.get(jmeno) == heslo:
    print(f"Welcome to the TEXT ANALYZER application, {jmeno}.")
else:
    print("Incorrect user name or password, the program will be terminated.")
    print(50*"=")
    exit()

# Výběr jednoho z textů:
pripustne_vstupy = ("1", "2", "3")
print("Select one of the texts to analyze and enter its number:")
print(50*"-")
print(pripustne_vstupy[0] + "\n\n" + TEXTS[0])
print(50*"-")
print(pripustne_vstupy[1] + "\n\n" + TEXTS[1])
print(50*"-")
print(pripustne_vstupy[2] + "\n\n" + TEXTS[2])
print(50*"-")

vybrany_text = input()
if vybrany_text == pripustne_vstupy[0]:
    TEXT_FINAL_LIST = TEXTS[0].split( )
elif vybrany_text == pripustne_vstupy[1]:
    TEXT_FINAL_LIST = TEXTS[1].split( )
elif vybrany_text == pripustne_vstupy[2]:
    TEXT_FINAL_LIST = TEXTS[2].split( )
else:
    print(50*"=")
    print(f"'{vybrany_text}' input is incorrect, the program will be terminated.")
    print(50*"=")
    exit()
# print(TEXT_FINAL_LIST)    # Kontrolní print

# Záhlaví vyhodnocení:
print(50*"=")
print(f"TEXT ANALYSIS OF TEXT NR. {vybrany_text}:")
print(50*"=")

# Analyzované parametry textu:
# Počet slov textu:
pocet_slov = len(TEXT_FINAL_LIST)
print("Number of words in text:", pocet_slov)
print(50*"-")

# Počet slov začínajících velkým písmenem:
pocet_slov_Title = 0
for slovo in TEXT_FINAL_LIST:
    if slovo.istitle():
        pocet_slov_Title += 1
        # print(slovo)      # Kontrolní print selektovaných slov
print("Number of titlecase words:", pocet_slov_Title)
print(50*"-")

# Počet slov psaných velkými písmeny:
pocet_slov_UPPER = 0
for slovo in TEXT_FINAL_LIST:
    if slovo.isupper():
        pocet_slov_UPPER += 1
        # print(slovo)      # Kontrolní print selektovaných slov
print("Number of uppercase words:", pocet_slov_UPPER)
print(50*"-")

# Počet slov psaných malými písmeny:
pocet_slov_lower = 0
for slovo in TEXT_FINAL_LIST:
    if slovo.islower():
        pocet_slov_lower += 1
        # print(slovo)      # Kontrolní print selektovaných slov
print("Number of lowercase words:", pocet_slov_lower)       
print(50*"-")

# Počet čísel:
pocet_cisel = 0
for slovo in TEXT_FINAL_LIST:
    if slovo.isnumeric():
        pocet_cisel += 1
        # print(slovo)      # Kontrolní print selektovaných čísel
print("Number of numeric strings:", pocet_cisel)      
print(50*"-")

# Součet všech čísel:
soucet_cisel = 0
for slovo in TEXT_FINAL_LIST:
    if slovo.isnumeric():
        slovo = int(slovo)
        soucet_cisel += slovo
        # print(slovo)      # Kontrolní print selektovaných čísel
print("The sum of all the numbers:", soucet_cisel)        
print(50*"-")

# Četnost délek slov:
# Převod listu se slovy vybraného textu na list s délkou
# jednotlivých slov tohoto textu (slova očištěna od diakritiky)
delky_slov = []
for slovo in TEXT_FINAL_LIST:
    ciste_slovo = slovo.strip(".,!? ")
    delky_slov.append(len(ciste_slovo))
# print(delky_slov)         # Kontrolní print listu

# Převod listu s délkou jednotlivých slov vybraného textu
# na set s výčtem všech vyskytujících se délek slov
vycet_delek_slov = set(delky_slov)
# print(vycet_delek_slov)   # Kontrolní print setu

print("Occurrences of word lengths:")
print("+---------------------------------------+")
print(f"| LEN\t| OCCURRENCES\t\t| NR.\t|")
print("+---------------------------------------+")
for cislo in vycet_delek_slov:
    cetnost = delky_slov.count(cislo)
    print(f"| {cislo}\t| {cetnost * '*': <20}\t| {cetnost}\t|")
print("+---------------------------------------+")
print(50*"=")


