from typing import List
class Virus:
  accession:str
  name:str
  genotype:str
  country:str
  date:str
  size:str

  def __init__(self, virusList:List[str])-> None:
    self.accession = virusList[0]
    self.name = virusList[1]
    self.genotype = virusList[2]
    self.country = virusList[3]
    if (virusList[4].rfind("N") != -1):
      self.date = "0"
    else:
      self.date = virusList[4]
    self.size = virusList[5]

  def getAccess(self)-> str:
    return self.accession

  def getName(self)->str:
    return self.name

  def getGenotype(self)->str:
    return self.genotype

  def getCountry(self)->str:
    return self.country

  def getDate(self)->int:
    return self.date

  def getSize (self)->int:
    return self.size