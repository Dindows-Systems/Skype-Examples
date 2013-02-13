
SkypeTalking

Version 0.8

Copyright (c) 2010 SkypeTalk Team

Projektets netsted: http://skypetalking.googlecode.com

1. Indledning

SkypeTalking er et program, der gør det populære program Skype, der bruges til internet-telefoni, mere tilgængeligt og nemmere at bruge for blinde. Programmet benytter Skype API Wrapper og punktskrift samt talen fra din skærmlæser til at finde informationerne fra Skype og sende informationen til din skærmlæser. SkypeTalking videregiver de fleste statusmeldinger fra Skype såsom ændring af en brugers status, indgående og udgående chatbeskeder, status for opkald og meget mere! Skypetalking får kort sagt Skype til at tale!

Programmet SkypeTalking er først og fremmest udviklket med det formål at gøre Skype mere brugbart med skærmlæseren NVDA, der er gratis og open source. Men JAWS, Window-eyes, System Access og SAPI5 tale er også understøttet. Når du benytter SAPI5, har du blot ikke mulighed for at udnytte punktskrift.

1.1. Systemkrav  

For at kunne bruge SkypeTallking, skal du have følgende:
* Windows 2000, XP, VISTA eller 7
* En af de understøttede skærmlæsere: I øjeblikket omfatter dette NVDA 2010.1 eller nyere, JAWS (alle versioner), Window_Eyes (alle versioner) eller System Access (alle versioner) herunder System Access to Go.
* Hvis du ikke bruger en af de understøttede skærmlæsere, bruges talen via en SAPI5 talesyntese i stedet. Hertil behøves en talesyntese, der er kompatibel med SAPI5 (Windows-systemer leveres med mindst 1 SAPI5 talesyntese)
* Herudover skal du naturligvis have selve Skype-programmet (3.x, 4.x eller nyere) - fungerer sandsynligvis også med Skype 2.x og muligvis med version 1.x. Dette er dog ikke blevet testet.

2. Anvendelse af programmet

2.1. Installation og første afvikling

Du installerer SkypeTalking ved at køre skypetalking_setup.exe og følge instruktionerne. Under installationen oprettes et ikon på Skrivebordet, en programgruppe i Start menuen samt installationsmappen x:\SkypeTalking, hvor "x" er bogstavet på din computers systemdrev.
SkypeTalking afinstalleres ved først at åbne programgruppen SkypeTalking i menuen Start og vælge "Uninstall SkypeTalking".
Du starter SkypeTalking ved at klikke på ikonet SkypeTalking enten fra Skrivebordet eller fra punktet SkypeTalking i Start-menuen under Programmer\SkypeTalking.
Første gang du starter SkypeTalking, er programmet med stor sandsynlighed ikke godkendt til at kommunikere med Skype. Af sikkerhedshensyn tillader Skype ikke tredjeparts-pluins eller ekstraprogrammer at kommunikere med Skype uden forudgående godkendelse af brugeren. Dette gøres for at undgå, at vira eller trodjanske heste forårsager skader på Skype. Gør følgende for at give SkypeTalking adgang til Skype:
1. Start SkypeTalking enten fra Skrivebordet eller fra menuen Start under Programmer>SkypeTalking. Du hører dernæst "Forbinder til Skype".
2. Åbn Skype.
3. Gå nu til menulinjen, vælg Funktioner og bevæg dig med piletasterne til Indstillinger og tryk Enter.
4. Vælg nu kategorien Avanceret ved hjælp af pil ned.
5. Tryk Shift+Tab flere gange indtil du når punktet "Håndter andre programmers adgang til Skype", som er et link. Tryk mellemrum for at aktivere linket. 
6. Find skypeTalking i listen (det er sædvanligvis det første punkt), tryk Tab til du når knappen "ændre" og tryk Mellemrum for at aktivere den.
Tryk Tab. Du hører nu, at du står på en radioknap, hvor der står: "Giv ikke dette program adgang til Skype". Tryk Pil Op indtil du hører: "Giv dette program adgang til Skype" og tryk Enter.
8. Sådan! Du har netop givet SkypeTalking lov til at bruge Skype. Du hører nu SkypeTalkings velkomstbesked. Du kan nu forlade Indstillinger ved at trykke flere gange på Escape. Du behøver ikke engang at gemme dine ændringer.
OBS: Hver gang du geninstallerer SkypeTalking skal du gentage disse trin. Men bare rolig! Du skal kun gøre det én gang pr. SkypeTaling-installation. Du skal ligeledes gøre det, hvis du ændrer den placering, hvor SkypeTalking.exe ligger.


