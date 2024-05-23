class Personaje:
  def __init__(self,sexo,edad,ps,atk,vatk,natk,vivo):
    self.sexo="masc"
    self.edad=0
    self.ps=1
    self.atk=1
    self.vatk=0
    self.natk=0
    self.vivo=True
  def atk_simple(self,enemigo):
    if (enemigo.ps<=self.atk)and(self.vivo>0):
      enemigo.vivo=False
      enemigo.ps=0
    else:
      enemigo.ps=enemigo.ps-self.atk
    self.n_atk+=1
  def subir_vel(self):
     self.n_atk+=1
     self.vatk=self.vatk+self.vatk/2
class Hechicero(Personaje):
  def __init__ (self,sexo,edad,ps,atk,vatk,natk,vivo,tipo_magia):
    super(). __init__(sexo,edad,ps,atk,vatk,natk,vivo)
    self.tipo_magia="NONE"
  def atk_esp (self,enemigo):
    if (self.tipo_magia=="Transformación"):
      if (enemigo.sexo=="masc"):
        enemigo.sexo="fem"
        self.n_atk+=1
      else: 
        enemigo.sexo="fem"
        self.n_atk+=1
    else: 
      if (self.tipo_magia=="Debilitación"):
        enemigo.atk-=enemigo.atk/10
        self.n_atk+=1
      else:
        super().atk_simple
class Curandero(Personaje):
  def __init__ (self,sexo,edad,ps,atk,vatk,natk,vivo,tipo_magia):
    super(). __init__(sexo,edad,ps,atk,vatk,natk,vivo)
    self.tipo_magia="NONE"
  def atk_esp (self,enemigo):
    if (self.tipo_magia=="Auto_Curación"):
     self.ps+=self.atk
     self.n_atk+=1
    else: 
      if (self.tipo_magia=="Síntesis"):
        if (enemigo.ps/10>2):
          enemigo.ps-=enemigo.ps/10
          self.ps+=self.ps/10
        else:
          enemigo.ps-=2   
        self.n_atk+=1
      else:
        super().atk_simple
hechicero = Hechicero(sexo="masc",edad=192,ps=250,atk=260,vatk=1,natk="0",vivo=True,tipo_magia="Transformacion")
hechicero.ps=250
hechicero.atk=260
curandero = Curandero(sexo="fem",edad=32,ps=120,atk=100,vatk=1,natk="0",vivo=True,tipo_magia="Síntesis")
curandero.ps=120
curandero.atk=100
print (hechicero.ps)
print (curandero.ps)
curandero.atk_esp(hechicero)
hechicero.atk_esp(curandero)
print (hechicero.ps)
print (curandero.ps)