#Chapter 2 Review Questions
Name: Rohith Yeedulapalli
Course: 5143 Operating Systems
Date:17 Feb 2016

##1.What are three objectives of an OS design?

The Objectives of an OS design are:
1.Efficiency
2.Maintainabilty
3.Security

1.EFFICIENCY: The Operating System Should work in an efficient manner and uses the resources in the best way. It should be able to manage the hardware.
2.SECURITY: The Operating System should provide security to the resources and only authorized person can access the system.
3.MAINTAINABILITY:The Operating System should be able to accomadate any fixes relating to bugs in any computer program. It should be easy to maintain and upgrade.
   
##2.What is the kernel of an OS?

Kernel is computer program which acts as an interface between the application hardware and the software of the computer.
There are two different concepts of kernels:
monolithic kernel
micro kernel

##3.What is multiprogramming?

In multiprogramming system,when one program is waiting for I/O transfer, there is another program ready to utilize the CPU. 
So,it is defined as execution of jobs at the same instance of time. The execution of multiple jobs are done by the same computer.

##4What is a process?

Process is a unit of work which is implemented  within the program. 
Also a program which is in execution state is called process.


##5.How is the execution context of a process used by the OS?

A process invokes some OS services such as I/o device handlers by means of service calls and the service calls are handled short term scheduler is invoked to pick the process for execution.


##6.List and briefly explain five storage management responsibilities of a typical OS.

PROCESS ISOLATION:It prevents the data and instructions from interfering with other process.
LONG TERM STORAGE:Is a process whereby memory is stored for a long period of time even when the computer is switch off it is stored in the RAM.
SUPPORT OF MODULAR PROGRAMMING:It divides the programs to modules and to create,destroy and alter the size of modules dynamcally.
AUTOMATIC ALLOCATION AND MANEGEMENT:In this processs allocation is transparent to the programmer.Programs should be dynamically allocated.
PROTECTION AND ACESS CONTROL:This is the process of sharing memory this is desirable when sharing is needed by a particular application it also threatens the integrity of programs.

##7.Explain the distinction between a real address and a virtual address.

Real addresses are provided by the hardware:
It has only one real address space per machine;
valid addresses lies between 0 and some machine specific maximum

Virtual addresses are provided by the OS kernel:
It has one virtual address space per process.
The addresses may start at 0.

##8.Describe the round-robin scheduling technique.

It allocates equal time for all the jobs,each job is added to the circular queue. It arranges the elements usually from top to the bottom of a list and then starting again at the top of the list and so on.

##9.Explain the difference between a monolithic kernel and a microkernel.

All the parts of a kernel like the Scheduler, File System, Memory Management, Networking Stacks, Device Drivers, etc., are maintained in a one  unit within the kernel in Monolithic Kernel.
In Micro kernel the very important parts like IPC, basic scheduler, basic memory handling, basic I/O primitives etc., are put into the kernel. Communication happen via message passing. Others are maintained as server processes in User Space

##10.What is multithreading?

Multithreading is a parallel execution of applications on a shared memory multiprocessors. It is the ability of a program to manage its use by more than one user at a time and to even manage multiple requests by the same user.

##11.List the key design issues for an SMP operating system.

The key design issues for an SMP operating system are:
Synchronization
Memory Management
Simultaneous concurrent process
Reliability and fault tolerance
Scheduling
