## PLEASE BACKUP BEFORE APPLYING THIS SCRIPT TO A DIRECTORY

# search-and-replace

This is a very simple tool that replaces, at the same time, directory names, file names, and file contents, based on a simple pattern.

Imagine that you have this project structure:

* RootProject/
  * PREFIX1DIRECTORY/
    * PREFIX1FILE.java
    * SomeFile.js
    
And PREFIX1FILE.java content is:

```
asdasdasdasdasprefix1
PREFIX1
Something
Blablabla

```
If you run the following command:

```
sar RootProject/ "PREFIX1" "SomethingElse"
```

Your new project structure will be:

* RootProject/
  * SomethingElseDIRECTORY/
    * SomethingElseFILE.java
    * SomeFile.js
    
And SomethingElseFILE.java content will be:

```
asdasdasdasdasSomethingElse
SomethingElse
Something
Blablabla

```
 
Important:
* When the character "/" is provided as a pattern, it will be replaced with "#" on file and directory names.
* The search for the old pattern is case insensitive in file's contents, and the new pattern is replaced exactly as provided.
  
  
  
