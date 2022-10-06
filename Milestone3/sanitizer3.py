
def ruler():
    print(9*"0"+10*"1"+10*"2"+10*"3"+10*"4"+10*"5"+"6")
    print(6*"1234567890")

def sanitize(toSan):
    signs = '<>();\\"\'-{}[]'
    toSan = toSan.strip()
    for chars in signs: #für alle teile von signs, do
        if(0!=toSan.count(chars)): #wenn die Zahl von chars in toSan nicht Null ist,
            print("Achtung! Der String enthält Sonderzeichen \"", chars, "\"  :", str(toSan.count(chars)).zfill(2)) #Sag mir die Zahl
    ruler()
    print("Der Eingangsstring lautete".ljust(49) + ':' + '\n' + toSan.ljust(60))  # Sag mir den Eingangsstring
    toSan = toSan.replace('<html>','      ')#destroy the tags vernichte html tags.
    toSan = toSan.replace('</html>','       ')
    for chars in signs: #für alle teile von signs, tu
        toSan = toSan.replace(chars,' ') #ersetze die Zeichen mit dem leeren String
    toSan = toSan.lower() #speichern als kleinbuchstaben.
    print('Der Sanitized String ist'.ljust(49) + ':' + '\n' + toSan[0].upper() + toSan[1:len(toSan)].ljust(59)) #sag mir was übrig bleibt
    ruler()
#The Strings to test
sanitize(" - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' ")

sanitize(' <html> ist eine tolle Sprache</html> ')

sanitize("Hacker schleusen auch gerne Code ein! test()")

sanitize(" ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!")

sanitize("Oder am Ende von Eingaben ")

sanitize('Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch)\n')

sanitize("<dieser String ist nun sanitized>")