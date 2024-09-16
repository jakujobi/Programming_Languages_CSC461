# Question
**ASS #1**
**CSC 461 Programming Languages**  
**FALL 2024**  
Dr. Stephen Krebsbach
---
**Ass #1: 10 points**  
**Due: Monday Sept. 16th 11:59 PM**  
(Talk to me if that is a problem)

---
### Assignment Instructions:
**Objective:**  
Create a complete pseudo-code program to perform the following tasks using the PseudoCode language developed in class, with **Absolute Addressing**.

---
### Deliverables:
1. Submit your source code in a file named `A1.dat`.  
   You should include the input cards shown below in the program as a test.

---
### The Program:

1. **Input**:  
   First, read a value **N** (range of 5-500), which indicates the number of values to be read and sorted in ascending order.  
   (If **N** is 20, there will be 20 more cards to read).
2. **Array Setup**:  
   Read the values into an array.
3. **Bubble Sort Algorithm**:  
   Sort the array using the Bubble Sort algorithm. You are required to use the modified version of Bubble Sort provided below (which uses bottom-tested loops, as supported by the class language using the `Incr` & `Test` construct).

```pseudocode
    int i; 
    int j; 
    int t; 

    i = 0; 
    do                           
    { 
        j = 0;  
        do 
        { 
            if (A[j] > A[j+1]) 
            { 
                t = A[j]; 
                A[j] = A[j+1]; 
                A[j+1] = t; 
            }    
            j++;         
        } while(j < N-1);           

        i++; 
    } while(i < N-1); 
```

4. **Output 1**:  
   After sorting the values, print them out in ascending order.

5. **Output 2**:  
   Finally, print the values that lie between **50 and 150 (inclusive)** in ascending order.

---
### Input Cards:

You should use the following input cards for your test and include them in your file:

```
10  
94  
150  
113  
37  
63  
160  
128  
235  
117  
1
```

```yaml
+0000000010   // N = 10
+0000000094   // First value
+0000000150   // Second value
+0000000113   // Third value
+0000000037   // Fourth value
+0000000063   // Fifth value
+0000000160   // Sixth value
+0000000128   // Seventh value
+0000000235   // Eighth value
+0000000117   // Ninth value
+0000000001   // Tenth value
```

---

### Expected Output:
1. **Sorted Values**:  
   ```
   1  
   37  
   63  
   94  
   113  
   117  
   128  
   150  
   160  
   235
   ```

2. **Values Between 50 and 150**:  
   ```
   63  
   94  
   113  
   117  
   128  
   150
   ```

---

Define the variables
- First Loop start
- Assign j to 0
- second loop start
- If aj larger start
- check if j'th item in array A is larger than (j+1)th item in Array A
- if it is larger , then jump to swap
- Swap start
	- move jth item to temporary spot
	- move (j+1)th item to jth spot
	- move temp to (j+1)spot

Program start
- make a place for i
- make a place for j
- make a place for t
- place 0 into i
- read N and store
	- Loop for going through array
	- 



### Data Area (Addresses 000-999)

| **Address** | Value       | Label  | Comment               |
| ----------- | ----------- | ------ | --------------------- |
| **000**     | +0000000000 | 0      | Zero Constant         |
| **001**     | +0000000001 | 1      | One Constant          |
| **002**     | +0000000000 | i      | Outer Loop Index      |
| **003**     | +0000000000 | j      | Inner loop index      |
| **004**     | +0000000000 | T      | Outer loop index      |
| **005**     | +0000000000 | N      | temp for swapping     |
| **006**     | +0000000000 | N-1    | calculated as N-1     |
| **007**     | +0000000050 | 50     | Fifty constant        |
| **008**     | +0000000150 | 150    | 150 constant          |
| **009**     | +0000000000 | TEMP   | just a general temp   |
| **010**     | +0000000000 | j+1    |                       |
| **011**     | +0000000000 | A[j]   | jth item in array     |
| **012**     | +0000000000 | A[j+1] | (j+1)th item in array |
| **013**     | +0000000000 | 151    | 151 (calc as 150 +1)  |
| **014**     | +0000000000 | 49     | unused                |
| **015**     | Unused      |        |                       |
| **...**     | .......     |        |                       |
| **999**     | Unused      |        |                       |

