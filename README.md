# pydocstrtest
This is a scratch repo to test python docstring solutions and formats.


## How I ran the test

I tested two python api documentation generators (pdoc and sphinx) with 3 python docstring styles.

### Pdoc
[Pdoc](https://github.com/mitmproxy/pdoc) is a simple to use tool for generating python documentaiton from docstrings in the source.

Usage:
```bash
pip install pdoc

pdoc -o ./docs mypdoctest
```

The output of this is in the docs folder for review.

### Sphinx
Sphinx is a powerful but much more complicated tool for generating pythong documentation from docstrings in the source.  I followed [these instructions](https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b) to get things setup and working.  It was a much more involved and error prone process.

Usage:
```bash
pip install -U Sphinx

sphinx-build -b html sphinx/source sphinx/build/html
```

To run a server and preview the output:
```bash
python3 -m http.server 3000
```

## My opinions

Starting with docstring formating:
- Google style and Numpy style are both easy to write
- Google style and Numpy style are both easy to read in the py files as a developer
- Google style and Numpy style both produce nice hints in default VSCode w/ Python extension
- Google style and Numpy style both produce nice output using pdoc
- Google style and Numpy style both produce lower quality output using sphinx
- RsT style produces very nice output using sphinx
- RsT style is more complex to read and write in the py files as a developer
- RsT style does not produce clean hints in default VSCode w/ Python extension

So it comes down to your need.  If API docuemtation is important I'd go with RsT style.  If
developer experience is more important I'd go with Google or Numpy style.  Google and Numpy
style seem equivalent to me.  The tool selection is directly tied to this same intent.  If
need nice API docuemtation to publish, definitely use Sphinx and RsT style.  If you just need
a nice developer experience I'd use pdoc.  Sphinx is quite complicated and appears to require
more care and feeding to maintain correct configuration.  That said, it is also quite powerful
and highly customizable.