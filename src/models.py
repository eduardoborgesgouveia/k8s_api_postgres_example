from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
#from database import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Departamento(Base):
    __tablename__ = 'departamentos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    def __repr__(self):
       return "<Departamento(id='%s', nome='%s')>" % (
                             self.id, self.nome)

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    alimento = Column(String)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'))
    departamento = relationship("Departamento", backref="pedidos")
    def __repr__(self):
       return "<Pedido(id='%s', cliente='%s', alimento='%s', departamento_id='%s', departamento_nome='%s')>" % (
                             self.id, self.cliente, self.alimento, self.departamento_id, self.departamento.nome)
    
