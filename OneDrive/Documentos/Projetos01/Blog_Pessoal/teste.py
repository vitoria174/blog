import redis

redis_connection = redis.Redis(host='localhost',port= 379, db=0)

print(redis_connection)

redis_connection.set('chave_1','valor_1')
valor = redis_connection.get('chave_1')
print(valor)
