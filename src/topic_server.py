import grpc
from google.protobuf.empty_pb2 import Empty

import topic_pb2
import topic_pb2_grpc

from db import topics, related

class TopicsServicer(topic_pb2_grpc.TopicsServicer):
  def AllTopics(self, request, context):
    return topic_pb2.TopicList(topics = topics)
  
  def Related(self, request, context):
    res = set()
    for (a, b) in related:
      if a == request.name:
        res.add(b)
      elif b == request.name:
        res.add(a)
    return topic_pb2.TopicList(topics=list(res))
