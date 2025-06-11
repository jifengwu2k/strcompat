import sys

if sys.version_info >= (3,):
    from urllib.parse import quote, unquote
    
    def unicode_to_utf_8_string(unicode_string):
        return unicode_string
    
    def utf_8_string_to_unicode(utf_8_string):
        return utf_8_string

    def unicode_to_uri_string(unicode_string):
        return quote(unicode_string)
    
    def uri_string_to_unicode(uri_string):
        return unquote(uri_string)

    def unicode_to_filesystem_string(unicode_string):
        return unicode_string

    def filesystem_string_to_unicode(filesystem_string):
        return filesystem_string
else:
    from urllib import quote, unquote
    from posix_or_nt import posix_or_nt

    def unicode_to_utf_8_string(unicode_string):
        return unicode_string.encode('utf-8')
    
    def utf_8_string_to_unicode(utf_8_string):
        return unicode(utf_8_string, 'utf-8')

    # UTF-8 is required to encode non-ASCII characters into valid URIs.
    def unicode_to_uri_string(unicode_string):
        return quote(unicode_string.encode('utf-8'))
    
    def uri_string_to_unicode(uri_string):
        return unicode(unquote(uri_string), 'utf-8')

    if posix_or_nt() == 'nt':
        default_filesystem_encoding = 'mbcs'
    else:
        default_filesystem_encoding = 'utf-8'
    
    get_filesystem_encoding = lambda: sys.getfilesystemencoding() or default_filesystem_encoding

    def unicode_to_filesystem_string(unicode_string):
        return unicode_string.encode(get_filesystem_encoding())

    def filesystem_string_to_unicode(filesystem_string):
        return unicode(filesystem_string, get_filesystem_encoding())
