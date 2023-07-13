#import database_utils
from flask import Blueprint, request, json, jsonify
from sqlalchemy import create_engine, select, update, func, null, insert
from sqlalchemy.orm.session import sessionmaker
import database
import messageria

urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/')
def index():
    return 'urls index route'

@urls_blueprint.route('/init_db', methods = ['GET'])
def create_database():
    try:
        database.init_db()
        ret = {"status": "Database are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Database are not created!!"}    
    return ret    


@urls_blueprint.route('/create_tables', methods = ['GET'])
def create_tables():    
    try:
        database.init_tables()
        ret = {"status": "Tables are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Problems to create tables!!"}    
    return ret    


@urls_blueprint.route('/add_all_departamentos', methods = ['GET'])
def add_all_departamentos():
    ret = database.add_departamentos()    
    ret = {"status": "departamentos has been added"}
    return ret

@urls_blueprint.route('/add_pedido', methods = ['POST'])
def add_pedido():
    req_data = request.get_json()
    pedido_json = {"cliente": req_data['cliente'],
                    "alimento": req_data['alimento'],
                    "departamento_id": req_data['departamento_id']
                    }
    ret = database.add_pedido(pedido_json)   

    ret = {"status": "pedido has been added"}
    return ret


@urls_blueprint.route('/pedidos', methods = ['GET'])
def get_all_pedidos():
    res = database.get_all_pedidos()
    ret = {"status": "200", "pedidos": res}
    return ret

@urls_blueprint.route('/pedido', methods = ['DELETE'])
def delete_pedido_json():
    req_data = request.get_json()
    usuario_json = {"id": req_data['id']}
    ret = database.delete_usuario_json(usuario_json)
    print(usuario_json)
    return ret

@urls_blueprint.route('/pedido', methods = ['PUT'])
def update_pedido_json():
    req_data = request.get_json()
    pedido_json = {"id": req_data['id'], 
                    "cliente": req_data['cliente'],
                    "alimento": req_data['alimento'],
                    "departamento_id": req_data['departamento_id']
                    }
    ret = database.update_pedido_json(pedido_json)
    print(pedido_json)
    return ret

@urls_blueprint.route('/pedido/<id>', methods = ['GET'])
def get_one_pedido(id):
    pedido_json = {"id": id}
    res = database.get_one_pedidos(pedido_json)
    ret = {"status": "200", "pedido": res}
    return ret


@urls_blueprint.route('/enviar_pedidos', methods = ['GET'])
def enviar_pedidos():
    ret = messageria.send_all_pedidos()
    ret = {"status": "Pedidos enviados"}
    return ret

@urls_blueprint.route('/receber_pedidos', methods = ['GET'])
def receber_pedidos():
    ret = messageria.receive()
    ret = {"status": "Pedidos lidos"}
    return ret

