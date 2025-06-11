# textcompat

A Python library handling conversions from `typing.Text` (Python 2 `unicode`, Python 3 `str`) to UTF-8, URI,
stdin/stdout, and filesystem `str`s, and vice versa.

Specifically, it handles the following conversions:

| Function                 | Python 2                                  | Python 3                   |
|--------------------------|-------------------------------------------|----------------------------|
| `text_to_utf_8_str`      | `unicode` -> UTF-8 `str`                  | No-op                      |
| `utf_8_str_to_text`      | UTF-8 `str` -> `unicode`                  | No-op                      |
| `text_to_uri_str`        | `unicode` -> URI `str`                    | `str` -> URI `str`         |
| `uri_str_to_text`        | URI `str` -> decoded `unicode`            | URI `str` -> decoded `str` |
| `text_to_stdout_str`     | `unicode` -> `str` in stdout encoding     | No-op                      |
| `stdin_str_to_text`      | `str` in stdin encoding -> `unicode`      | No-op                      |
| `text_to_filesystem_str` | `unicode` -> `str` in filesystem encoding | No-op                      |
| `filesystem_str_to_text` | `str` in filesystem encoding -> `unicode` | No-op                      |

To determine the filesystem encoding, the library tries to use `sys.getfilesystemencoding()`. If it returns `None`, the
library detects the operating system and uses reasonable defaults:

- NT: 'mbcs'
- POSIX: 'utf-8'

## Example

On an NT machine with:

- `sys.getdefaultencoding() == 'ascii'`
- `sys.getfilesystemencoding() == 'mbcs'`
- `locale.getpreferredencoding() == 'cp936'`
- `sys.stdin.encoding == 'cp936'`
- `sys.stdout.encoding == 'cp936'`

```python
from __future__ import print_function
from textcompat import *

text = u'测试A1你我他中文123!@#￥%（）【】～*'

print(repr(text_to_utf_8_str(text)))
# Python 2:
# '\xe6\xb5\x8b\xe8\xaf\x95A1\xe4\xbd\xa0\xe6\x88\x91\xe4\xbb\x96\xe4\xb8\xad\xe6\x96\x87123!@#\xef\xbf\xa5%\xef\xbc\x88\xef\xbc\x89\xe3\x80\x90\xe3\x80\x91\xef\xbd\x9e*'
# Python 3:
# '测试A1你我他中文123!@#￥%（）【】～*'

assert type(utf_8_str_to_text(text_to_utf_8_str(text))) is type(text) and utf_8_str_to_text(
    text_to_utf_8_str(text)) == text

print(repr(text_to_uri_str(text)))
# Python 2 and 3:
# '%E6%B5%8B%E8%AF%95A1%E4%BD%A0%E6%88%91%E4%BB%96%E4%B8%AD%E6%96%87123%21%40%23%EF%BF%A5%25%EF%BC%88%EF%BC%89%E3%80%90%E3%80%91%EF%BD%9E%2A'

assert type(utf_8_str_to_text(text_to_utf_8_str(text))) is type(text) and uri_str_to_text(text_to_uri_str(text)) == text

print(repr(text_to_stdout_str(text)))
# Python 2: '\xb2\xe2\xca\xd4A1\xc4\xe3\xce\xd2\xcb\xfb\xd6\xd0\xce\xc4123!@#\xa3\xa4%\xa3\xa8\xa3\xa9\xa1\xbe\xa1\xbf\xa1\xab*'
# Python 3: '测试A1你我他中文123!@#￥%（）【】～*'

assert type(stdin_str_to_text(text_to_stdout_str(text))) is type(text) and stdin_str_to_text(
    text_to_stdout_str(text)) == text

print(repr(text_to_filesystem_str(text)))
# Python 2: '\xb2\xe2\xca\xd4A1\xc4\xe3\xce\xd2\xcb\xfb\xd6\xd0\xce\xc4123!@#\xa3\xa4%\xa3\xa8\xa3\xa9\xa1\xbe\xa1\xbf\xa1\xab*'
# Python 3: '测试A1你我他中文123!@#￥%（）【】～*'

assert type(utf_8_str_to_text(text_to_utf_8_str(text))) is type(text) and filesystem_str_to_text(
    text_to_filesystem_str(text)) == text
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
