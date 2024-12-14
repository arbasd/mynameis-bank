import random
 
def ivesti_info(ko_prasoma):
    prasymas = ''
 
    if ko_prasoma.lower() == "vardas":
        prasymas = "vardą"
    else:
        prasymas = "pavardę"
 
    while True:
        zodis = input(f"Įveskite savo {prasymas}: ")
        if zodis.isalpha():
            zodis = zodis.capitalize()
            break
        print("Jūsų įvestis gali būti sudaryta tik iš raidžių!")
 
    return zodis
 
def patikrinti_balansa():
    print(f"Jūsų banko balansas yra: {banko_balansas}")
 
def ideti_pinigu():
    global banko_balansas
    pasirinkimas = input("1. Isideti pinigu \n 2. Gryzti i meniu\n")
    if pasirinkimas == "2":
        grizti_i_meniu()   
    while True:
        idejimas = input("Kiek norėtumėte įsidėti pinigų? ")
 
        if idejimas.isnumeric():
            idejimas = float(idejimas)
            break
        print("Neteisinga įvestis (privalo būti teigiamas skaičius)")
 
    banko_balansas += idejimas
    print(f"Jūs sėkmingai įsidėjote {idejimas} eurų.")
 
def isgryninti_pinigu():
    global banko_balansas
    pasirinkimas = input("1. Issigryninti pinigu \n 2. Gryzti i meniu\n")
    if pasirinkimas == "2":
        grizti_i_meniu()   
    while True:
        isemimas = input("Kiek norėtumėte išsigryninti pinigų? ")
 
        if isemimas.isnumeric():
            isemimas = float(isemimas)
            break
        print("Neteisinga įvestis (privalo būti teigiamas skaičius)")
 
 
    banko_balansas -= isemimas
    print(f"Jūs sėkmingai išsigryninote {isemimas} eurų")
 
def pakeisti_varda_pavarde():
    global banko_balansas
    global vartotojas_vardas
    global vartotojas_pavarde
    sprendimas = input("Šis veiksmas kainuos 50 eurų. Ar norite tęsti?\n1. Tęsti\n2. Grįžti\n")
    if sprendimas == "1":
        if banko_balansas >= 50:
            banko_balansas -= 50
            vartotojas_vardas = ivesti_info("vardas")
            vartotojas_pavarde = ivesti_info("pavarde")
        else:
            print("Nepakankama liesu!")
    else:
        grizti_i_meniu()

def investuoti():
    print("Pasirinkite investavimo buda:")
    print("1. Kriptovaliutos (Auksta rizika)")
    print("2. Akcijos (Maža rizika)")
    print("3. grizti i meniu...")
    if pasirinkimas == "3":
        grizti_i_meniu()
    while pasirinkimas not in ("1","2"): 
        print("Neteisingas pasirinkimas! turite pasirinkti 1 arba 2!")
        print("Pasirinkite investavimo buda:")
        print("1. Kriptovaliutos (Auksta rizika)")
        print("2. Akcijos (Maža rizika)")
        pasirinkimas = input()
    while True:
        investicija = input("Kiek noretumete investuoti?")

        if not investicija.isnumeric():
          print("Neteisinga įvestis (privalo būti teigiamas skaičius)")

        investicija = float(investicija)

        if banko_balansas < investicija:
            print("Nepakanka lesu!")
            continue
        
        banko_balansas -= investicija
        break
       
    if pasirinkimas == "1":
        random_skaicius = random.randint(1,100)

        if random_skaicius <= 35:
            banko_balansas += investicija * 3
            print(f"Jus sekmingai patrigubinote savo investicija! dabartinis balansas {banko_balansas}")
        else:
            print(f"Jūs nesekmingai patrigubinote savo investicija! dabartinis balansas {banko_balansas}")
def grizti_i_meniu():
    print("griztama i meniu")
    pagrindine()
    
 

banko_balansas = 100
vartotojas_vardas = ivesti_info("vardas")
vartotojas_pavarde = ivesti_info("pavarde")
 
def pagrindine():
    while True:
        pasirinkimas = input(f"Gerb. {vartotojas_vardas} {vartotojas_pavarde}, pasirinkite: \n1. Patikrinti banko balansą. \n2. Įsidėti pinigų į banką.\n3. Išsigryninti pinigus.\n4. Pasikeisti vardą ir pavardę.\n5. Investuoti.\n")
 
        match pasirinkimas:
            case "1":
                patikrinti_balansa()
            case "2":
                ideti_pinigu()
            case "3": 
                isgryninti_pinigu()
            case "4":
                pakeisti_varda_pavarde()
            case "5":
                investuoti()
 
 
if __name__ == "__main__":
    pagrindine()