from boa.interop.Neo.Blockchain import GetHeader
from boa.interop.Neo.Header import GetHash, GetNextConsensus  # All these references are needed


def Main(height):
    header = GetHeader(height)
    hash_val = GetHash(header)
    return hash_val