2.2. Anvendelse

Når SkypeTalking er startet, kører det i baggrunden og annoncerer begivenheder, indtil det afsluttes. SkypeTalking rummer en lang række kommandoer, der er forbundet til genvejstaster og som bruges til at styre, hvordan programmet fungerer og til at få bestemte informationer læst op eller gentaget. Alle SkypeTalkings genvejstaster bruges sammen med tasterne Alt, ctrl og Shift (Alt+Ctrl+Shift+Noget andet). Vi siger derfor, at Alt+Ctrl+Shift fungerer som SkypeTalking-tast. En kommando udføres derfor ved at holde Alt+Ctrl+Shift (SkypeTalking-tast) nede, mens en yderligere tast trykkes.
OBS: Du kan ændre alle SkypeTalkings genvejstaster efter behov ved at åbne filen SkypeTalking.ini, som findes i SkypeTalking-mappen. Denne mulighed anbefales dog kun for øvede brugere for øjeblikket.

I de følgende afsnit beskrives alle SkypeTalkings kommandoer og deres brug.

 
3. Kommandoerne

3.1. Læse Skype chatbeskeder

3.1.1. Sig seneste 10 indgående/udgående chatbeskeder (Alt+Ctrl+Shift+tallene 1 til og med 0)

Du kan læse de sidste indgående og udgående chatbeskeder (1 til og med 10), som du har sendt eller modtaget i løbet af den aktuelle SkypeTalking session ved at trykke Alt+Ctrl+Shift+tallene 1 til og med 0 på et alfanumerisk tastatur. Hvis et tal trykkes ned 2 gange, kopieres den tilknyttede besked til udklipsholderen. Trykkes det 3 gange, åbnes en web-adresse i din standard-browser, hvis den pågældende besked indeholder en web-adresse.

3.1.2. Overvåge aktive chats (Alt+Ctrl+Shift+Funktionstast F1 til og med F10)

Denne funktion giver mulighed for at overvåge aktive chats dvs. de åbne chatvinduer. Det er nyttigt, hvis du ønsker at læse de seneste 10 chatbeskeder i en bestemt chat i stedet for de nyeste chatbeskeder, du har modtaget fra alle chats. Benyt Alt+Ctrl+Shift+Funktionstasterne F1 til og med F10 til at sætte en overvågning på en chat op til 10 chats eller tryk 2 gange for at sætte fokus til det pågældende chatvindue), hvorefter du med Alt+Ctrl+Shift+tallene kan læse  de 10 nyeste chatbeskeder i den aktuelt overvågede chat. Når du trykker Alt+Ctrl+Shift+C, hører du, hvilken chat du netop nu overvåger. Trykker du kommandoen 2 gange, bringes fokus til den pågældende chat.

3.1.3. Gentag seneste chatbesked (Alt+Ctrl+Shift+R)
 

Denne kommando gentager den seneste indgående eller udgående chatbesked. Hvis kommandoen trykkes 2 gange, åbnes et Skype chatvindue tilknyttet denne besked samtidig med, at overvågning sættes til den pågældende chat.

3.2. Gentag seneste begivenhed (Alt+Ctrl+Shift+E)

Denne kommando gentager den seneste Skype begivenhed herunder chatbeskeder. De begivenheder, som kan blive læst op igen ved hjælp af denne kommando, omfatter statusskift, seneste chatbesked og status for samtaler.

3.3. Ignorér Skype-begivenheder (Alt+Ctrl+Shift+I)

Denne kommando bruges til at slå ignorering af Skype-begivenheder til og fra. Hvis funktionen er slået til, ignorerer SkypeTalking alle begivenheder og vil hverken annoncere eller huske dem.

3.4. Løbende ændre din status på Skype (Alt+Ctrl+Shift+Backspace)

Denne kommando bruges til skift af Skype-status imellem online, ikke tilstede, ikke tilgængelig, vil ikke forstyrres osv. Din status ændres 1 sekund efter, at du har trykket kommandoen.

3.5. Sig samtales varighed (Alt+Ctrl+Shift+D)

Kommandoen virker under en samtale. Den vil annoncere varigheden af den igangværende samtale i timer/minutter/sekunder.

3.6. Sig status for den igangværende filoverførsel (Alt+Ctrl+Shift+F)

Denne kommando vil oplyse status for den seneste indgående eller udgående filoverførsel. Hvis den pågældende filoverførsel er i gang, oplyses ligeledes overførselshastigheden i megabytes pr. sekund samt antal megabytes, der allerede er overført.

