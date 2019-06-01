import grpc
import hashlib
import post_pb2
import post_pb2_grpc
import uuid

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.empty_pb2 import Empty

posts = {'': []}

class IterWithContext(object):
  def __init__(self, collection, context):
    self.collection = collection
    self.contexts = ['']
    for md in context.invocation_metadata():
      if md.key == 'use-data-contexts':
        self.contexts = md.value.split('+')
  
  def __iter__(self):
    # for now we only support one context, as more than one will complicate things
    # with regards to sorting and duplicates/cow
    for item in self.collection[self.contexts[0]]:
      yield item

class Pager(object):
  def __init__(self, request):
    self.after = request.after
    self.since = request.since.ToNanoseconds()
    self.seen = not self.after
  
  def __call__(self, post):
    if self.since > post.created.ToNanoseconds(): return False
    if self.after:
      if self.seen:
        return True
      if post.id == self.after:
        self.seen = True
        return False
      return False
    return True

class PostsServicer(post_pb2_grpc.PostsServicer):
  """gRPC server for Posts"""
  def __init__(self):
    posts[''].clear()
  
  def Create(self, request, context):
    print('Got create post request', context.invocation_metadata())
    if not (request.text.strip()):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Post text can\'t be empty')
      raise Exception('Invalid arguments!')
    if not (request.conversationId or request.inReplyTo):
      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details('Replies need inReplyTo, OPs need conversationId')
      raise Exception('Invalid arguments!')
    post = post_pb2.Post()
    post.id = str(uuid.uuid4())
    post.text = request.text
    post.authorDisplayName = request.authorDisplayName or 'Anonymous Coward'
    post.conversationId = request.conversationId
    # TODO cache conversationTitle
    post.inReplyTo = request.inReplyTo
    post.created.GetCurrentTime()
    post.updated.FromNanoseconds(post.created.ToNanoseconds())
    posts[''].append(post)
    print('After answering request, posts is:\n', repr(posts))
    return post
  
  def PostsByUser(self, request, context):
    if request.watch:
      return super().PostsByUser(request, context)
    pager = Pager(request)
    for post in IterWithContext(posts, context):
      # TODO when we have proper auth we'll use user IDs, for now display names
      if (post.authorDisplayName == request.authorId) or (post.authorId == request.authorId) and pager(post):
        yield post

  def Thread(self, request, context):
    if request.watch:
      return super().Thread(request, context)
    thread = [request.postId]
    pager = Pager(request)
    for post in IterWithContext(posts, context):
      if post.id == request.postId and pager(post):
        yield post
      elif post.inReplyTo in thread:
        if not request.shallow:
          thread.append(post.id)
        if pager(post):
          yield post
  
  ########################################################################
  # admin/testing
  def SetupContext(self, request, context):
    print('got context request', request)
    posts[request.name] = request.posts
    return Empty()
