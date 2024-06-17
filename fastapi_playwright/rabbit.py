from aio_pika import connect, Message

RABBITMQ_URL = "amqp://guest:guest@localhost/"

async def send_task(identifier: str, url: str):
    connection = await connect(RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue(name="task_queue", durable=True)
    message = Message(body=f"{identifier},{url}".encode())
    await queue.publish(message)
    await connection.close()