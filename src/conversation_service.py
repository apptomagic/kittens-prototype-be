import grpc
import uuid
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.empty_pb2 import Empty

import conversation_pb2
import conversation_pb2_grpc

from db import conversations
from auth import get_user_from_context


class ConversationsServicer(conversation_pb2_grpc.ConversationsServicer):
  """gRPC server for Conversations"""
  def __init__(self):
    conversations.clear_all()
  
  def Create(self, request, context):
    import post_pb2
    from db import posts
    print('Got create conversation request', context.invocation_metadata())
    user = get_user_from_context(context)
    if not user:
      context.set_code(grpc.StatusCode.UNAUTHENTICATED)
      context.set_details('Must be authenticated to post')
      raise Exception('Unauthenticated!')
    if not (request.title.strip()):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Conversations need title')
      raise Exception('Invalid arguments!')
    if not (request.text.strip()):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Conversations need text')
      raise Exception('Invalid arguments!')
    if not ([topic for topic in request.topics if topic.strip()]):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Conversations need topics')
      raise Exception('Invalid arguments!')
    conversation = conversation_pb2.Conversation()
    conversation.id = str(uuid.uuid4())
    post = post_pb2.Post()
    post.id = str(uuid.uuid4())
    post.text = request.text
    post.authorId = user.id
    post.authorDisplayName = user.displayName
    post.conversationId = conversation.id
    post.conversationTitle = request.title
    post.created.GetCurrentTime()
    post.updated.FromNanoseconds(post.created.ToNanoseconds())
    posts.append(post, context)
    conversation.title = request.title
    conversation.opId = post.id
    conversation.topics.extend(request.topics)
    conversations.append(conversation, context)
    print('After answering request, conversations is:\n', repr(conversations))
    return conversation_pb2.ConversationAndOP(
      conversation = conversation,
      op = post,
    )

  def ByTopic(self, request, context):
    if request.watch:
      return super().ByTopic(request, context)
    from db import posts
    pager = conversations.pager(request)
    for conversation in conversations.iter_with_context(context):
      if request.topic in conversation.topics:
        op = posts.get_one(conversation.opId, context)
        if pager(conversation, op.created):
          yield conversation_pb2.ConversationAndOP(
            conversation = conversation,
            op = op,
          )

  
  ########################################################################
  # admin/testing
  def SetupContext(self, request, context):
    print('got context request', request)
    conversations.populate(request.name, request.conversations)
    return Empty()
