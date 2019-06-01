import grpc
import uuid
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.empty_pb2 import Empty

import conversation_pb2
import conversation_pb2_grpc

from db import conversations


class ConversationsServicer(conversation_pb2_grpc.ConversationsServicer):
  """gRPC server for Conversations"""
  def __init__(self):
    conversations.clear_all()
  
  def Create(self, request, context):
    import post_pb2
    from db import posts
    print('Got create conversation request', context.invocation_metadata())
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
    post.authorDisplayName = request.authorDisplayName or 'Anonymous Coward'
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
    return conversation_pb2.CreateConversationResponse(
      conversation = conversation,
      op = post,
    )

  def Thread(self, request, context):
    if request.watch:
      return super().Thread(request, context)
    from db import posts
    conversation = conversations.get_one(request.conversationId, context)
    thread = [conversation.opId]
    pager = posts.pager(request)
    for post in posts.iter_with_context(context):
      if post.id == conversation.opId and pager(post):
        yield post
      elif post.inReplyTo in thread:
        thread.append(post.id)
        if pager(post):
          yield post
  
  ########################################################################
  # admin/testing
  def SetupContext(self, request, context):
    print('got context request', request)
    conversations.populate(request.name, request.conversations)
    return Empty()
