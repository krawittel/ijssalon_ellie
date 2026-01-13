from algemene_functie import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro.")

def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro.")
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
totaal = inkomsten_totaal(dagelijkse_inkomsten)

def inkomsten_totaal_btw(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden.")
inkomsten_lijst = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return (f"De hoogste waarde is {hoogste} en de laagste waarde is {laagste}.")
fictieve_inkomsten = [220, 430, 125, 160, 205, 90, 345]


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde = totaal / aantal
    return (f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde} euro.")
fictieve_inkomsten = [220, 430, 125, 160, 205, 90, 345]

def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return (f"De hoogste en laagste waarden uit de lijst zijn: {resultaat}")
getallen = [10, 5, 3, 2, 1, 2, 9]

print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal(dagelijkse_inkomsten))
print(inkomsten_totaal_btw(inkomsten_lijst, btw))
print(laag_en_hoog(fictieve_inkomsten)) 
print(gemiddelde(fictieve_inkomsten))
print(meervoudig(getallen))

