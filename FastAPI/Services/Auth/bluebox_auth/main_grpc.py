import logging
from concurrent import futures

import grpc

from config import Config
from infrastructure.postgresql.database import setup_database
from rpc.api_keys.setup import setup_api_key


def serve():
    port = Config.SERVE_PORT
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    setup_api_key(server)

    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    setup_database()
    serve()
