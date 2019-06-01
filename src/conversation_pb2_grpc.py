# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import conversation_pb2 as conversation__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import post_pb2 as post__pb2


class ConversationsStub(object):
  """////////////////////////////////////////////////////////////////////////
  service definition

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/kittens.conversation.Conversations/Create',
        request_serializer=conversation__pb2.CreateConversationRequest.SerializeToString,
        response_deserializer=conversation__pb2.CreateConversationResponse.FromString,
        )
    self.Thread = channel.unary_stream(
        '/kittens.conversation.Conversations/Thread',
        request_serializer=conversation__pb2.ThreadRequest.SerializeToString,
        response_deserializer=post__pb2.Post.FromString,
        )
    self.SetupContext = channel.unary_unary(
        '/kittens.conversation.Conversations/SetupContext',
        request_serializer=conversation__pb2.SetupContextRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ConversationsServicer(object):
  """////////////////////////////////////////////////////////////////////////
  service definition

  """

  def Create(self, request, context):
    """Create a new conversation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Thread(self, request, context):
    """All posts in the conversation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetupContext(self, request, context):
    """//////////////////////////////////////////////////////////////////////
    admin/testing
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConversationsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=conversation__pb2.CreateConversationRequest.FromString,
          response_serializer=conversation__pb2.CreateConversationResponse.SerializeToString,
      ),
      'Thread': grpc.unary_stream_rpc_method_handler(
          servicer.Thread,
          request_deserializer=conversation__pb2.ThreadRequest.FromString,
          response_serializer=post__pb2.Post.SerializeToString,
      ),
      'SetupContext': grpc.unary_unary_rpc_method_handler(
          servicer.SetupContext,
          request_deserializer=conversation__pb2.SetupContextRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kittens.conversation.Conversations', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