3.7. Oplys din aktuelle online-status eller saldo (Alt+Ctrl+Shift+O)

Første gang denne kommando udføres, oplyses din aktuelle online-status. Hvis du trykker kombinationen 2 gange, oplyses din Skypekredit saldo.

3.8. Oplæs eller skift din Skype humørbesked (Alt+Ctrl+Shift+M)

Hvis du har angivet en humørbesked på Skype, bruges denne kommando til at få læst den op. Hvis du trykker den 2 gange, fremkommer en dialogboks, hvor du kan indtaste en humørbesked. Du indtaster din tekst og afslutter med Enter. Derefter ændres din humørbesked.

3.9. andre kommandoer

3.9.1. Dialogboksen Om SkypeTalking (Alt+Ctrl+Shift+A)

Der fremkommmer en dialogboks med oplysninger om den aktuelle version af SkypeTalking, information om copyright, information om webstedet osv. Du lukker dialogboksen ved at trykke Enter. 

3.9.2. Oplys Skype-version (Alt+Ctrl+Shift+V)

Denne kommando oplyser, hvilken version af Skype der i øjeblikket er installeret på brugerens computer. Hvis den trykkes 2 gange, oplyses hvilken version af Skype Wrapper API, der er installeret (hovedsageligt nyttig for udviklere).

3.9.3. Stop SAPI5-tale (Alt+Ctrl+Shift+Mellemrum)

Denne kommando standser talen, når SkypeTalking benytter SAPI5-tale. Hvis du bruger SkypeTalking sammen med din skærmlæser, kan du stoppe talen på normal vis med Ctrl-tasten.

3.9.4. Afslut SkypeTalking (Alt+Ctrl+shift+Q)

Denne kommando udlæser SkypeTalking fra hukommelsen. Du vil som standard blive bedt om at bekræfte. Hvis du svarer ja, udlæses SkypeTalking og alle nye begivenheder, igangværende filoverførsler og chatbeskeder slettes, fordi Skypetalking holder styr på dem i computerens hukommelse. Hvis du svarer nej, fortsætter SkypeTalking med at køre i sin igangværende session.

4. Dialogboksen Indstillinger

Dialogboksen med SkypeTalkings indstillinger startes ved at trykke Alt+Ctrl+Shift+P. Herfra kan du ændre SkypeTalkings virkemåde, standardsprog samt output. Dialogboksen Indstillinger indeholder 3 faneblade (Generel, Output og meldinger), som du kan skifte imellem ved hjælp af de sædvanlige Windows genvejstaster Ctrl+tab og Ctrl+Shift+Tab.

4.1. Fanebladet Generel

Fanebladet Generel i SkypeTalkings indstillings-dialogboks har følgende indstillingsmuligheder.

4.1.1. Sprog

Combo-boksen Sprog viser alle de tilgængelige sprog, som SkypeTalking i øjeblikket understøtter. Her kan du vælge dit foretrukne sprog, og dit valg får omgående virkning, så snart du har gemt dine valg. Som standard bruger SkypeTalking sproget i dit operativsystem.

4.1.2. Start Skype automatisk, hvis programmet ikke allerede kører

Hvis denne indstilling er slået til, starter SkypeTalking automatisk selve Skype-programmet, hvis du har glemt at starte Skype, før du startede SkypeTalking. Det kan også være nyttigt, hvis du har brug for at få øjeblikkelig tale på Skype. Indstillingen er slået til som standard, hvilket betyder at SkypeTalking starter Skype, hvis Skype ikke allerede kører.

4.1.3. Bekræft inden afslutning af SkypeTalking

Indstillingen er slået til som standard. Hvis du slår den fra, udlæses SkypeTalking øjeblikkelig, så snart kommandoen for at afslutte udføres og meddelelsen til bekræftelse springes over.

4.1.4. Når SkypeTalking afsluttes skal Skype ligeledes afsluttes

Indstillingen er selvforklarende. Den er slået til som standard dvs. at SkypeTalking vil afslutte Skype, når du afslutter SkypeTalking. Du bør derfor slå indstillingen fra, hvis du ønsker at bruge Skype, når du har afsluttet SkypeTalking.

4.2. Fanebladet Output

Fanebladet Output rummer indstillinger, der har med output via tale og punktskrift at gøre. Herfra kan du justere følgende indstillinger.

4.2.1. Tale-output

