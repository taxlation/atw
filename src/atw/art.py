from dataclasses import dataclass
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

@dataclass
class Art1: 
  """
  Dataclass voor Art. 1 Algemene termijnenwet
  """
  startDatum: date # startdatum
  wettelijkeTermijn: timedelta # in een wet gestelde termijn
  verlengingTermijn: timedelta = timedelta(days=0) # verlenging van termijn

  def __post_init__(self):
    self.Art1Lid1()
    self.Art1Lid2()

  @property
  def einddatum(self):
    """
    Berekent de einddatum van de gestelde termijn.

    Functie telt het wettelijke termijn en de eventuele verlenging op bij de startdatum.

    Geeft terug:
      datetime.date: De einddatum met inachtneming van de wettelijke termijn en verlenging.
    """
    return self.startDatum + self.wettelijkeTermijn + self.verlengingTermijn

  def Art1Lid1(self):
    """
    Past de termijn aan zodat de einddatum niet eindigt op zater-, zon- en feestdagen.

    Functie controleert of einddatum op een zater-, zon- of feestdag valt, of in de lijst met feeestdagen voorkomt. 
    Als dat zo is, wordt de termijn met één dag verlengd en wordt de functie opnieuw toegepast.
    
    Geeft terug:
      datetime.date: De eventueel verlengde termijn met inachtneming van artikel 1, lid 1, ATW.
    """
    while self.einddatum.weekday() >= 5 or self.einddatum in Art3:
      self.verlengingTermijn += timedelta(days=1)
    
    return self.verlengingTermijn
  
  def Art1Lid2(self):
    """
    Deze functie maakt de termijnaanpassing van functie Art2Lid1 ongedaan als de termijn negatief is.

    Functie controleert of termijn minder dan 0 is.
    Als dat zo is, wordt de verlengde einddatum op de oorspronkelijke einddatum gezet.

    Geeft terug:
      datetime.date: De eventueel niet-verlengde termijn met inachtneming van artikel 1, lid 2, ATW.
    """
    if self.wettelijkeTermijn < timedelta(0):
      self.verlengingTermijn = timedelta(days=0)
    
    return self.verlengingTermijn


@dataclass
class Art2:  
  """
  Dataclass voor Art. 2 Algemene termijnenwet
  """
  startDatum: date # startdatum
  wettelijkeTermijn: timedelta # in een wet gestelde termijn
  verlengingTermijn: timedelta = timedelta(days=0) # verlenging van termijn
  
  def __post_init__(self):
    self.Art2()

  @property
  def einddatum(self):
    """
    Berekent de einddatum van de gestelde termijn.

    Functie telt het wettelijke termijn en de eventuele verlenging op bij de startdatum.

    Geeft terug:
      date: De einddatum met inachtneming van de wettelijke termijn en verlenging.
    """
    return self.startDatum + self.wettelijkeTermijn + self.verlengingTermijn

  def Art2(self):
    """
    Verlengt de termijn in geval de termijn ten minste drie dagen is maar niet bestaat uit twee werkdagen.

    Deze functie controleert of de termijn tenminste drie dagen is. 
    Als dat het geval is, wordt zo nodig de termijn zoveel verlengd dat daarin ten minste twee dagen voorkomen die niet een zaterdag, zonder of algemeen erkende feestdag zijn.
    
    Geeft terug:
     timedelta: De verlenging van de termijn.
    """
    if (self.einddatum - self.startDatum) >= timedelta(days=3):
      huidige_datum = self.startDatum
      werk_dagen = 0

      while (huidige_datum <= self.einddatum):
        if huidige_datum.weekday() < 5 and huidige_datum not in Art3:
          werk_dagen += 1
        huidige_datum += timedelta(days=1)

      while werk_dagen < 2:
        self.verlengingTermijn += timedelta(days=1)
        if self.einddatum.weekday() < 5  and self.einddatum not in Art3:
          werk_dagen +=1

      return self.verlengingTermijn

Art3 = [
  date(2025, 1, 1), # Nieuwjaarsdag: woensdag 1 januari 2025 (lid 1)
  date(2025, 4, 21), # Tweede Paasdag: maandag 21 april 2025 (lid 1)
  date(2025, 5, 9), # Tweede Pinksterdag: maandag 25 mei 2025 (lid 1)
  date(2025, 12, 25), # Eerste Kerstdag: donderdag 25 december 2025 (lid 1)
  date(2025, 12, 26), # Tweede Kerstdag: vrijdag 26 december 2025 (lid 1)
  date(2025, 5, 29), # Hemelvaartsdag: donderdag 29 mei 2025 (lid 1)
  date(2025, 4, 26), # Dag waarop de verjaardag van de Koning wordt gevierd: zaterdag 26 april 2025 (lid 1)
  date(2025, 5, 5), # Vijfde mei: maandag 5 mei 2025 (lid 1)
  date(2025, 4, 18), # Goede Vrijdag: vrijdag 18 april 2025 (lid 2)
  date(2025, 5, 30), # Besluit van 8 maart 2022, nr. 2022000289: vrijdag 30 mei 2025 (lid 3)
]

@dataclass
class Art4: 
  """
  Dataclass voor Art. 4 Algemene termijnenwet
  """
  startDatum: date # startdatum
  wettelijkeTermijn: timedelta # in een wet gestelde termijn
  wettelijkeTermijnEenheid: str # Eenheid van de in een wet gestelde termijn (uur, dag, week, maand, jaar)
  verlengingTermijn: timedelta = timedelta(days=0) # verlenging van termijn

  def __post_init__(self):
    self.Art4OnderdeelA()

  @property
  def einddatum(self):
    """
    Berekent de einddatum van de gestelde termijn.

    Functie telt het wettelijke termijn en de eventuele verlenging op bij de startdatum.

    Geeft terug:
      datetime.date: De einddatum met inachtneming van de wettelijke termijn en verlenging.
    """
    return self.startDatum + self.wettelijkeTermijn + self.verlengingTermijn
  
def Art4OnderdeelA(self) -> bool:
    """
    Laat verlengde termijnen niet van toepassing zijn indien de wettelijke termijn specifiek is geformuleerd.
    
    Returns:
      bool: True if Art. 4 applies (no extensions allowed)
    """
    if ((self.wettelijkeTermijnEenheid == 'uur') or
      (self.wettelijkeTermijn > timedelta(days=90) and self.wettelijkeTermijnEenheid == 'dag') or
      (self.wettelijkeTermijn > timedelta(weeks=12) and self.wettelijkeTermijnEenheid == 'week') or
      (self.wettelijkeTermijn > (self.startDatum + relativedelta(months=1) - self.startDatum) and self.wettelijkeTermijnEenheid == 'maand') or
      (self.wettelijkeTermijn >= (self.startDatum + relativedelta(year=12) - self.startDatum) and self.wettelijkeTermijnEenheid == 'jaar')
    ):
      self.verlengingTermijn = timedelta(days=0)
      return True
    return False

      