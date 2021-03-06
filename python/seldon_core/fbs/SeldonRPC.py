# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SeldonRPC(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSeldonRPC(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SeldonRPC()
        x.Init(buf, n + offset)
        return x

    # SeldonRPC
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SeldonRPC
    def Method(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # SeldonRPC
    def MessageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # SeldonRPC
    def Message(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def SeldonRPCStart(builder): builder.StartObject(3)
def SeldonRPCAddMethod(builder, method): builder.PrependInt8Slot(0, method, 0)
def SeldonRPCAddMessageType(builder, messageType): builder.PrependUint8Slot(1, messageType, 0)
def SeldonRPCAddMessage(builder, message): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(message), 0)
def SeldonRPCEnd(builder): return builder.EndObject()