Denne combo-boks giver dig mulighed for at vælge, hvor taleoutput skal foretages. Hvis du vælger Find Automatisk, bruges din nuværende skærmlæser eller SAPI5, hvis der ikke kører nogen skærmlæser, eller hvis SkypeTalking ikke understøtter din skærmlæser. Hvis du vælger SAPI5, bruger SkypeTalking automatisk den SAPI5-talesyntese, der er valgt som standard på dit system og ignorerer din skærmlæser.

4.2.2. SAPI5 indstillingsmuligheder

De efterfølgende 3 kontroller er redigerings-spinbokse til styring af lydstyrke og talehastighed for din SAPI5 talesyntese. De får virkning, hvis du har valgt SAPI5. Du kan enten ændre værdierne ved hjælp af piletasterne eller ved at skrive den ønskede værdi med tal.

4.2.3. Slå visning i punktskrift til

Med denne tjekboks får du mulighed for at få SkypeTalkings output vist på dit punktdisplay. Denne indstilling virker ikke, når du bruger SAPI5 til taleoutput.

4.3. Fanebladet Meldinger

I dette faneblad kan du slå annoncering af de forskellige Skype-meldinger, der i øjeblikket understøttes af SkypeTalking, til og fra. Alt, hvad der ikke er markeret/afkrydset her, ignoreres af SkypeTalking. Du kan ændre annoncering af indgående chats, udgående chats, onlien status osv.

5. Kontaktpersoner (Contacts Manager)

SkypeTalkings Contacts Manager giver dig mulighed for at administrere dine Skype-kontaktpersoner på en nemmere og mere tilgængelig måde. Du åbner manageren med genvejstasten Alt+Ctrl+Shift+F11. Hvis du trykker denne kommando 2 gange, vil SkypeTalking igen fokusere på Skypes oprindelige vindue med kontaktpersoner.

5.1. navigation i Contacts Manager

SkypeTalkings Contacts Manager viser dine kontaktpersoner i en multivalg listboks, hvilket giver dig mulighed for at vælge én eller flere kontaktpersoner, som du dernæst kan udføre en bestemt handling på. Med piletasterne bevæger du dig rundt i listen over kontaktpersoner og Mellemrum til henholdsvis at vælge og fravælge en kontaktperson. Contacts Manager viser ligeledes kontaktpersonernes status, humørbesked samt, for kontaktpesoner der er offline, meddelelse om tidspunkt for, hvornår den pågældende kontaktperson sidst blev set online.

5.2. Udføre en handling på den valgte kontaktperson

De valgmuligheder, der vises i Contacts Manager, afhænger af antallet af valgte kontaktpersone. Hvis du ikke har valgt nogen kontaktpersoner, giver SkypeTalking en advarselsbesked. Hvis en enkelt kontaktperson er valgt, er følgende handlinger tilgængelige:
1. Knappen Ring Op - foretrager et opkald til den valgte kontaktperson - denne knap er standard, så den aktiveres også ved tryk på Enter, når du står på en kontaktperson.
2. Knappen Chat - Åbner et vindue, der indeholder en chat med den valgte kontaktperson.
3. Knappen Vis Profil - Åbner Contact Managers profilvisningsvindue med oplysninger om den valgte kontaktpersons profil.
Hvis du har valgt 2 elelr flere kontaktpersoner, kan du foretage følgende handlinger:
1. Knappen Opret Telefonmøde - Opretter et telefonmøde med alle de valgte kontaktpersoner - denne knap er standard, så du kan også aktivere den ved tryk på Enter, når du har valgt kontaktpersonerne.
2. Knappen Opret Multichat - Åbner et chatvindue og opretter en multichat med alle de valgte kontaktpersoner.
Du kan med Tab og Shift+Tab bevæge dig imellem de forskellige handlinger og listen over kontaktpersoner. Du kan til enhver tid trykke Escape eller vælge knappen Cancel for at lukke Contacts Manager.

5.3. Profilvisning

Profilvisningen er en del af Contacts Manager, der aktiveres ved tryk på knappen Vis Profil for en enkelt kontaktperson. Den viser detaljerne i den pågældende kontaktpersons profil i en tilgængelig dialogboks, der er nem at bruge. Tab og Shift+Tab bruges til at flytte imellem de enkelte detaljer. Du kan desuden bruge piletasterne og de velkendte kommandoer til udvælgelse af tekst til kopiering af en bestemt detalje, hvis du har brug for det. Tryk Escape eller vælg knappen Cancel for at lukke Profilvisning og vende tilbage til Contacts Manager.

