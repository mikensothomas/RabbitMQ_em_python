import pika

def minha_callback(ch, method, properties, body):
    print(body)

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(
    queue="dados_fila",
    durable=True
)
channel.basic_consume(
    queue="dados_fila",
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f'Escutando na porta: 5672')
channel.start_consuming()

