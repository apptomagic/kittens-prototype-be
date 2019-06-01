import grpc
from google.protobuf.empty_pb2 import Empty

import topic_pb2
import topic_pb2_grpc

class TopicsServicer(topic_pb2_grpc.TopicsServicer):
  pass
