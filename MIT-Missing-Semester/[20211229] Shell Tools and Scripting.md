# Shell Tools and Scripting

这节课见识了好多好多搜索相关的工具。

```bash
# NOTICE! No Space!
foo=bar
echo $foo
echo "Value is $foo"
echo 'Value is $foo'
```

**mcd.sh**

```bash
mcd () {
    mkdir -p "$1"
    cd "$1"
}
```

```bash
source mcd.sh
mcd test
# $_ is last argument of last command;
# $? is the return value of last command;

# about debug
shellcheck mcd.sh

# redo last command with super user
sudo !!

# about the false
false
echo $?
false || echo "Oops fail"
false || "Thsi will not print"
true && echo "Things went well"
false && "Thsi will not print"
false ; echo "This will always print"

foo=$(pwd)
echo $foo
echo "we are in $(pwd)"
cat <(ls) <(ls ..)
```

**example.sh**

```bash
#!/bin/bash

echo "Starting program at $(date)"

echo "Running program $0 with $# arguments with pid $$"

for file in "$@"; do
    grep foobar "$file" > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status
    # We redirect STDOUT and STDERR to a null register because we do not care about them
    if [[ "$?" -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

```bash
ls *.sh
ls project?
convert image.png image.jpg
convert image.{png,jpg}

touch foo{,1,2,10}
touch project{1,2}/src/test/test{1,2,3}.py

mkdir foo bar
touch {foo,bar}/{a..j}
touch foo/x bar/y
diff <(ls foo) <(ls bar)
```

**script.py**

```python
#!/usr/bin/env python3
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```

**关于搜索**

```bash
tldr convert
# about find
find . -name src -typd d
find '**/test/*.py' -type f
find . -mtime -1
find. -name "*.tmp" -exec rm {}\;
find . -name "*.tmp"
# or
locate
grep -R
rg
fd
fzf
tree
broot

# about history
history 1 | grep convert
# or Ctrl+R and search and Ctrl+R to explore
```