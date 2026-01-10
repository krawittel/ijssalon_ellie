mijn_dictionary = {
  "aardbei" : 3,
  "vanille" : 4,
  "chocolade" : 5 
}
aanbieding = mijn_dictionary["aardbei"] * 0.8
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts euro {aanbieding}")
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
print(reclame_tekst4)