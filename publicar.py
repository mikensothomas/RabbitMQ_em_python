import pika

# Configurações de conexão
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Conectando ao RabbitMQ
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Loop para enviar mensagens
try:
    while True:
        # Solicitar mensagem do usuário
        mensagem = input("Digite a mensagem para enviar (ou 'sair' para encerrar): ")
        
        # Verifica se o usuário quer sair do loop
        if mensagem.lower() == 'sair':
            break
        
        # Publicar mensagem na fila
        channel.basic_publish(
            exchange="dados_fila",
            routing_key="",
            body=mensagem,
            properties=pika.BasicProperties(
                delivery_mode=2  # Mensagem persistente
            )
        )
        print("Mensagem enviada com sucesso!")

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")

finally:
    # Fechar conexão
    connection.close()
    print("Conexão com RabbitMQ fechada.")
