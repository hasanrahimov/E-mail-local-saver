# E-pasta saglabātāja programmas README.md

## Projekta uzdevums

Šī programma ir izstrādāta, lai risinātu problēmu, ka daži cilvēki neveikli izmanto mūsdienu tehnoloģijas un dažreiz, nejauši izdzēš svarīgas e-pasta ziņas. Šī programma nodrošina garantiju, ka neviens e-pasta vēstules netiks dzēstas lietotāja kļūdas dēļ, un tās var tikt atjaunotas pat pēc gadiem.

## Python bibliotēkas un to izmantošana

Šajā projektā tiek izmantotas vairākas Python bibliotēkas, lai efektīvi apstrādātu un saglabātu e-pasta ziņas. Galvenokārt tie ir:

- os: Lai darbotos ar failu sistēmu un izveidotu direktorijas saglabāšanai.
- imaplib: Drošai IMAP savienojumam ar e-pasta serveri.
- email: E-pasta ziņu parsēšanai un apstrādei.
- decode_header: Lai dekodētu e-pasta virsrakstus un iegūtu skaidru informāciju.
- parsedate_to_datetime: Lai pārvērstu e-pasta ziņas datumus datuma objektos, lai failam varētu piešķirt nosaukumu kā datumu.

Šīs bibliotēkas tiek izmantotas, lai uzlabotu programmas veiktspēju un nodrošinātu efektīvu e-pasta ziņu saglabāšanu.

## Programmatūras izmantošanas metodes

1. Ievadīt e-pasta datus: Programma lietotājam prasa ievadīt savu e-pasta adresi un lietotnes paroli, lai veiktu pieslēgumu e-pasta serverim.

2. Atlasīt vēstules: Pēc veiksmīgas pieslēgšanās programma atlasa visus e-pasta ziņojumus no lietotāja "INBOX" mapes.

3. Saglabāt e-pasta vēstules: Katru atrastu e-pasta vēstuli programma saglabā uz lietotāja datora, izveidojot direktorijas un failus, kas atbilst nosūtītāju un datuma informācijai.

4. Atjaunot dzēstās vēstules: Ja lietotājs nejauši izdzēš e-pasta vēstuli, programma nodrošina*, ka tā netiek dzēsta, saglabājot to direktorijā "Saved-E-mails".

5. Izvēlēties failu formātu: Programma atšķiras atkarībā no tā, vai e-pasta vēstulē ir pielikumi vai tikai teksts, un saglabā tos atbilstoši.

Ar šīm metodēm programma nodrošina vieglu lietošanu un pilnu kontroli pār saviem saglabātajiem e-pasta ziņojumiem, novēršot to nejaušu zaudējumu un palīdzot lietotājiem efektīvāk pārvaldīt savu e-pastu.

*Ja programma tika iespējota pirms vēstules dzēšanas
