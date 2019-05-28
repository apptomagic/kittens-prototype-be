from concurrent import futures
import grpc
import hashlib
import post_pb2
import post_pb2_grpc
import time
import uuid

from grpc_reflection.v1alpha import reflection
from google.protobuf.timestamp_pb2 import Timestamp

posts = []

class PostsServicer(post_pb2_grpc.PostsServicer):
  """gRPC server for Posts"""
  def __init__(self):
    posts.clear()
  
  def Create(self, request, context):
    print('Got create post request')
    if not (request.text.strip()):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Post text can\'t be empty')
      raise Exception('Invalid arguments!')
    if not (request.conversationTitle or request.inReplyTo):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Replies need inReplyTo, OPs need conversationTitle')
      raise Exception('Invalid arguments!')
    post = post_pb2.Post()
    post.id = uuid.uuid5(uuid.NAMESPACE_DNS, 'apptomagic.com').hex
    post.text = request.text
    post.authorDisplayName = request.authorDisplayName
    post.conversationTitle = request.conversationTitle
    post.inReplyTo = request.inReplyTo
    post.created.GetCurrentTime()
    post.updated.FromNanoseconds(post.created.ToNanoseconds())
    posts.append(post)
    print('After answering request, posts is:\n', repr(posts))
    return post

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
    print('Posts Server running ...')

    try:
      # need an infinite loop since the above
      # code is non blocking, and if I don't do this
      # the program will exit
      while True:
        time.sleep(60*60*60)
    except KeyboardInterrupt:
      server.stop(0)
      print('Posts Server Stopped ...')

if __name__ == '__main__':
  server = PostsServicer()
  server.start_server()
