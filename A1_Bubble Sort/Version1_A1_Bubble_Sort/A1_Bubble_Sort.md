# Question

**ASS #1**
**CSC 461 Programming Languages**
**FALL 2024**
Dr. Stephen Krebsbach
---------------------

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

1. **Input**:First, read a value **N** (range of 5-500), which indicates the number of values to be read and sorted in ascending order.(If **N** is 20, there will be 20 more cards to read).
2. **Array Setup**:Read the values into an array.
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

4. **Output 1**:After sorting the values, print them out in ascending order.
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

| Value       | **Address** | Label    | Comment               |
| ----------- | ----------- | -------- | --------------------- |
| +0000000000 | **000**     | 0        | Zero Constant         |
| +0000000001 | **001**     | 1        | One Constant          |
| +0000000000 | **002**     | i        | Outer Loop Index      |
| +0000000000 | **003**     | j        | Inner loop index      |
| +0000000000 | **004**     | t        | Temp for swapping     |
| +0000000000 | **005**     | N        | Number of elements    |
| +0000000000 | **006**     | N-1      | calculated as N-1     |
| +0000000050 | **007**     | 50       | Fifty constant        |
| +0000000150 | **008**     | 150      | 150 constant          |
| +0000000000 | **009**     | TEMP     | just a general temp   |
| +0000000000 | **010**     | j+1      |                       |
| +0000000000 | **011**     | A[j]     | jth item in array     |
| +0000000000 | **012**     | A[j+1]   | (j+1)th item in array |
| +0000000000 | **013**     | 151      | 151 (calc as 150 +1)  |
| +0000000000 | **014**     | unused   | unused                |
| +0000000000 | **015**     | A[Base}] | Base of A             |
| .......     | **...**     |          |                       |
| Unused      | **999**     |          |                       |

### Input Data

| **Item**        | Value | Label   | Comment |
| --------------------- | ----- | ------- | ------- |
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
+0000000010
+0000000094
+0000000150
+0000000113
+0000000037
+0000000063
+0000000160
+0000000128
+0000000235
+0000000117
+0000000001
### Code Are

