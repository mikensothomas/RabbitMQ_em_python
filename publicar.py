import pika

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

try:
    while True:
        mensagem = input("Digite a mensagem (ou 'sair' para encerrar): ")
        
        if mensagem.lower() == 'sair':
            break
        
        channel.basic_publish(
            exchange="dados_fila",
            routing_key="",
            body=mensagem,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        print("Mensagem enviada com sucesso!")

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")

finally:
    connection.close()
    print("Conexão com RabbitMQ fechada.")
