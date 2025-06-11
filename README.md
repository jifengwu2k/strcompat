# strcompat

A Python library handling conversions `unicode` <-> UTF-8 `str`s (Python 2), `unicode` <-> URI `str`s (Python 2 and 3), and `unicode` <-> `str`s in the filesystem encoding (Python 2).

Different versions of Python treat `str` and `unicode` differently:

- In **Python 2**, `str` is a byte string, and `unicode` is a Unicode string.
- In **Python 3**, `str` is a Unicode string.

Windows systems running Python 2 are especially prone to Unicode issues:

- The default system encoding is often ASCII - too limited for many real-world text values.
- APIs like `open()`, `os.listdir()`, `os.path`, `subprocess`, and many Windows-specific APIs expect `str` values, not `unicode`.
- The filesystem encoding (`mbcs`) and console encodings (`cp936`, etc.) are not UTF-8.

This library ensures that Unicode data is properly encoded to native `str` when required - for example, encoding file paths, URIs, or command-line arguments.

It handles the following conversions:


| Function | Python 2 | Python 3 |
|----------|----------|----------|
| `unicode_to_utf_8_string` | `unicode` -> UTF-8 `str` | No-op |
| `utf_8_string_to_unicode` | UTF-8 `str` -> `unicode` | No-op |
| `unicode_to_uri_string` | `unicode` -> URI-encoded `str` | `str` -> URI-encoded `str` |
| `uri_string_to_unicode`   | URI `str` -> decoded `unicode` | URI `str` -> decoded `str` |
| `unicode_to_filesystem_string` | `unicode` -> `str` in filesystem encoding  | No-op |
| `filesystem_string_to_unicode` | `str` in filesystem encoding -> `unicode` | No-op |

## Usage Example

On a Windows machine with:

- `sys.getdefaultencoding() == 'ascii'`
- `sys.getfilesystemencoding() == 'mbcs'`
- `locale.getpreferredencoding() == 'cp936'`
- `sys.stdout.encoding == 'cp936'`
- `sys.stderr.encoding == 'cp936'`

```python
>>> from strcompat import *
>>> u = u"测试A1你我他中文123!@#￥%（）【】～*"

>>> unicode_to_utf_8_string(u)
# Python 2:
'\xe6\xb5\x8b\xe8\xaf\x95A1\xe4\xbd\xa0\xe6\x88\x91\xe4\xbb\x96\xe4\xb8\xad\xe6\x96\x87123!@#\xef\xbf\xa5%\xef\xbc\x88\xef\xbc\x89\xe3\x80\x90\xe3\x80\x91\xef\xbd\x9e*'
# Python 3:
'测试A1你我他中文123!@#￥%（）【】～*'

>>> utf_8_string_to_unicode(unicode_to_utf_8_string(u)) == u
# Python 2 and 3:
True

>>> unicode_to_uri_string(u)
# Python 2 and 3:
'%E6%B5%8B%E8%AF%95A1%E4%BD%A0%E6%88%91%E4%BB%96%E4%B8%AD%E6%96%87123%21%40%23%EF%BF%A5%25%EF%BC%88%EF%BC%89%E3%80%90%E3%80%91%EF%BD%9E%2A'

>>> uri_string_to_unicode(unicode_to_uri_string(u)) == u
# Python 2 and 3:
True

>>> unicode_to_filesystem_string(u)
# Python 2: '\xb2\xe2\xca\xd4A1\xc4\xe3\xce\xd2\xcb\xfb\xd6\xd0\xce\xc4123!@#\xa3\xa4%\xa3\xa8\xa3\xa9\xa1\xbe\xa1\xbf\xa1\xab*'
# Python 3:
'测试A1你我他中文123!@#￥%（）【】～*'

>>> filesystem_string_to_unicode(unicode_to_filesystem_string(u)) == u
# Python 2 and 3:
True
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
