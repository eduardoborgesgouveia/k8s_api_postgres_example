import json
import time
import pika
import database

connection = None
def conect():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    return channel

def send(queue, message):
    connection = conect()
    connection.basic_publish(exchange='', routing_key=queue, body=message)
    print(" [x] Sent '" + message + "'")
    connection.close()

def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

def receive():
    connection = conect()
    ret = database.get_all_departamentos()
    res = []
    for departamento in ret:
        connection.basic_consume(queue=departamento['nome'], on_message_callback=callback, auto_ack=True)
    
    connection.start_consuming()
    time.sleep(4)
    connection.stop_consuming()



def send_all_pedidos():
    ret = database.get_all_pedidos()
    for pedido in ret:
        send(pedido['departamento'], json.dumps(pedido))
    return ret