### Input Data

| **Item**        | Value | Label   | Comment |
| --------------- | ----- | ------- | ------- |
| **+0000000010** | 10    | N = 10  |         |
| **+0000000094** | 94    | First   |         |
| **+0000000150** | 150   | Second  |         |
| **+0000000113** | 113   | Third   |         |
| **+0000000037** | 37    | Fourth  |         |
| **+0000000063** | 63    | Fifth   |         |
| **+0000000160** | 160   | Sixth   |         |
| **+0000000128** | 128   | Seventh |         |
| **+0000000235** | 235   | Eighth  |         |
| **+0000000117** | 117   | Ninth   |         |
| **+0000000001** | 1     | Tenth   |         |

Read N and Calculate N-1

Read Values into Array A

Prep i and j to 0 for sorting

/table
### Code Are

| Address | Value       | Label         | Comment                           |
| ------- | ----------- | ------------- | --------------------------------- |
|         |             | **Read_N**    | **Read N and calculate N-1**      |
| 1000    | +8000000005 |               | Read N into address 005           |
|         | -1001005006 |               | Calc  N-1, store into 006         |
|         |             |               | Set 1 = 0                         |
|         |             |               |                                   |
|         |             | **Fill_A**    | **Read values into Array A**      |
|         |             |               | Read value into TEMP              |
|         |             |               | Store temp into A[i]              |
|         |             |               | Increment i                       |
|         |             |               | If (i<N) jump to Fill_A           |
|         |             |               |                                   |
|         |             | **Set_i_j_0** | **Prep i and j to 0**             |
|         |             |               | set i=0                           |
|         |             |               | set j=0                           |
|         |             |               |                                   |
|         |             | Out_loop      |                                   |
|         |             |               | set j=0                           |
|         |             |               |                                   |
|         |             | In_loop       |                                   |
|         |             |               | Calc j+1 into (j+1)               |
|         |             |               | put A[j] into A[j]                |
|         |             |               | put A[j+1] into A[j+1]            |
|         |             |               | if If A[j] ≥ A[j+1], jump to swap |
|         |             | Incre_J       | Increment j                       |
|         |             |               | if j < N-1, jump to In_loop       |
|         |             |               | increment i++                     |
|         |             |               |                                   |
|         |             | Swap          |                                   |
|         |             |               | put A[j] into t                   |
|         |             |               | put A[j+1] into A[j]              |
|         |             |               | put t into A[j+1]                 |
|         |             |               | jump back to Incre_ j             |
|         |             |               |                                   |
|         |             |               | increment i                       |
|         |             |               | if (i<N-1), jump to Outloop       |
|         |             |               |                                   |
|         |             |               |                                   |
|         |             | P_Sorted      | Print Sorted Array                |
|         |             |               | Set i to 0                        |
|         |             |               |                                   |
|         |             | P_S_loop      | Move A[i] into TEMP               |
|         |             |               | print TEMP                        |
|         |             |               | increment i                       |
|         |             |               | if (i<N), jump to P_S_loop        |
|         |             |               |                                   |
|         |             | F_50_150      | filter values between 50 & 150    |
|         |             |               | Set i to 0                        |
|         |             |               | Calc 50-1 and store in 49 spot    |
|         |             |               | Calc 150+1 into 151 spot          |
|         |             | Check_50      |                                   |
|         |             |               | Load A[i] into TEMP               |
|         |             |               | if A[i]>49 jump to Check_150      |
|         |             |               | increment i                       |
|         |             |               | if i<N, jump to Check_50          |
|         |             | Check_150     |                                   |
|         |             |               | if A[i] < 151, jump to P_Range    |
|         |             |               | increment i                       |
|         |             |               | if (i<N), jump to Check_50        |
|         |             |               |                                   |
|         |             | P_Range       |                                   |
|         |             |               | print TEMP                        |
|         |             |               | increment i                       |
|         |             |               | if (i<N) jump to Check_50         |
|         |             |               |                                   |
|         |             | Terminate     |                                   |
|         |             |               | Stop the program                  |

