import asyncio
import logging

import grpc
from google.protobuf.json_format import MessageToDict

from protos import SuperStream_pb2_grpc, SuperStream_pb2


async def msg_generator():
    for i in range(10):
        yield SuperStream_pb2.ClientMessage(text=f'The message #{i}')
        await asyncio.sleep(1)


async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = SuperStream_pb2_grpc.SuperStreamStub(channel)
        call = stub.getAnswer(msg_generator())
        async for response in call:
            print(MessageToDict(response))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(main())
