# tiktoken-compress

Using GPT3's [byte-pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding) to
compress text. The number of tokens GPT-3 has in its vocab happens (n=50280) to fit quite nicely
into an unsigned short, so I'd thought I'd give it a try. It's quite efffective, having a compression
ratio of about 50%, but  good ol' gzip as expected blows it out of the water. Would it be
possible to make a an ultra-text-specific compression algorithm that can beat gzip? Maybe,
but certainly not with this.

```
$ du -h *txt*
3.9M    bible.txt
1.2M    bible.txt.gz
2.0M    bible.txt.ttk
1.1M    tiny-shakespeare.txt
428K    tiny-shakespeare.txt.gz
664K    tiny-shakespeare.txt.ttk
2.4M    world192.txt
708K    world192.txt.gz
1.3M    world192.txt.ttk
```

## Usage
```shell
python -m tiktoken_compress compress bible.txt bible.txt.ttk
python -m tiktoken_compress decompress bible.txt.ttk bible-decompressed.txt 
```

## Test Sources
- https://github.com/karpathy/char-rnn/blob/master/data/tinyshakespeare/input.txt
- https://corpus.canterbury.ac.nz/descriptions/#large
