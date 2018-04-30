# Skriv en funktion upprepa(s,n) som skriver ut strängen s på skärmen n gånger, en gång per rad

def upprepa(s,n):
    # i kan du döpa till vad du vill, det är en "varvräknare" som börjar på 0. in range betyder för "i intervallet"

    """En funktion som upprepar strängen s för ett antal n gånger.""" #Detta är en docstring
    for i in range(0, n):
        print(s)

upprepa("Hej", 5)

# 2.Dokumentera funktionen upprepa(s,n)ovan med hjälp av en lämplig docstring

# skriv 3 citattecken följt av en beskrivning och stäng med 3 citatteckken


print (upprepa.__doc__)

#3.Gör ett dialogskript som ber användaren skriva in sin ålder i år och sedan skriver ut åldern i dagar på skärmen.

# AVKOMMENTERA DENNA FÖR ATT DEN SKA FRÅGA OM ÅLDER (TA BORT # FRÅN RADEN NEDAN)
# ålder = input("Skriv din ålder i år : ")

# inputen blev en sträng och du kan inte ta en sträng gånger ett tal så du får omvandla med int(detduvillomvandla)

#print(int(ålder)*365)

# Skriv en funktion räkna(symb,s) som returnerar antalet gånger som symbolen symb förekommer i strängen s.

fraser = ["hejsan", "svejsan", "tja"]

for hälsningar in (fraser):
    print(hälsningar)

def räkna(symb,s):
    counter = 0
    for letter in (s):
        if letter == symb:
            counter+=1



    return counter


print(räkna("s", "sofias snurr"))

#Skriv en funktion fib(n)som returnerar tal nummern i Fibonaccis talföljd 0,1,1,2,3,5,8,13,... där nästa tal fås genom att summera de båda föregående talen

# 5 8 13 21 34

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

############################

## bokstavligt talat en ordlista (dictionary)
ordlista = {
    "Ost" : "Cheese",
    "Hund" : "Dog",
    "Swag" : "Idiot"
}

##för att hämta ord använd funktionen "get" som alla dictionarys har

## hämtar motsvarande ord i ordlistan
print(ordlista.get("Ost"))
print(ordlista)

print("Nu har vi ändrat på den") #genom att "poppa" så tar vi bort det översta i listan, alltså har vi nu ändrat på dictionaryn
ordlista.pop("Ost") #vi behöver inte tilldela den igen genom att ta ordlista = ordlista.pop("Ost)
print(ordlista)

vårsträng = "en mening"
vårsträng.capitalize()
print (vårsträng)

## man kan alltså inte ändra direkt på strängen, du måste tilldela den igen
vårsträng = vårsträng.capitalize()
