from atw.art import Art1, Art2, Art4
from datetime import date, timedelta

# Voorbeeld los gebruik van Art1: 2025-12-24 startdatum en 72 uur
Art1Voorbeeld= Art1(startDatum= date(2025,12,24), wettelijkeTermijn= timedelta(hours=72))
print("Verlenging van termijn met Art1", Art1Voorbeeld.verlengingTermijn)
print("Einddatum na verlenging:", Art1Voorbeeld.einddatum)

# Voorbeeld los gebruik van Art2: 2025-12-24 startdatum en 72 uur
Art2Voorbeeld= Art2(startDatum= date(2025,12,24), wettelijkeTermijn= timedelta(hours=72))
print("Verlenging van termijn met Art2", Art2Voorbeeld.verlengingTermijn)
print("Einddatum na verlenging:", Art2Voorbeeld.einddatum)

# Voorbeeld los gebruik van Art4: 2025-12-24 startdatum en 72 uur
Art4Voorbeeld= Art4(startDatum= date(2025,12,24), wettelijkeTermijn= timedelta(hours=72), wettelijkeTermijnEenheid = 'uur', verlengingTermijn= timedelta(days=2))
print("Verlenging van termijn met Art4:", Art4Voorbeeld.verlengingTermijn)
print("Einddatum na verlenging:", Art4Voorbeeld.einddatum)


# Voorbeeld gezamenlijk gebruik van Art1, Art2 en Art4 (voor applicatie)
voorbeeld_startdag = date(2025,12,24)
voorbeeld_wettelijke_termijn = timedelta(days=3)

Artikel1 = Art1(startDatum= voorbeeld_startdag, wettelijkeTermijn= voorbeeld_wettelijke_termijn)
print("Voorbeeld toegepast na artikel 1", Artikel1.verlengingTermijn)
Artikel2 = Art2(startDatum= voorbeeld_startdag, wettelijkeTermijn= voorbeeld_wettelijke_termijn, verlengingTermijn= Artikel1.verlengingTermijn)
print("Voorbeeld toegepast na artikel 2", Artikel2.verlengingTermijn)
Artikel4 = Art4(startDatum= voorbeeld_startdag, wettelijkeTermijn= voorbeeld_wettelijke_termijn, wettelijkeTermijnEenheid = 'uur', verlengingTermijn= Artikel2.verlengingTermijn)
print("Voorbeeld toegepast na artikel 4", Artikel4.verlengingTermijn)

print('Verlenging termijn volgens ATW', Artikel4.verlengingTermijn, 'tot', Artikel4.einddatum)