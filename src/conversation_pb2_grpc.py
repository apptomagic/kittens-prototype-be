# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import conversation_pb2 as conversation__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


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
        response_deserializer=conversation__pb2.ConversationAndOP.FromString,
        )
    self.ByTopic = channel.unary_stream(
        '/kittens.conversation.Conversations/ByTopic',
        request_serializer=conversation__pb2.ConversationsByTopicRequest.SerializeToString,
        response_deserializer=conversation__pb2.ConversationAndOP.FromString,
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

  def ByTopic(self, request, context):
    # missing associated documentation comment in .proto file
    pass
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
          response_serializer=conversation__pb2.ConversationAndOP.SerializeToString,
      ),
      'ByTopic': grpc.unary_stream_rpc_method_handler(
          servicer.ByTopic,
          request_deserializer=conversation__pb2.ConversationsByTopicRequest.FromString,
          response_serializer=conversation__pb2.ConversationAndOP.SerializeToString,
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
