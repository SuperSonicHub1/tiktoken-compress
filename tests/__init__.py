from tiktoken_compress import compress, decompress

string = "Hello, world!"
assert decompress(compress(string)) == string
