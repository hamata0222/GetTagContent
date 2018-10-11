# GetTagContent
This script gets content from a file.
The file is specified by expression below.

```
<path-to-the-file> (<line-number>)

  <path-to-the-file>  : The full path to the file
  <line-number>       : The number of line in the file to get the content
```

## Usage
You can give the script a argument to input file.
Or no argument, the script want you to input file.

```
[example.txt]
/path/to/the/file/file_name (10)
/path/to/the/file/file_name (1234)
```

```
$ python GetTagContent.py example.txt
```

## Result
You can see the result of script in the file which has the name ``_result`` after the name of the input file.
If your input file name is ``example.txt``, the result file name is ``example_result.txt``.

```
[example_result.txt]
/path/to/the/file/file_name (10): the content of the file
/path/to/the/file/file_name (1234): the content of line 1234
```

