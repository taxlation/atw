# atw - Algemene termijnenwet
## Overzicht
Dit package past de regels van de Algemene termijnenwet (hierna: Atw) toe bij de berekening van de verlengde termijn. Deze regels zijn van toepassing wanneer de einddatum van een termijn op een zaterdag, zondag of algemeen erkende feestdag eindigt.

## Classes
### Art. 1
**Properties**
- _startDatum_: start datum van een termijn (date).
- _wettelijkeTermijn_: In een wet gestelde termijn (timedelta).
- _verlengingTermijn_: Nieuw te berekenen verlenging van de termijn (timedelta).
- _eindDatum_: Nieuw te berekenen einddatum (date).

**Methods**
- _Art1Par1()_: Verlengt de termijn, als deze op een zaterdag, zondag of algemeen erkende feestdag eindigt, tot en met de eerstvolgende dag die niet een zaterdag, zondag of feestdag is.
- _Art1Par2()_: Maakt de verlenging ongedaan wanneer de termijn is bepaald door terugrekening vanaf de start van een termijn.

### Art. 2 
**Properties**
- _startDatum_: start datum van een termijn (date).
- _wettelijkeTermijn_: In een wet gestelde termijn (timedelta).
- _verlengingTermijn_: Nieuw te berekenen verlenging van de termijn (timedelta).
- _eindDatum_: Nieuw te berekenen einddatum (date).

**Methods**
- _Art2()_: Verlengt een in de wet gestelde termijn van tenminste drie dagen zo nodig dat in de termijn ten minste twee dagen voorkomen die niet een zaterdag, zondag of een algemeen erkende feestdag zijn.

### Art. 3
**Defaults**
- Volgens lid 1: Nieuwjaarsdag, de Christelijke tweede Paas- en Pinksterdag, de beide Kerstdagen, de Hemelvaartsdag, de dag waarop de verjaardag van de Koning wordt gevierd en de vijfde mei (Date).
- Volgens lid 2: Goede Vrijdag (Date).
- Volgens lid 3: Gepubliceerd in de Nederlandse Staatscourant (Date).

### Art. 4
**Properties**
- _startDatum_: start datum van een termijn (date).
- _wettelijkeTermijn_: In een wet gestelde termijn (timedelta).
- _verlengingTermijn_: Nieuw te berekenen verlenging van de termijn (timedelta).
- _eindDatum_: Nieuw te berekenen einddatum (date).

**Methods**
- _Art4_: Maakt een verlenging ongedaan in geval de termijn is omschreven in uren, in meer dan 90 dagen, in meer dan twaalf weken, in meer dan drie maanden, of in een of meer jaren, of de termijn betreft de bekendmaking, inwerkingtreding of buitenwerkingtreding van wettellijke voorschriften, of de termijn betreft de termijn van vrijheidsbeneming.
