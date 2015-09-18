from thrift.Thrift import TType


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
    return thrift(*result)
