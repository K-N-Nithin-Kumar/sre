# PID-NAMESPACE.

```
Before jumping straight into the PID namespace 
  - I think it's a good idea to provide just a little bit of background as to why this namespace is important
```


```
When a process is created on most Unix-like operating systems.
It is given a specific numeric identifier called a process ID (PID).
This PID helps to identify a process uniquely even if there are two processes that share the same human-readable name. 
```
All of these processes are tracked in a special file system called `procfs`.

```
One of the main reasons for the PID namespace is to allow for process isolation.
```


---

```
Historically, the Linux kernel has maintained a single process tree. 
The tree contains a reference to every process currently running in a parent-child hierarchy. 
A process, given it has sufficient privileges and satisfies certain conditions.
can inspect another process by attaching a tracer to it or may even be able to kill it
```
---
```
With the introduction of Linux namespaces, it became possible to have multiple “nested” process trees.
Each process tree can have an entirely isolated set of processes. 
This can ensure that processes belonging to one process tree cannot inspect or kill
In fact cannot even know of the existence of - processes in other sibling or parent process trees
```
---

```
Every time a computer with Linux boots up, it starts with just one process, with process identifier (PID) 1.
This process is the root of the process tree, and it initiates the rest of the system by performing the 
appropriate maintenance work and starting the correct daemons/services.
All the other processes start below this process in the tree.

```

---

```
The PID namespace allows one to spin off a new tree, with its own PID 1 process. 
The process that does this remains in the parent namespace, in the original tree
but makes the child the root of its own process tree

```
---
```
With PID namespace isolation, processes in the child namespace have no way of knowing of the parent process’s existence. 
However, processes in the parent namespace have a complete view of processes in the child namespace
```

---
Screenshot 2021-05-20 at 8.51.13 PM![image](https://user-images.githubusercontent.com/43216503/119005637-3daa8c00-b9ad-11eb-8992-616f5e826f3b.png)

---

```
we have a process named 1 which is the first PID and from 1 parent process there are new PIDs are generated just like a tree. 
If you see the 6th PID in which we are creating a subtree, there actually we are creating a different namespace.
In the new namespace, 6th PID will be its first and parent PID

```

```
So the child processes of 6th PID cannot see the parent process or namespace but the parent process can see the child PIDs of the subtree.

```







