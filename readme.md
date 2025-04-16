# Hänga Gubbe-spel

## Beskrivning
Detta är ett enkelt Hänga Gubbe-spel byggt med Python och Tkinter. I detta mycket klassiska spel ska spelaren försöka gissa ett hemligt ord, en bokstav i taget. För varje felaktig gissning kommer spelaren ett steg närmare att förlora (bli hängd). Spelet är slut när när spelaren antingen har gissat det hemliga ordet eller haft för många chanser på sig.

## Funktioner
- Slumpmässigt valda ord från en fördefinierad lista.
- Ett enkelt grafiskt gränssnitt.
- Omedelbar återkoppling på en gissning.
- Visar status, vinster och förluster.
- Begränsat till 6 felgissningar innan spelet är över.

## Så spelar du
1. Starta applikationen.
2. Ett slumpmässigt ord väljs och varje bokstav i ordet visas som understreck.
3. Skriv in en bokstav i textrutan.
4. Klicka på knappen "Gissa".
5. Om din gissning är rätt visas bokstaven i ordet.
6. Om den är felaktig ökar antalet felgissningar med ett.
7. Fortsätt gissa tills du antingen:
   - Lyckas gissa alla bokstäver i ordet - vinst.
   - Gör sex felaktiga gissningar - förlust.

## Systemkrav
- Python 3.x
- Tkinter

## Installation och start
1. Klona eller ladda ner Hangman.py
2. Starta spelet genom att skriva:

python Hangman.py

## Framtida förbättringar
- Visa en gubbe och en stolpe istället för understreck.
- Hämta ord från en AI eller annan källa.
- Implementera olika svårighetsgrader.
- Implementera "leveling" så att svårighetsgraden ökar utifrån spelarens förmåga. 
- Lägg till en "Starta om"-knapp.