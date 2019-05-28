# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import post_pb2 as post__pb2


class PostsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/kittens.post.Posts/Create',
        request_serializer=post__pb2.CreatePostRequest.SerializeToString,
        response_deserializer=post__pb2.Post.FromString,
        )
    self.PostsByUser = channel.unary_stream(
        '/kittens.post.Posts/PostsByUser',
        request_serializer=post__pb2.PostsByUserRequest.SerializeToString,
        response_deserializer=post__pb2.Post.FromString,
        )
    self.Replies = channel.unary_stream(
        '/kittens.post.Posts/Replies',
        request_serializer=post__pb2.RepliesRequest.SerializeToString,
        response_deserializer=post__pb2.Post.FromString,
        )


class PostsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostsByUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Replies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PostsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=post__pb2.CreatePostRequest.FromString,
          response_serializer=post__pb2.Post.SerializeToString,
      ),
      'PostsByUser': grpc.unary_stream_rpc_method_handler(
          servicer.PostsByUser,
          request_deserializer=post__pb2.PostsByUserRequest.FromString,
          response_serializer=post__pb2.Post.SerializeToString,
      ),
      'Replies': grpc.unary_stream_rpc_method_handler(
          servicer.Replies,
          request_deserializer=post__pb2.RepliesRequest.FromString,
          response_serializer=post__pb2.Post.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kittens.post.Posts', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
