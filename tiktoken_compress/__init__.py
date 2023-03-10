import tiktoken
import struct

# assert encoding.max_token_value == 50280
# Just small enough to fit in a short!
encoding = tiktoken.get_encoding("p50k_base")

def compress(text: str) -> bytes:
	return b"".join(token_id.to_bytes(2, "big", signed=False) for token_id in encoding.encode(text))

def decompress(buffer: bytes) -> str:
	return encoding.decode(struct.unpack(f">{len(buffer) // 2}H", buffer))
