# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cta_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cta_event.proto',
  package='cta_event',
  serialized_pb=_b('\n\x0f\x63ta_event.proto\x12\tcta_event\"2\n\x08\x43TAEvent\x12\x14\n\x0ctelescope_id\x18\x01 \x02(\r\x12\x10\n\x04\x64\x61ta\x18\x04 \x03(\x02\x42\x02\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CTAEVENT = _descriptor.Descriptor(
  name='CTAEvent',
  full_name='cta_event.CTAEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='telescope_id', full_name='cta_event.CTAEvent.telescope_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='cta_event.CTAEvent.data', index=1,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['CTAEvent'] = _CTAEVENT

CTAEvent = _reflection.GeneratedProtocolMessageType('CTAEvent', (_message.Message,), dict(
  DESCRIPTOR = _CTAEVENT,
  __module__ = 'cta_event_pb2'
  # @@protoc_insertion_point(class_scope:cta_event.CTAEvent)
  ))
_sym_db.RegisterMessage(CTAEvent)


_CTAEVENT.fields_by_name['data'].has_options = True
_CTAEVENT.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)