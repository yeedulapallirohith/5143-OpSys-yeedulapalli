#Chapter 3 Review Questions
Name: Rohith Yeedulapalli	
Course: 5143 Operating Systems
Date: 02 Mar 2016

##3.4 What does it mean to preempt a process?

In the field of computing, the process of interrupting an assigned task being done by computer system temporarily or time-being and then will resume the task after while is called preemption. This change is called context switch. Normally, this will be carriedout by priviliged task or part of the system called preemptive scheduler, It has power for preemption, or interrupting, and later resume, other tasks in the computer system.

##3.5 What is swapping and what is its purpose?
The Memory management technique used by the operating system  by moving some blocked process to the secondary memory from the main memory to rise the utility of the processor is called swapping. This forms a queue of temporarily suspended process and the execution will be continued with new arriving pocess. So after this swapping process, the operating system will have two options for selection of process for execution.

##3.9 List three general categories of information in a process control block.
The three general categories of information in process control block are

Process identification data: It's a unique identification number for the process in a multiuser or a multitasking system,data like the identification of user, group identifier, has the process id of its relavant.

Processor state data:It defines the state of the process whenever it got suspended.Here new process is given a chance to and the running process is stopped.The kernal has to stop the execution of the running process and should notedown the values to hardware registers in PCB

Process control data: It is used to manage the process itself by the operating system.

##3.10 Why are two modes (user and kernel) needed?
Kernel Mode:
The kernal mode has all the access for the hardware without any restrictions. It can execute any instruction given by CPU and can reger any memory address. In general, kernal is assigned for lower-level, trusted functions of the operating system. Crashes in kernal mode will halt the entire PC.

User Mode:
Here, the executing code cannot access hardware directly or reference memory. This is more protected when compared to kernal, and when the crashes occur, they can be always recoverable. Mostly the code running on the computer will be executed in user mode only.

##3.12 What is the difference between an interrupt and a trap?
The term INTERRUPT belongs to hardware interrupts. These are caused by external hardware events usually by timer chip, I/O ports, CMOS, Expansion cards, peripheral devices such as keyboard, mouse, etc. So during the process of program execution, there causes some events that will temporarily halt the CPU from processing, these events are called interrupts. Where as TRAPS are the software-invoked interrupts.It is the transfer of control which is initialted by the programer itself.

##3.13 Give three examples of an interrupt.
In general, there are three kinds of interrupts.
1)Internal Interrupt: The internal interrupt will be occurred when there is some problm with the execution of program, like if there is some error in the program that is being executed, this causes interrupt called internal Interrupt.
2)Software Interrupt:It calls the system and interrupts the process. This is used for the process to execute someother process
3)External Interrupt:The External interrupt is caused by the external function like when the process in execution,then Input and Output Device request for any Operation and the CPU will Execute that instructions first 

##3.14 What is the difference between a mode switch and a process switch?
The changing of the currently running process without change in the running state.The process context switch involves saving more state information.A process context switch involves taking the currently executing process out of the Running state in favor of another process.
