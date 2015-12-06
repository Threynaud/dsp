# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`pwd`: Display the current working directory. <br>
`cd <path>`: Navigate to the parent directory. <br>
`mkdir <name>`: Create a new directory named 'name'. <br>
`rm <file>`: Delete 'file'. Use -r argument to delete the repository <br>
`mv <old> <new>`: Rename old file to new. <br>
`cp <file> <directory>`: Copy file into the repository. <br>
`find <directory> name "<file>"`: Find all files named 'file' in the directory. <br>
`grep "<text>" <file>`: Return all occurencies of 'text' in the file. Use `-i` for case insensitivity. <br>
`grep "<text>" <directory>`: Return all files contaning 'text' in 'directory'. <br>
`sudo`: Run programs with the security privileges of another user, including the super user. <br>
`top`or `htop`: Display information about running processes. <br>
`kill <pid>`: Quit process number "pid". <br>
`man`: Read manual page. <br>.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

`ls` : List the files in a given directory <br>
`ls -a`: Include directory entries whose names begin with a dot (.) <br>
`ls -l`: List in long format which include for instance the file mode, the number of links, the owner name, the group name, the number of bytes in the file, ... <br>
`ls -lh`: When used with the -l option, use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 2 for sizes.

`ls -la`: List all files and folders including hidden ones in long format.
`ls -lha` will both give long format, with reduced file size for all files and folders including hidden ones.

---


---

What does `xargs` do? Give an example of how to use it.

`xargs` is used to pass the output of one command as an argument to another command. <br>
`ls -1 *.py | xargs wc -l` will count number of lines/words/characters in each python  file under the given directory.

---

