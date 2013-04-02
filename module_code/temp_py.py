__author__ = 'zhuxh'

import tempfile

print(tempfile.gettempdir())
print(tempfile.gettempprefix())

print(tempfile.mkdtemp())
print(tempfile.TemporaryFile().name)