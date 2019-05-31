# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: post.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='post.proto',
  package='kittens.post',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\npost.proto\x12\x0ckittens.post\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x80\x02\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08\x61uthorId\x18\x03 \x01(\t\x12\x19\n\x11\x61uthorDisplayName\x18\x04 \x01(\t\x12\x16\n\x0e\x63onversationId\x18\x05 \x01(\t\x12\x19\n\x11\x63onversationTitle\x18\x06 \x01(\t\x12\x11\n\tinReplyTo\x18\x07 \x01(\t\x12+\n\x07\x63reated\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tretracted\x18\n \x01(\x08\"h\n\x11\x43reatePostRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1a\n\x11\x61uthorDisplayName\x18\xe0\x07 \x01(\t\x12\x16\n\x0e\x63onversationId\x18\x03 \x01(\t\x12\x11\n\tinReplyTo\x18\x04 \x01(\t\"o\n\x12PostsByUserRequest\x12\x10\n\x08\x61uthorId\x18\x01 \x01(\t\x12\r\n\x05watch\x18\x02 \x01(\x08\x12\r\n\x05\x61\x66ter\x18\x03 \x01(\t\x12)\n\x05since\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"y\n\rThreadRequest\x12\x0e\n\x06postId\x18\x01 \x01(\t\x12\x0f\n\x07shallow\x18\x02 \x01(\x08\x12\r\n\x05watch\x18\x03 \x01(\x08\x12\r\n\x05\x61\x66ter\x18\x04 \x01(\t\x12)\n\x05since\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"F\n\x13SetupContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x05posts\x18\x02 \x03(\x0b\x32\x12.kittens.post.Post2\x95\x02\n\x05Posts\x12=\n\x06\x43reate\x12\x1f.kittens.post.CreatePostRequest\x1a\x12.kittens.post.Post\x12\x45\n\x0bPostsByUser\x12 .kittens.post.PostsByUserRequest\x1a\x12.kittens.post.Post0\x01\x12;\n\x06Thread\x12\x1b.kittens.post.ThreadRequest\x1a\x12.kittens.post.Post0\x01\x12I\n\x0cSetupContext\x12!.kittens.post.SetupContextRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_POST = _descriptor.Descriptor(
  name='Post',
  full_name='kittens.post.Post',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kittens.post.Post.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='kittens.post.Post.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authorId', full_name='kittens.post.Post.authorId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authorDisplayName', full_name='kittens.post.Post.authorDisplayName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversationId', full_name='kittens.post.Post.conversationId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversationTitle', full_name='kittens.post.Post.conversationTitle', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inReplyTo', full_name='kittens.post.Post.inReplyTo', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='kittens.post.Post.created', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated', full_name='kittens.post.Post.updated', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retracted', full_name='kittens.post.Post.retracted', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=347,
)


_CREATEPOSTREQUEST = _descriptor.Descriptor(
  name='CreatePostRequest',
  full_name='kittens.post.CreatePostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='kittens.post.CreatePostRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authorDisplayName', full_name='kittens.post.CreatePostRequest.authorDisplayName', index=1,
      number=992, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversationId', full_name='kittens.post.CreatePostRequest.conversationId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inReplyTo', full_name='kittens.post.CreatePostRequest.inReplyTo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=453,
)


_POSTSBYUSERREQUEST = _descriptor.Descriptor(
  name='PostsByUserRequest',
  full_name='kittens.post.PostsByUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authorId', full_name='kittens.post.PostsByUserRequest.authorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='watch', full_name='kittens.post.PostsByUserRequest.watch', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='kittens.post.PostsByUserRequest.after', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='kittens.post.PostsByUserRequest.since', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=566,
)


_THREADREQUEST = _descriptor.Descriptor(
  name='ThreadRequest',
  full_name='kittens.post.ThreadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='postId', full_name='kittens.post.ThreadRequest.postId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shallow', full_name='kittens.post.ThreadRequest.shallow', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='watch', full_name='kittens.post.ThreadRequest.watch', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='kittens.post.ThreadRequest.after', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='kittens.post.ThreadRequest.since', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=689,
)


_SETUPCONTEXTREQUEST = _descriptor.Descriptor(
  name='SetupContextRequest',
  full_name='kittens.post.SetupContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kittens.post.SetupContextRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='posts', full_name='kittens.post.SetupContextRequest.posts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=761,
)

_POST.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POST.fields_by_name['updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POSTSBYUSERREQUEST.fields_by_name['since'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_THREADREQUEST.fields_by_name['since'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SETUPCONTEXTREQUEST.fields_by_name['posts'].message_type = _POST
DESCRIPTOR.message_types_by_name['Post'] = _POST
DESCRIPTOR.message_types_by_name['CreatePostRequest'] = _CREATEPOSTREQUEST
DESCRIPTOR.message_types_by_name['PostsByUserRequest'] = _POSTSBYUSERREQUEST
DESCRIPTOR.message_types_by_name['ThreadRequest'] = _THREADREQUEST
DESCRIPTOR.message_types_by_name['SetupContextRequest'] = _SETUPCONTEXTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), dict(
  DESCRIPTOR = _POST,
  __module__ = 'post_pb2'
  # @@protoc_insertion_point(class_scope:kittens.post.Post)
  ))
_sym_db.RegisterMessage(Post)

CreatePostRequest = _reflection.GeneratedProtocolMessageType('CreatePostRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPOSTREQUEST,
  __module__ = 'post_pb2'
  # @@protoc_insertion_point(class_scope:kittens.post.CreatePostRequest)
  ))
_sym_db.RegisterMessage(CreatePostRequest)

PostsByUserRequest = _reflection.GeneratedProtocolMessageType('PostsByUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTSBYUSERREQUEST,
  __module__ = 'post_pb2'
  # @@protoc_insertion_point(class_scope:kittens.post.PostsByUserRequest)
  ))
_sym_db.RegisterMessage(PostsByUserRequest)

ThreadRequest = _reflection.GeneratedProtocolMessageType('ThreadRequest', (_message.Message,), dict(
  DESCRIPTOR = _THREADREQUEST,
  __module__ = 'post_pb2'
  # @@protoc_insertion_point(class_scope:kittens.post.ThreadRequest)
  ))
_sym_db.RegisterMessage(ThreadRequest)

SetupContextRequest = _reflection.GeneratedProtocolMessageType('SetupContextRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETUPCONTEXTREQUEST,
  __module__ = 'post_pb2'
  # @@protoc_insertion_point(class_scope:kittens.post.SetupContextRequest)
  ))
_sym_db.RegisterMessage(SetupContextRequest)



_POSTS = _descriptor.ServiceDescriptor(
  name='Posts',
  full_name='kittens.post.Posts',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=764,
  serialized_end=1041,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='kittens.post.Posts.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEPOSTREQUEST,
    output_type=_POST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PostsByUser',
    full_name='kittens.post.Posts.PostsByUser',
    index=1,
    containing_service=None,
    input_type=_POSTSBYUSERREQUEST,
    output_type=_POST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Thread',
    full_name='kittens.post.Posts.Thread',
    index=2,
    containing_service=None,
    input_type=_THREADREQUEST,
    output_type=_POST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetupContext',
    full_name='kittens.post.Posts.SetupContext',
    index=3,
    containing_service=None,
    input_type=_SETUPCONTEXTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSTS)

DESCRIPTOR.services_by_name['Posts'] = _POSTS

# @@protoc_insertion_point(module_scope)
