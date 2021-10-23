# Summarization

## Files:
Files are named series of bytes with bits (0's and 1's) on hard drive.
There are 2 main type of files:
* binary
* textual

Binary files are just considered as sequence of bytes.
Textual files are considered as series of bytes that are splitted into series of codepoints(series of bytes representing
some character)
Textual files have specific encoding (for instance UTF-8)

## Python IO:
Python io module is basicc module for IO actions.

### Binary IO:
Binary io procedure takes in raw binary data (bytes/byte array) and doesn't perform any action on it during reading/writing

### Text IO:
text io procedure takes in binary data, then tries to encode the data according to specific encoding (unicode) into
character during reading and during writing it decodes characters into bytes before writing to disk.

Text io procedure takes in raw data (non-buffered)

## IO.open:
* `open()` is similar to `io.open()`
* `open(path, 'rb')` open for binary reading
* `open(path, 'wb')` open for binary writing

## Closing File:
File is closed automatically when program finishes execution or it can be closed with file.close() call

## with statement:
with statement allows to automatically call file.close() at the end of its execution.

## Read:
`read()` - allows to read all bytes or specific number of them from file.
`readline()` - allows to read all characters per line or specific number of them from file.
`readlines()` - reads all the lines of file

## Write:
* write(string)
* write(sequence)

## File Buffering:
Buffer - is memory object, that can store chunk of data from OS file stream until it is consumed.
When consumed buffer is filled with new similar portion of data if there is any more data in file stream.
Interacting with OS file stream might have high latency (considerable time is taken to get data from OS file stram or to 
write to it)

`open()` has buffering option that can have the following values:
* 0 - unbuffered.
* 1 - line buffering.
* positive integer > 1 - number of bytes buffered
* -1 - system default.

Text can't be unbuffered as the bytes should be loaded to buffer first then converted to characters.

## Internal and OS buffers:
Python creates its won buffer to speed up operations to prevent system calls for every write operation
Thus, when buffer is filled only then the data is written to OS file stream. But it can be written to OS buffer, not file
itself.
The data can be in internal buffer until the file is closed, so if the power goes off, the data can be lost.

`flush()` - writes the data from internal buffer to OS buffer without closing.
If another process will read the file, it will get the fresh contents.

## Random Access to File:
By default, we read/write from/to file from the start, but it's possible to change that behavior.
Opening a file system associates a pointer with it which determines from where reading or writing take place.

`file.tell()` - returns current position of the pointer.

we can navigate to specific location using `file.seek(offset,whence=0)` where offset defines how many bytes will be skipped
from whence.

whence can have the following values:
* 0 - start of the file
* 1 - current position
* 2 - end of file

## IO.BytesIO():
io.BytesIO() is creating a buffer in memory that can be used to write some data there or later read from it. This object 
has api similar to files and can be used instead of files in parameter.

