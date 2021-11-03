from abc import ABC ,abstractmethod
class Band:
    """
    Band Class Container of musicians
    """
    instance=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
    def play_solos(self):
        SoloArray = []
        for i in self.members:
            SoloArray.append(i.play_solo())
        return SoloArray

    
    @classmethod
    def to_list(cls):
        return cls.instances
  
    
class Musician:
    """
    Musician Class
    """
    def __init__(self,name):
        self.name = name
    def get_instrument(self):
      pass
    @abstractmethod
    def play_solo(self):
           pass
    @abstractmethod  
    def __str__(self):
          pass
    @abstractmethod      
    def __repr__(self):
         pass

class Guitarist(Musician):
    """Guitar player Class"""
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"
       
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
            
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
  

class Drummer(Musician):
    """Drummer player Class"""
    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash"
       
    def __str__(self):
        return f"My name is {self.name} and I play drums"
            
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
  
class Bassist(Musician):
    """Bassist player Class"""
    def get_instrument(self):
        return "bass"  

    def play_solo(self):
        return "bom bom buh bom"
    def __str__(self):
        return f"My name is {self.name} and I play bass"
            
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


if __name__ == "__main__":

   name=input("please enter your name> ")
    
   name = Bassist(name)

   Issa = Bassist(name)

   print(f'{name.name} Is playing on {name.get_instrument()} Thats make a sound {name.play_solo()}')
   print(Issa.name)
   print(Issa.get_instrument())
   print(Issa.play_solo())

   Salman = Guitarist('Salman')
   print(Salman.name)
   print(Salman.get_instrument())
   print(Salman.play_solo())



   Josef = Drummer('Josef')
   print(Josef.name)
   print(Josef.get_instrument())
   print(Josef.play_solo())
   