| Address | Value       | Label                  | Comment                                               |
| ------- | ----------- | ---------------------- | ----------------------------------------------------- |
|         |             | **Read_N**             |                                                       |
| 1000    | +8000000005 | Read input             | Read N into address 005                               |
| 1001    | -1005001006 | Sub                    | Sub  N(005) - 1(001), store into N-1(006)             |
| 1002    | +0000000002 | Move                   | Move 0(000) to i (002)                                |
|         |             |                        |                                                       |
|         |             | **Fill_A_with_Values** | **Read values into Array A**                          |
| 1003    | +8000000009 | Read                   | Read value into TEMP(009)                             |
| 1004    | -6009015002 | Array store            | Move TEMP(009) into ABase(015) at i (002)             |
| 1005    | +1001002002 | Add                    | Increment i(002)+ 1(001) into i(002)                  |
| 1006    | -5002005003 | < jump                 | If (i(002)<N(005) ) jump to Fill_A_with_Values(1003)  |
|         |             |                        |                                                       |
|         |             | **Set_i_0**            |                                                       |
| 1007    | +0000000002 | Move                   | Move 0(000) into i(002)                               |
|         |             |                        |                                                       |
|         |             | **Out_loop**           |                                                       |
| 1008    | +0000000003 | Move                   | Move 0(000) into j(003)                               |
|         |             |                        |                                                       |
|         |             | **In_loop**            |                                                       |
| 1009    | +1001003010 | Add                    | Add j(003)+1(001) into (j+1)(010)                     |
| 1010    | +6015003011 | Load                   | load jth(003) item from A(015)  into A[j]011          |
| 1011    | +6015010012 | Load                   | load j+1th(010) item from A(015) into A[j+1]012       |
| 1012    | +5011012016 | ≥ jump                 | If A_j(011) ≥ A_j+1(012), jump to swap(1016)          |
|         |             | **Incre_J**            |                                                       |
| 1013    | +1001003003 | Add                    | Add 1(001) + j(003) into j(003)                       |
| 1014    | -5003006009 | < jump                 | if j(003) < N-1(006), jump to In_loop(1009)           |
| 1015    | +1002001002 | Add                    | Add i(002) + 1(001) into i(002)                       |
|         |             |                        |                                                       |
|         |             | **Swap**               |                                                       |
| 1016    | +0011000004 | Move                   | put A_j(011) into t (004)                             |
| 1017    | +0012000011 | Move                   | put A_j+1(012) into A_j(011)                          |
| 1018    | +0004000012 | Move                   | put t(004) into A_j+1(012)                            |
| 1019    | +4000000013 | <>jump                 | jump back to Incre_ j(1013) if 0(000) == 0(000)       |
|         |             |                        |                                                       |
| 1023    | +1002001002 | Add                    | Add i(002) + 1(001) into i(002)i to increment i       |
| 1024    | -5002006009 | < jump                 | if i(002) < N-1(006), jump to Out_loop(1009)          |
|         |             |                        |                                                       |
|         |             |                        |                                                       |
|         |             | **Print_Sorted**       |                                                       |
| 1025    | +0000000002 | Move                   | Move 0(000) into i(002)                               |
|         |             | **Print_Sorted_Range** |                                                       |
| 1026    | +6015002009 | load                   | load i(002) item from A(015)  into TEMP(009)          |
| 1027    | -8009000000 | Print                  | print TEMP(009)                                       |
| 1028    | +1002001002 | Add                    | Add i(002) + 1(001) into i(002)i to increment i       |
| 1029    | -5002005027 | < jump                 | if i(002) < N(005), jump to Print_Sorted_Range (1027) |
|         |             |                        |                                                       |
|         |             | **Filter_50_150**      |                                                       |
| 1030    | +0000000002 | Move                   | Move 0(000) into i(002)                               |
| 1031    | +0008001013 | Add                    | Calc 150(008) + 1(001) into 151(013) spot             |
|         |             | **Check_50**           |                                                       |
| 1032    | +6015002009 | Load                   | Load A[i] into TEMP(009)                              |
| 1033    |             | ≥ jump                 | if TEMP(009) ≥ 50(007) jump to Check_150(1035)        |
| 1034    | +1002001002 | Add                    | Add i(002) + 1(001) into i(002)i to increment i       |
| 1035    | -5002005035 | < jump                 | if i(002) < N(005), jump to Check_50(1035)            |
|         |             | **Check_150**          |                                                       |
| 1036    | -5009013038 | < jump                 | if TEMP(009) < 151, jump to Print_Sorted_Range(1038)  |
| 1037    | +1002001002 | Add                    | Add i(002) + 1(001) into i(002)i to increment i       |
| 1038    | -5002005032 | < jump                 | if (i(002) < N(005), jump to Check_50(1032)           |
|         |             |                        |                                                       |
|         |             | **Print_Sorted_Range** |                                                       |
| 1039    | -8009000000 | Print                  | print TEMP(009)                                       |
| 1040    | +1002001002 | Add                    | Add i(002) + 1(001) into i(002)i to increment i       |
| 1041    | -5002005032 | < jump                 | if (i<N) jump to Check_50(1032)                       |
|         |             |                        |                                                       |
|         |             | **Terminate**          |                                                       |
| 1042    | +9000000000 | Stop Ptogram           | Stop the program                                      |

| Value       | Address | Label        | Comment                                               |
| ----------- | ------- | ------------ | ----------------------------------------------------- |
| +8000000005 | 1000    | Read input   | Read N into address 005                               |
| -1005001006 | 1001    | Sub          | Sub  N(005) - 1(001), store into N-1(006)             |
| +0000000002 | 1002    | Move         | Move 0(000) to i (002)                                |
| +8000000009 | 1003    | Read         | Read value into TEMP(009)                             |
| -6009015002 | 1004    | Array store  | Move TEMP(009) into ABase(015) at i (002)             |
| +1001002002 | 1005    | Add          | Increment i(002)+ 1(001) into i(002)                  |
| -5002005003 | 1006    | < jump       | If (i(002)<N(005) ) jump to Fill_A_with_Values(1003)  |
| +0000000002 | 1007    | Move         | Move 0(000) into i(002)                               |
| +0000000003 | 1008    | Move         | Move 0(000) into j(003)                               |
| +1001003010 | 1009    | Add          | Add j(003)+1(001) into (j+1)(010)                     |
| +6015003011 | 1010    | Load         | load jth(003) item from A(015)  into A[j]011          |
| +6015010012 | 1011    | Load         | load j+1th(010) item from A(015) into A[j+1]012       |
| +5011012016 | 1012    | ≥ jump       | If A_j(011) ≥ A_j+1(012), jump to swap(1016)          |
| +1001003003 | 1013    | Add          | Add 1(001) + j(003) into j(003)                       |
| -5003006009 | 1014    | < jump       | if j(003) < N-1(006), jump to In_loop(1009)           |
| +1002001002 | 1015    | Add          | Add i(002) + 1(001) into i(002)                       |
| +0011000004 | 1016    | Move         | put A_j(011) into t (004)                             |
| +0012000011 | 1017    | Move         | put A_j+1(012) into A_j(011)                          |
| +0004000012 | 1018    | Move         | put t(004) into A_j+1(012)                            |
| +4000000013 | 1019    | <>jump       | jump back to Incre_ j(1013) if 0(000) == 0(000)       |
| +1002001002 | 1020    | Add          | Add i(002) + 1(001) into i(002)i to increment i       |
| -5002006009 | 1021    | < jump       | if i(002) < N-1(006), jump to Out_loop(1008)          |
| +0000000002 | 1022    | Move         | Move 0(000) into i(002)                               |
| +6015002009 | 1023    | load         | load i(002) item from A(015)  into TEMP(009)          |
| -8009000000 | 1024    | Print        | print TEMP(009)                                       |
| +1002001002 | 1025    | Add          | Add i(002) + 1(001) into i(002)i to increment i       |
| -5002005027 | 1026    | < jump       | if i(002) < N(005), jump to Print_Sorted_Range (1027) |
| +0000000002 | 1027    | Move         | Move 0(000) into i(002)                               |
| +0008001013 | 1028    | Add          | Add 150(008) + 1(001) into 151(013) spot              |
| +6015002009 | 1029    | Load         | Load A[i] into TEMP(009)                              |
| -5009007035 | 1030    | ≥ jump       | if TEMP(009) ≥ 50(007) jump to Check_150(1035)        |
| +1002001002 | 1031    | Add          | Add i(002) + 1(001) into i(002)i to increment i       |
| -5002005035 | 1032    |              | if i(002) < N(005), jump to Check_50(1029)            |
| -5002013038 | 1033    | < jump       | if TEMP(009) < 151, jump to Print_Sorted_Range(1038)  |
| +1002001002 | 1034    | Add          | Add i(002) + 1(001) into i(002)i to increment i       |
| -5002005032 | 1035    | < jump       | if (i(002) < N(005), jump to Check_50(1029)           |
| -8009000000 | 1036    | Print        | print TEMP(009)                                       |
| +1002001002 | 1037    | Add          | Add i(002) + 1(001) into i(002)i to increment i       |
| -5002005032 | 1038    | < jump       | if (i<N) jump to Check_50(1029)                       |
| +9000000000 | 1039    | Stop Program | Stop the program                                      |
