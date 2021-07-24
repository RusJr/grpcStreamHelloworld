import asyncio
import logging

import grpc

from protos import SuperStream_pb2_grpc, SuperStream_pb2


class SuperStream(SuperStream_pb2_grpc.SuperStreamServicer):

    async def getAnswer(self, request_iterator, context):
        yield SuperStream_pb2.ServerReply(text='Start!')
        async for msg in request_iterator:
            print(msg)
            yield SuperStream_pb2.ServerReply(text=f'Your msg is: {msg}')
        yield SuperStream_pb2.ServerReply(text='Done!')


async def serve() -> None:
    server = grpc.aio.server()
    SuperStream_pb2_grpc.add_SuperStreamServicer_to_server(SuperStream(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(serve())
