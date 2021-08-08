# SED command

## Table of Contents

1. <span style="color:lightblue">Introduction</span>
   1. <span style="color:lightblue">What is SED ?</span>
   2. <span style="color:lightblue">How SED command is invoked ?</span>
2. <span style="color:lightblue">Commands</span>
   1. <span style="color:lightblue">Replacing or Substituting</span>
   2. <span style="color:lightblue">Deleting</span>
   3. <span style="color:lightblue">File Spacing</span>
   4. <span style="color:lightblue">View or Print Lines</span>
3. <span style="color:lightblue">References</span>

<br />


# Introduction


## What is SED command ?

* Sed command is Short for stream editor that allows searching, find and replace, insertion or deletion.
* Most commonly sed command is used for substitution or for finding replace.
* It allows you to edit a file without opening it which is much quicker way to find and replace something in file, than opening a editior and then changing it.

<br><br>

## How SED command is Invoked?

```
$ sed OPTIONS... [Script] [InputFile...]
$ man sed  
```

<br />

# Commands

## 1 . **Replacing or substituting**
   
   ### **Examples** 
   **consider below text file as an input.**

```
$ cat > test.txt
unix is great os. unix is opensource. unix is free os.
learn operating system.
unix linux which one you choose.
unix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```
   <br> <br>
   

### **Example 1 : suppose you need to replace unix with linux**

```
$ sed 's/unix/linux/' test.txt
linux is great os. unix is opensource. unix is free os.
learn operating system.
linux linux which one you choose.
linux is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

   <br> 
   <h3> Here the “s” specifies the substitution operation. The “/” are delimiters. The “unix” is the search pattern and the “linux” is the replacement string.
   
   By default, the sed command replaces the first occurrence of the pattern in each line and it won’t replace the second, third…occurrence in the line.
   </h3>
   
   <br> <br>

   ### **Example 2 : If you want to replace the nth occurence of a word in a line**

```
$ sed 's/unix/linux/3' test.txt
unix is great os. unix is opensource. linux is free os.
learn operating system.
unix linux which one you choose.
unix is easy to learn.unix is a multiuser os.Learn linux .unix is a powerful.
```
   
   <br> <br>
   
   ### **Example 3 : If you want to replace all the occurence of a word in a line**

```
$ sed 's/unix/linux/g' test.txt
linux is great os. linux is opensource. linux is free os.
learn operating system.
linux linux which one you choose.
linux is easy to learn.linux is a multiuser os.Learn linux .linux is a powerful.
```
<br> <br>

### **Example 4 : Replacing string on a specific line number**

   ```
   $ sed '1 s/unix/linux/' test.txt
   linux is great os. unix is opensource. unix is free os.
   learn operating system.
   unix linux which one you choose.
   unix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
   ```
<br> <br>


### **Example 5 : Replacing strings on a range of a lines**

```
$ cat numbers.txt
one
two
three
four
five
six
seven
eight
nine
ten
```

```
$ sed '3,7 s/.*/replaced/g' numbers.txt
one
two
replaced
replaced
replaced
replaced
replaced
eight
nine
ten
```

<br> <br>

## 2 . **Deleting**

### **Examples**

**We can take the previous numbers.txt file for this example**

### **Example 1 : Suppose, you want to delete a particular line.**

```
$ sed '4d' numbers.txt
one
two
three
five
six
seven
eight
nine
ten
```

<h3>So in the above example "d" flag is used for deleting, and the number specified here is the nth line in this case 4th line.<h3>


<br><br>

### **Example 2 : To delete lines in range.**

```
$ sed '3,5d' numbers.txt
one
two
six
seven
eight
nine
ten
```

<br><br>

### **Example 3 : To delete line containing the word.**

```
$ sed '/three/d' numbers.txt
one
two
four
five
six
seven
eight
nine
ten
```

<br> <br>

## 3 . **File Spacing**

### **Examples**

### **Example 1 : Insert One blank line after each line.**

```
$ sed G numbers.txt
one

two

three

four

five

six

seven

eight

nine

ten

```

<br><br>


### **Example 2 : Insert One blank line after each line.**

```
$ sed "G;G" numbers.txt
one


two


three


four


five


six


seven


eight


nine


ten


```
<br><br>

### **Example 3 : Delete Blank lines**

```
$ sed '/^$/d' numbers.txt
one
two
three
four
five
six
seven
eight
nine
ten
```

<br> <br>

### **Example 4 : insert a line for every matching pattern**

```
$ sed '/three/{x;p;x;}' numbers.txt
one
two

three
four
five
six
seven
eight
nine
ten
```

<br><br>

## 4 . **View/Print lines**

### **Examples**

### **Example 1 : print the content within a range.**
```
$ sed -n '2,5p' numbers.txt
two
three
four
five
```

<br><br>

### **Example 2 : print the nth line.**

```
$ sed -n '4'p numbers.txt
four
```

<br> <br>

### **Example 3 : print from the nth line to end of a file.**

```
$ sed -n '6,$'p numbers.txt
six
seven
eight
nine
ten
```

<br> <br>
   
### **Example 4 : print the line which matches pattern.**

```
$ sed -n '/is/p' test.txt
unix is great os. unix is opensource. unix is free os.
unix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

<br> <br>
   
### **Example 5 : Duplicating the lines with /p flag**

```
$ sed '/.*/p' test.txt
unix is great os. unix is opensource. unix is free os.
unix is great os. unix is opensource. unix is free os.
learn operating system.
learn operating system.
unix linux which one you choose.
unix linux which one you choose.
unix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
unix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```
    
<br> <br>


## **References**

* https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/
* https://www.geeksforgeeks.org/sed-command-linux-set-2/
* https://www.gnu.org/software/sed/manual/sed.html
* https://www.youtube.com/watch?v=EACe7aiGczw&ab_channel=DistroTube



   
