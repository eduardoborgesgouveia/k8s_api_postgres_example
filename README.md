# INSTRUÇÕES 

## Requisitos para executar o programa:

* Alterar a conexão do banco Postgres em .env
* Alterar a conexão do Broker RabbitMqtt em 'messageria.py'
* Criar 4 filas com os nomes:
    -> 'sanduiches'
    -> 'pratos prontos'
    -> 'sobremesas'
    -> 'bebidas'

## Uma vez que o ambiente estiver preparado, devemos:

* executar o arquivo app.py
* realizar o request -> GET -> http://localhost:5000/init_db
* realizar o request -> GET -> http://localhost:5000/create_tables
* realizar o request -> GET -> http://localhost:5000/add_all_departamentos
* realizar o request -> POST -> http://localhost:5000/add_pedido
    * sugestão body:
> 
 ```
        {
            "cliente": "Eduardo",
            "alimento": "PF - Frango",
            "departamento_id": "2"
        }
 ``` 
> 
 ```
        {
            "cliente": "Pedro",
            "alimento": "cheese burg",
            "departamento_id": "1"
        }
 ```
> 
 ```
        {
            "cliente": "Joao",
            "alimento": "milkshake",
            "departamento_id": "4"
        }
 ```
> 
 ```
        {
            "cliente": "Maria",
            "alimento": "cheese cake",
            "departamento_id": "3"
        }
 ```
> 

