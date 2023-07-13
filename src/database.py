import json
import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, insert, delete
from models import Base, Departamento, Pedido
from sqlalchemy_utils import database_exists, create_database
# from settings import DATABASE_URL
DATABASE_URL = os.environ.get('DATABASE_URL_ARG')
print(DATABASE_URL)
#engine = None
engine = create_engine(DATABASE_URL)

db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
                                         
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Base de dados criada com sucesso!!")
    else:
        print("Base de dados já foi criada!!")
        engine.connect()

def init_tables():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()    
    
    if (sqlalchemy.inspect(engine).has_table("usuario")):
        print("Table alredy exists")
        ret = {"status": "Table alredy exists"}
    else:
        import models
        Base.metadata.create_all(bind=engine)
        print("Tables has been created!!")
        ret = {"status": "Tables has been created!!"}
    return ret

def add_departamentos():
    engine = create_engine(DATABASE_URL)    
    con = engine.connect()

    Session = sessionmaker(engine)
    session = Session()     
    DEPARTAMENTOS_BASE = ['sanduiches', 'pratos prontos', 'sobremesas', 'bebidas']
    for dep in DEPARTAMENTOS_BASE:
        query = (
                insert(Departamento).
                values(
                    nome = dep
                    )
        )

        print(query)
        try:

            result = session.execute(query)
            session.commit()
            ret = {"status": "departamentos has been added"}
        

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
    
def add_pedido(json):
    engine = create_engine(DATABASE_URL)    
    con = engine.connect()

    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Pedido).
            values(
                cliente = json['cliente'],
                alimento = json['alimento'],
                departamento_id = json['departamento_id']
                )
    )
    print(query)    
    try:
        #result = conn.execute(query)
        result = session.execute(query)
        print(result.fetchall())
        session.commit()
        ret = {"status": "Pedido has been added"}
    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret


def get_all_pedidos():
    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Pedido)    
    res = session.execute(s).all()
    list_ret = []
    for row in res:
        aux = {
            "id": row['Pedido'].id,
            "cliente": row["Pedido"].cliente,
            "alimento": row["Pedido"].alimento,
            "departamento_id": row["Pedido"].departamento.id,
            "departamento": row["Pedido"].departamento.nome
        }
        list_ret.append(aux)
    return list_ret
    
    
def get_all_departamentos():
    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Departamento)    
    res = session.execute(s).all()
    list_ret = []
    for row in res:
        aux = {
            "id": row['Departamento'].id,
            "nome": row["Departamento"].nome
        }
        list_ret.append(aux)
    return list_ret 

def get_one_pedidos(json_pedido):
    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Pedido).where(Pedido.id == json_pedido['id'])
    conn = engine.connect()
    res = session.execute(s).all()
    list_ret = []
    for row in res:
        aux = {
            "id": row['Pedido'].id,
            "cliente": row["Pedido"].cliente,
            "alimento": row["Pedido"].alimento,
            "departamento_id": row["Pedido"].departamento.id,
            "departamento": row["Pedido"].departamento.nome
        }
        list_ret.append(aux)
    print(list_ret)
    return list_ret
    

def delete_pedido_json(json_pedido):
    engine = create_engine(DATABASE_URL)    
    con = engine.connect()

    Session = sessionmaker(engine)
    session = Session()     

    query = (
            delete(Pedido).
            where(Pedido.id == json_pedido['id'])
    )
    
    print(query)    
    try:
        result = session.execute(query)
        session.commit()
        if(result.rowcount > 0):
            ret = {"status": "Pedido has been deleted"}
        else:
            ret = {"status": "Pedido did not find"}
   

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret

def update_pedido_json(json_pedido):
    engine = create_engine(DATABASE_URL)    
    con = engine.connect()

    
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            update(Pedido).
            where(Pedido.id == json_pedido['id']).
            values( cliente = json_pedido['cliente'],
                    alimento = json_pedido['alimento'],
                    departamento_id = json_pedido['departamento_id'])
    )
    print(query)    
    try:
        result = session.execute(query)
        session.commit()
        
        if (result.rowcount > 0):
            ret = {"status": "Pedido has been updated"}
        else:
            ret = {"status": "Pedido has not been updated"}    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret