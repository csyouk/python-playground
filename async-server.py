import asyncio
import sys

PORT = 8888
BUFFER_SIZE = 1024

## server side
async def _handle(reader, writer):
  # data = await reader.read(BUFFER_SIZE)
  data = await reader.read(1000000)
  print("{0} bytes received:{1}".format(len(data), data.decode()))
  await asyncio.sleep(1)
  data = data + b" add"
  writer.write(data)
  writer.close()

async def run_server():
  server = await asyncio.start_server(_handle, 'localhost', port=PORT)


async def _connect(mes):
  print("msg : ", mes)
  mes = mes * 10000000
  reader, writer = await asyncio.open_connection('localhost', PORT)
  writer.write(mes.encode())
  # data = await reader.read(BUFFER_SIZE)
  data = await reader.read(len(mes))
  print("decode : ", data.decode())
  writer.close()

if __name__ == "__main__":
  if len(sys.argv) > 1:
    loop = asyncio.get_event_loop()
    if sys.argv[1] == 'server':
      loop.create_task(run_server())
      loop.run_forever()
    else:
      print(sys.argv)
      loop.run_until_complete(_connect(sys.argv[1]))
    loop.close()

