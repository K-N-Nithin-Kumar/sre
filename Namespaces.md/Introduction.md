# NAMESPACES

   ``` 
   Namespaces are a feature of the Linux kernel that partitions kernel resources such that one set of processes sees one set of resources.
   And another set of processes sees a different set of resources.
   ```
   
   ```
   The feature works by having the same namespace for a group of resources and processes, but those namespaces refer to distinct resources.
   ```
   
   ```
 Example Elaboration-1.
 
 Consider my apartment building. It's technically two distinct buildings with their own entrances. 
 However, the parking garage, gym, pool, and common rooms are shared
 The buildings have their own names, City Place and City Place 2. 
 They have their own street addresses, floors, and elevators.Yet, they are attached to the same physical complex.
 ```

Example One![image](https://user-images.githubusercontent.com/43216503/118993892-83faed80-b9a3-11eb-928c-359321164542.png)




```
The physical complex is the same idea as a computer. Two namespaces (or more) can reside on the same physical computer.
And much like the apartment building, namespaces can either share access to certain resources or have exclusive access.
```

```
Example Elaboration-2.

Recently, there has been a growing number of programming contest and “hackathon” platforms such as HackerRank, TopCoder, Codeforces, and many more. 
A lot of them utilize automated pipelines to run and validate programs that are submitted by the contestants.

It is often impossible to know in advance the true nature of contestants’ programs, 
and some may even contain malicious elements. By running these programs namespaced in complete isolation from the rest of the system.
the software can be tested and validated without putting the rest of the machine at risk.
By this way  it is possible to safely execute arbitrary or unknown programs on your server.

```

```
Linux namespaces allow other aspects of the operating system to be independently modified as well. 
This includes the process tree, networking interfaces, mount points, inter-process communication resources and more
```

```
The unshare command allows you to run a program with some namespaces ‘unshared’ from its parent. 
Essentially what this means is that unshare will run whatever program you pass it in a new set of namespaces.

```

```
$ unshare -h

Usage:  
 unshare [options] <program> [<argument>...]

Run a program with some namespaces unshared from the parent.

Options:  
 -m, --mount[=<file>]      unshare mounts namespace
 -u, --uts[=<file>]        unshare UTS namespace (hostname etc)
...
```




