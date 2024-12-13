# CSC 461 Programming Languages - Assignment #6 (Fall 2024)
## Overview
- **Instructor**: Dr. Stephen Krebsbach
- **Points**: 15 points
- **Due Date**: Tuesday, December 17th, 11:59 PM
## Objective
Develop basic Lisp functions based on the provided starting file, `start.lsp`.

---
## Steps to Complete the Assignment
1. **Download `start.lsp`**
    - Provided as a starting point.
2. **Rename the File**
    - Rename `start.lsp` to `cid##.lsp`, replacing `##` with your **Class ID (CID)**. For example:
        - If CID = 47, rename the file to `cid47.lsp`.
3. **Edit the File**
    - Replace `(print "your name")` with your actual name.
    - Do not modify the pre-defined testing variables.
4. **Complete the Functions**
    - Use the provided header comment blocks to guide your implementation.
    - Ensure the code works as specified without modifying the predefined test cases or adding higher-level Lisp functions.
5. **Test the Functions**
    - Verify that all functions produce correct outputs with the provided test variables.
6. **Submit the File**
    - Submit the final Lisp file into the dropbox.
    - Ensure the file can load and execute in Lisp without further modifications.

---
## Test Variables

The following `setq` variables are pre-defined for testing:
- **`A`**: `(setq A '((1 2) 3 (2 3 (1 9))))`
- **`B`**: `(setq B '(1 2 3 4 5))`
- **`C`**: `(setq C '((1 2) ((3)) 4 (5)))`
- **`D`**: `(setq D '(1 2 (6 3) 4 5))
- **`Empl`**: `(setq Empl '( (10 Mary Smith 36 12) (5 Bob Olsen 33 12) (130 Lace Smith 44 16)))`

### A
```lisp
(setq A
	'(
		(1 2) 3 (2 3 (1 9))
	)
)
```

### B
```lisp
(setq B
	'(
	1 2 3 4 5
	)
)
```

### C
```lisp
(setq C
	'(
		(1 2)
		((3))
		4
		(5)
	)
)
```

### D:
```lisp
(setq D
	'(
		1
		2
		(6 3)
		4
		5
	)
)
```

### Empl:
```lisp
(setq Empl
	'(
		(10 Mary Smith 36 12)
		(5 Bob Olsen 33 12)
		(130 Lace Smith 44 16)
	)
)
```
---

## 1. `lookupEmpl`

- **Description**: Retrieve an employee's record by their key from the `Empl` database.
- **Input**:
    - `Empl`: A list of employee tuples.
    - `Key`: The unique key for the employee.
- **Output**:
    - Employee record if found.
    - `'NOT FOUND` if no match.
- **Example**:
    ```lisp
    (lookupEmpl Empl 10) ; Returns: (10 Mary Smith 36 12)
    ```
### Source code
```lisp
;****** lookupempl ***************
; returns values related to the Key value of an
; employee tuple defined as (KEY# Fname Lname Age Dept#)
; Example: employe tuple --> (10 Mary Smith 36 12)
; A databasee list called Empl will contanin several Employees
; the funtion lookupEmpl will use the Key to return the Emply record list
; of the employee.
; If no employee match return 'NOT FOUND.
; Example: (lookupempl Empl 10) --> (10 Mary Smith 36 12)
;********************************
```
---
## 2. `doubleOdd`
- **Description**: Doubles all odd numbers in a single-level list.
- **Input**: A single-level list.
- **Output**: A list with odd numbers doubled.
- **Example**:
    ```lisp
    (doubleOdd B) ; Returns: (2 2 6 4 10)
    ```
### Source code
```lisp
;****** Doubleodd ***************
; Doubleodd: return a list where all the odd numbers have been doubled.
; Example: (doubleodd B) --> (2 2 6 4 10)
; Assume single level list
;********************************
```

---
## 3. `addAll`
- **Description**: Computes the sum of all positive integers in a nested list.
- **Input**: A nested list.
- **Output**: Sum of positive integers or `0` if the list is empty.
- **Example**:
    ```lisp
    (addAll C) ; Returns: 15
    ```
### Source code
```lisp
;****** addAll ******************
; addall: returns the sum of nested list of positive integers
; Example: (addAll C) --> 15
; Return 0 if the list is empty
; Assume that it may be a nested level list
;********************************
```


---
## 4. `large_atom`
### Optional Function (Extra Credit)
- **Description**: Finds the largest value greater than 0 in a nested list.
- **Input**: A nested list.
- **Output**: Largest value greater than 0, or `0` if the list is empty.
- **Example**:
    ```lisp
    (large_atom D) ; Returns: 6
    ```
- **Note**: Avoid using higher-level functions like `max`.
### Source code
```lisp
;----- OPTIONAL (do not have to do) ------------------
;****** large_atom ***************
; large_atom : returns the largest value greater than 0
; in a nested list of positive integers
; Example: (large_atom D) --> 6
; Return 0 if the list is empty
; Assume that it may be a nested level list
; DO NOT use higher level funtions like max ..
;
; THIS SHOULD BE THE HARDER ONE :)
;*********************************
```

---
### Guidelines
- Adhere to Lisp syntax and the constraints of the assignment.
- Avoid using advanced Lisp functions for assistance, such as `max` or `member`.
- Ask questions if anything is unclear.
Good luck!