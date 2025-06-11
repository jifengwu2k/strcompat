import sys
from typing import Text
from posix_or_nt import posix_or_nt

if posix_or_nt() == 'nt':
    DEFAULT_FILESYSTEM_ENCODING = 'mbcs'
    DEFAULT_STDOUT_ENCODING = 'mbcs'
    DEFAULT_STDIN_ENCODING = 'mbcs'
else:
    DEFAULT_FILESYSTEM_ENCODING = 'utf-8'
    DEFAULT_STDOUT_ENCODING = 'utf-8'
    DEFAULT_STDIN_ENCODING = 'utf-8'


def get_filesystem_encoding():
    # type: () -> str
    return sys.getfilesystemencoding() or DEFAULT_FILESYSTEM_ENCODING


def get_stdout_encoding():
    # type: () -> str
    return getattr(sys.stdout, 'encoding', None) or DEFAULT_STDOUT_ENCODING


def get_stdin_encoding():
    # type: () -> str
    return getattr(sys.stdin, 'encoding', None) or DEFAULT_STDIN_ENCODING


if sys.version_info < (3,):
    from urllib import quote, unquote


    def text_to_utf_8_str(text):
        # type: (Text) -> str
        return text.encode('utf-8')


    def utf_8_str_to_text(utf_8_str):
        # type: (str) -> Text
        return unicode(utf_8_str, 'utf-8')


    def text_to_uri_str(text):
        # type: (Text) -> str
        # UTF-8 is required to encode non-ASCII characters into valid URIs.
        return quote(text.encode('utf-8'))


    def uri_str_to_text(uri_str):
        # type: (str) -> Text
        return unicode(unquote(uri_str), 'utf-8')


    def text_to_stdout_str(text):
        # type: (Text) -> str
        return text.encode(get_stdout_encoding())


    def stdin_str_to_text(stdin_str):
        # type: (str) -> Text
        return unicode(stdin_str, get_stdin_encoding())


    def text_to_filesystem_str(text):
        # type: (Text) -> str
        return text.encode(get_filesystem_encoding())


    def filesystem_str_to_text(filesystem_str):
        # type: (str) -> Text
        return unicode(filesystem_str, get_filesystem_encoding())
else:
    from urllib.parse import quote, unquote


    def text_to_utf_8_str(text):
        # type: (Text) -> str
        return text


    def utf_8_str_to_text(utf_8_str):
        # type: (str) -> Text
        return utf_8_str


    def text_to_uri_str(text):
        # type: (Text) -> str
        return quote(text)


    def uri_str_to_text(uri_str):
        # type: (str) -> Text
        return unquote(uri_str)


    def text_to_stdout_str(text):
        # type: (Text) -> str
        return text


    def stdin_str_to_text(stdin_str):
        # type: (str) -> Text
        return stdin_str


    def text_to_filesystem_str(text):
        # type: (Text) -> str
        return text


    def filesystem_str_to_text(filesystem_str):
        # type: (str) -> Text
        return filesystem_str
