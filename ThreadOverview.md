Name: Rohith Yeedulapalli

Course: 5143 Operating Sysytems

Date: 08 April 2016

Mustang ID: M20227640

Question 1

Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

Threads1.py 
 This thread contains threads which runs independently, it is not necessary to access the same memory space at any point when they are executing.
the threads have copies of same local variables.
Threads2.py
 This thread uses a global variable shared counter. During execution at some point, the two threads try to access together. This leads to race condition.


  

Question 2

After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

The code Threads3.py will fix the race condition in Threads2.py.  This is done by using unlock method in which any one of the threads gets area, where they can have access to the global variables,
the thread at that point of time locks this access to the variable till the process is completed. After this it unlocks or releases the variable. This process of locking and unlocking the variable increases the execution time


Question3

Comment out the join statements at the bottom of the program and describe what happens.

If join is present then the main program will execute after execution is done. If this is not present then abnormal execution takes place. From this we can infer that join 
is used so that it waits for complete execution of threads and then completes execution of main.

Question 4

What happens if you try to Ctrl-C out of the program before it terminates?

If Ctrl-C is done, the program doesn't terminate. It keeps executing.

Question 5

Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

Here, every thread tries to initiate or assign a value to the variable. This is complex because when a thread requests for the global variable, another thread may be already
working on that global variable and this may lead to situation where the contents are altered. This gives incorrect value to the thread which is requesting resource. So, in this situation both threads keep on running
resulting in incorrect values.

Question 6

Does uncommenting the lock operations clear up the problem in question 5?

Yes when the lock section is uncommented, each thread has a indvidual right to sharedNumber at a specific point in time and No thread will print because
they both have correct values at each point in the execution.
