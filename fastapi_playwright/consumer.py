import aio_pika
import asyncio
from save_page_content import save_page_content

async def process_task(message: aio_pika.IncomingMessage):
    async with message.process():
        identifier, url = message.body.decode().split(",")
        output_path = f"screenshots/{identifier}.html"
        await save_page_content(url, output_path)
        print(f"Saved {url} to {output_path}")

async def consume():
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("task_queue", durable=True)
    await queue.consume(process_task)

loop = asyncio.get_event_loop()
loop.run_until_complete(consume())