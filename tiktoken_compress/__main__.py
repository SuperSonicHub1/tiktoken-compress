from argparse import ArgumentParser, FileType, Namespace
from sys import stdin, stdout
from tiktoken_compress import compress, decompress

def compress_command(args: Namespace):
	args.output.write(compress(args.input.read()))

def decompress_command(args: Namespace):
	args.output.write(decompress(args.input.read()))

parser = ArgumentParser()

subparsers = parser.add_subparsers(help='sub-command help', required=True)

parser_compress = subparsers.add_parser('compress', help='encode text')
parser_compress.set_defaults(func=compress_command)
parser_compress.add_argument('input', nargs='?', type=FileType('r'), default=stdin)
parser_compress.add_argument('output', nargs='?', type=FileType('wb'), default=stdout)

parser_decompress = subparsers.add_parser('decompress', help='decode text')
parser_decompress.set_defaults(func=decompress_command)
parser_decompress.add_argument('input', nargs='?', type=FileType('rb'), default=stdin)
parser_decompress.add_argument('output', nargs='?', type=FileType('w'), default=stdout)

args = parser.parse_args()
args.func(args)
