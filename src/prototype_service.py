from concurrent import futures
import grpc
import time
from grpc_reflection.v1alpha import reflection

import post_pb2
import post_pb2_grpc
from post_service import PostsServicer

def start_server(self):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  post_pb2_grpc.add_PostsServicer_to_server(PostsServicer(), server)

  SERVICE_NAMES = (
      post_pb2.DESCRIPTOR.services_by_name['Posts'].full_name,
      reflection.SERVICE_NAME,
  )
  reflection.enable_server_reflection(SERVICE_NAMES, server)

  server.add_insecure_port('[::]:50051')

  server.start()
  print('Prototype Server running ...')

  try:
    # need an infinite loop since the above
    # code is non blocking, and if I don't do this
    # the program will exit
    while True:
      time.sleep(60*60*60)
  except KeyboardInterrupt:
    server.stop(0)
    print('Prototype Server Stopped ...')

if __name__ == '__main__':
  server = PostsServicer()
  server.start_server()
