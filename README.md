# JsonLParser
Parses JsonL files. Finds key's in JsonL lines and extracts the value.


" , are removed before output to text file 

Worked decently with 26Gb JsonL file after zstd decompression


#notes to self
zstd was run in Git Bash as it's added as a command to bash profile
zsrd -D [file location]         Decompresses zstd file to the file type that comes next in the name, in this case JsonL

Was a fun way to explore Python file input, output and some of the syntax python has
