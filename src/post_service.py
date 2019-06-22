import grpc
import uuid
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.empty_pb2 import Empty

import post_pb2
import post_pb2_grpc

from dev import debug
from db import posts
from auth import get_user_from_context


class PostsServicer(post_pb2_grpc.PostsServicer):
  """gRPC server for Posts"""
  def __init__(self):
    posts.clear_all()
  
  def Create(self, request, context):
    debug('Got create post request', context.invocation_metadata())
    user = get_user_from_context(context)
    if not user:
      context.set_code(grpc.StatusCode.UNAUTHENTICATED)
      context.set_details('Must be authenticated to post')
      raise Exception('Unauthenticated!')
    if not request.text.strip():
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Posts need text')
      raise Exception('Invalid arguments!')
    if not (request.conversationId or request.inReplyTo):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Posts need conversationId')
      raise Exception('Invalid arguments!')
    if not request.conversationId:
      parent = posts.get_one(request.inReplyTo, context)
      request.conversationId = parent.conversationId
    else:
      from db import conversations
      conversation = conversations.get_one(request.conversationId, context)
      if not request.inReplyTo:
        request.inReplyTo = conversation.opId
    post = post_pb2.Post()
    post.id = str(uuid.uuid4())
    post.text = request.text
    post.authorId = user.id
    post.authorDisplayName = user.displayName
    post.conversationId = request.conversationId
    # TODO cache conversationTitle
    post.inReplyTo = request.inReplyTo
    post.created.GetCurrentTime()
    post.updated.FromNanoseconds(post.created.ToNanoseconds())
    posts.append(post, context)
    debug('After answering request, posts is:\n', repr(posts))
    return post
  
  def PostsByUser(self, request, context):
    if request.watch:
      return super().PostsByUser(request, context)
    pager = posts.pager(request)
    for post in posts.iter_with_context(context):
      # TODO when we have proper auth we'll use user IDs, for now display names
      if (post.authorDisplayName == request.authorId) or (post.authorId == request.authorId) and pager(post):
        yield post

  def Thread(self, request, context):
    if request.watch:
      return super().Thread(request, context)
    thread = [request.postId]
    pager = posts.pager(request)
    for post in posts.iter_with_context(context):
      if post.id == request.postId and pager(post):
        yield post
      elif post.inReplyTo in thread:
        if not request.shallow:
          thread.append(post.id)
        if pager(post):
          yield post

  def Conversation(self, request, context):
    if request.watch:
      return super().Conversation(request, context)
    pager = posts.pager(request)
    for post in posts.iter_with_context(context):
      if post.conversationId == request.conversationId and pager(post):
        yield post

  ########################################################################
  # admin/testing
  def SetupContext(self, request, context):
    debug('got context request', request)
    posts.populate(request.name, request.posts)
    return Empty()