6. Sende og modtage SMS-beskeder med SkypeTalking

Du kan nemt sende og modtage SMS-beskeder med SkypeTalkings SMS-assistent.

6.1. SMS-assistenten

Du får adgang til SMS-assistenten ved at trykke Alt+Ctrl+Shift+S. Når den åbner, bliver du bedt om at indtaste et telefonnummer. Du skal indtaste et gyldigt telefonnummer inklusive landekode. For eksempel: +11234567. Hvis nummeret ikke er gyldigt, bliver du atter placeret i feltet til indtastning af telefonnummer, så du kan forsøge igen. Tryk Enter for at fortsætte eller Escape for at annullere. Hvis nummeret er gyldigt, fortsætter assistenten og du placeres nu i et indtastningsfelt, hvor du skriver din SMS-besked. Når du står i denne dialogboks, kan du til enhver til trykke F2 for at høre status for den SMS, du er i gang med at skrive. Du hører en advarselslyd, når det resterende antal tegn i beskeden når 0. Når du er færdig med at skrive din SMS, kan du trykke Enter eller bevæge dig med Tab til knappen Send eller trykke Cancel for at annullere afsendelsen. Når du har aktiveret knappen Send og din saldo er positiv, sendes din SMS.

7. Afsluttende bemærkninger og kontaktoplysninger

7.1. Hente kildekoden

SkypeTalking er gratis og open source software, der er skrevet i programmeringssproget PYTHON, som er tilgængeligt fra www.python.org. Open source betyder, at kildekoden er tilgængelig for alle, der ønsker den. SkypeTalking benytter licensen GNU General Public License version 2.0. Du finder hele teksten til licensen i filen license.txt, som følger med SkypeTalking. Hvis du selv er programmør eller ønsker at bidrage til kildekoden eller afvikler SkypeTalking direkte fra kildekoden, kan du finde kildekoden til SkypeTalking i SVN på følgende adresse:
http://skypetalking.googlecode.com
som er projektets netsted. Herfra kan du også hente den seneste version.

7.2. Bidrage med oversættelse

hvis du er oversætter og ønsker at lokalisere SkypeTalking og programmets dokumentation til dit eget sprog, kan du kontakte mig pr. e-mail for at få den seneste sprogfil sammen med instruktioner i, hvordan du kan sende dine oversættelser tilbage til mig. 

7.3. SkypeTalking postlisten

Du kan tilmelde dig SkypeTalkings e-postliste hos Google Grupper på følgende adresse:
skypetalking+subscribe@googlegroups.com.
Hvis du vil sende mail til listen, skal du sende til:
skypetalking@googlegroups.com.
Bemærk venligst at sproget på denne postliste er engelsk. Det er det bedste sted at få teknisk support samt tips og tricks til brugen af SkypeTalking. Det er også her, du modtager regelmæssig information om nyheder angående udviklingsarbejdet med SkypeTalking direkte fra kildekodens opbevaringssted på nettet. Alle spørgsmål er velkomne her, såvel begynderspørgsmål som spørgsmål om udviklingen.

7.5. Tak til

Følgende har på den ene eller anden måde bidraget til udviklingen af SkypeTalking:
- Hrvoje Katiæ, som er hovedmanden bag SkypeTalking-projektet.
- Gianluca Casalino, som har udviklet en række avancerede funktioner til SkypeTalking og har bidraget med en stor arbejdsindsats i programmeringen af SkypeTalking. Takket være hans engagement er SkypeTalking blevet endnu bedre end før! 
- René Linke, som også i nogen grad bidrager ved at lave rettelser og komme med ideer til nye funktioner.
- Mange supergode mennesker, der har gjort SkypeTalking tilgængeligt på deres eget sprog. Det betyder, at skypeTalking nu taler mere end 15 sprog!
- Og så naturligvis alle brugerne verden over, der hver dag benytter SkypeTalking og derved er med til at gøre opmærksom på programmet, så stadigt flere kan drage nytte af dette fremragende produkt!
En stor tak til jer alle!!!

7.5. Mine kontaktoplysninger

Min E-Mail adresse til spørgsmål, forslag, support og aflevering af oversættelser:  hrvojekatic@gmail.com
Du kan følge mig på Twitter under: www.twitter.com/hkatic
Min side på Facebook: www.facebook.com/jukebox2009
Mit Klango-Id på klango.net: DJ_Jukebox
På MSN er min adresse: hrkatic@hotmail.com
Skype Id: hrvojekatic

Slut på dokumentet   