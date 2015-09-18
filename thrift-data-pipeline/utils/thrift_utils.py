from thrift.Thrift import TType
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


def get_model(data, thrift):
    result = list()
    spec = thrift.thrift_spec
    spec = filter(lambda x: x is not None, spec)
    for tid, ttype, field, _, _ in spec:
        value = data[field]
        value = value.strip()

        if ttype is TType.BOOL:
            value = bool(value)
        elif ttype is TType.DOUBLE:
            value = ''.join([i for i in value if i.isdigit() or i is "."])
            value = float(value)
        elif ttype is TType.I16 or ttype is TType.I32 or ttype is TType.I64:
            value = ''.join([i for i in value if i.isdigit()])
            value = int(value)
        elif ttype is TType.STRING:
            value = str(value)
        else:
            pass
        result.append((tid, value))
    result = sorted(result)
    result = map(lambda x: x[1], result)
    return thrift(*result)


def get_server(service, handler, port):
    processor = service.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    transport_factory = TTransport.TBufferedTransportFactory()
    protocol_factory = TBinaryProtocol.TBinaryProtocolFactory()
    return TServer.TSimpleServer(processor, transport, transport_factory, protocol_factory)


def get_async_server(service, handler, port):
    processor = service.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    transport_factory = TTransport.TFramedTransport(transport)
    protocol_factory = TBinaryProtocol.TBinaryProtocolFactory()
    return TServer.TThreadedServer(processor, transport, transport_factory, protocol_factory)


def get_thrift_client(host, port, service):
    socket = TSocket.TSocket(host, port)
    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = service.Client(protocol)
    transport.open()
    client.ping()
