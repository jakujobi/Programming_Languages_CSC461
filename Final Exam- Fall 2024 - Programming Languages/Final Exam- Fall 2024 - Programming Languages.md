# CSC 461 Programming Languages

## Final Exam

### Fall 2024 (Update 1)
#### Please complete the FINAL QUIZ by
12/16 : Monday - Final Exam Due 11:59 PM

Please answer the questions provided in this exam clearly and to your best ability. If you have questions
on any ambiguities on what is being asked, please contact me (email) as soon as possible for a
clarification.

By submitting the Quiz, YOU affirm that the work product you turn in on this Exam is yours alone and
you have not received help or advice from others. You understand that violation of this statement
not only violates Dakota State University student code of conduct, it also degrades the reputation of
the university and this program. By doing so it harms all the other students in this course and
across the university.

You understand that use of AI generated material is considered plagiarism and will result in a failing
grade for this exam.
**You should record your answers using the FINAL Quiz on D2L**

---
### Weird words
- Halverson Skip
- Halverson Illusion


---
## Q1-Q3: Formal Parameters can be conceptually classified as IN or OUT or INOUT.

Given the limited information one can get from looking at just this code and, assuming the code is being used correctly, what can you deduce from the following code in terms of classifying them?

```c
Function Foo(A, B, C)
begin
    A := B + C;    // add B to C and assign to A
    print(B);       // print out the value of B
    print(C);       // print out the value of C
    return B;       // return the value of B as the function value
end;
```
How would you BEST classify A, B, and C given this limited information?

### Q1 (3 pts): Variable A
- [ ]  a) IN
- [ ]  b) OUT
- [ ]  c) INOUT



### Q2 (3 pts): Variable B
- [ ]  a) IN
- [ ]  b) OUT
- [ ]  c) INOUT



### Q3 (3 pts): Variable C
- [ ]  a) IN
- [ ]  b) OUT
- [ ]  c) INOUT




---

## Q4 (3 pts): The passing of the Actual parameters to the Formal parameters raises several issues.
Though it is conceptually easy to use text replacement of the formal with the actual parameter when working with PASS-BY-NAME, the implementation can be complex.
### What is actually passed from the actual to the formal parameter?
- [ ]  a) Code to determine the address of the actual
- [ ]  b) Text of the actual to be substituted for the formal
- [ ]  c) A reference to the location of the actual
- [ ]  d) The value of the actual



---
## Q5 (3 pts): Some language X, requires all the Formal parameters to functions be in-mode only as a function call should only be used as part of a mathematical expression.

### Why would language X make such a strict requirement for functions?
- [ ]  a) So that the formal parameters cannot cause side effects
- [ ]  b) Because a function should return a value to the expression and should be used in it
- [ ]  c) So that a stack-dynamic variable is created




---
## Q6 (3 pts): A Closure is often used when passing a Function as a parameter. What is a Closure?
What is a closure? It is often used when passing a function as a parameter
- [ ]  a) A Halverson skip
- [ ]  b) A pairing of the function with its referencing environment
- [ ]  c) A method to skip over a level of scoping
- [ ]  d) A static to dynamic link pairing



---

## Q7 (3 pts): As discussed in class, the C-like assignment expression `x = 3;` has a side effect. What is it?
What is the side effect of the C-like assignment expression `x=3`
- [ ]  a) x is assigned the value 3
- [ ]  b) the expression evaluates to 3
- [ ]  c) it evokes the Halverson illusion
- [ ]  d) The Name binding for x is modified




---
## Q8 (3 pts): An Unambiguous grammar will always
- [ ]  a) have meaningful variable names
- [ ]  b) be well commented to help understand the code
- [ ]  c) have only one distinct parse tree
- [ ]  d) have a well-balanced parse tree





---
## Q9 (3 pts): The inclusion of the optional “else” with the “if” statement helps the user with reliability by enforcing __
How does the inclusion of the optional `else` with the `if` statement help the user with reliability? What does it enforce?
- [ ]  a) Mutual exclusion
- [ ]  b) The order of precedence
- [ ]  c) Type checking
- [ ]  d) Short-circuiting





---
## (VOIDED) Q10 (3 pts): The Pointer type is designed to be used for two distinct purposes. One is to allow Pass-by-Reference. The other is to ___
- [ ]  a) make code more readable
- [ ]  b) make code more reliable
- [ ]  c) access anonymous variables
- [ ]  d) provide a form of indirect addressing





---
## Q11 (3 pts): In what type of static-scoping languages are closures NOT useful?
- [ ]  a) Those that do not allow nested subprograms
- [ ]  b) Imperative
- [ ]  c) Those that allow nested subprograms
- [ ]  d) General-purpose






---
---

## Q12-15: For the following code, show the output for the 4 output statements (#1..#4) under the parameter passing method stated.

**Assume static scoping**

```c
PROGRAM EX1; 
int i;           // global 
int A[3];        // global {array starts at 1} 

	PROCEDURE P1(int x, int y) 
	BEGIN 
	    y := 2; 
	    i := 3; 
	END; 

BEGIN  // main
    A[1] := 6; A[2] := 12; A[3] := 11; 
    i := 2; 
    P1(A[i], i);           // first call 
    PRINT(i);              // #1 prints value of i 
    PRINT_A(A);            // #2 assume function that prints all the values found in the array A 
    i := 1; 
    P1(i, A[i]);           // second call 
    PRINT(i);              // #3 prints value of i 
    PRINT_A(A);            // #4 assume function that prints all the values found in the array A 
END.
```

**Assumptions:**
- `x` is passed by **Name**.
- `y` is passed by **Reference**.

### Workng
- The code looks like Pascal
- But also kind of like C

#### Breaking down the code
```
PROGRAM EX1; 
	// Declaring Variables but kind of like constants
	int i;           // global 
	int A[3];        // global {array starts at 1} 

		// A function called P1
		// Actually doesn't do anything to caller x and y
		// Since they are passed in as value
		// but wierd that it takes x but does not do anything with it
		PROCEDURE P1(int x, int y) 
		BEGIN 
		    y := 2; // The change doesn't affect the caller y
		    i := 3; // It updates this variable called i
		END; 
	
	BEGIN  // main
		// Initialize the array
	    A[1] := 6; A[2] := 12; A[3] := 11; 
	    i := 2; 
	    P1(A[i], i);           // first call 
	    PRINT(i);              // #1 prints value of i 
	    PRINT_A(A);            // #2 assume function that prints all the values found in the array A 
	    i := 1; 
	    P1(i, A[i]);           // second call 
	    PRINT(i);              // #3 prints value of i 
	    PRINT_A(A);            // #4 assume function that prints all the values found in the array A 
END.
```

- So, i will fixit up to look more like pascal, and run it



---
### Q12 (2 pts):
### **#1**: Output of `PRINT(i);`

- [ ] a) 3
- [ ]  b) 4
- [ ]  c) 2
- [ ]  d) None of the others

---
### Q13 (2 pts):
### **#2**: Output of `PRINT_A(A);`
- [ ]  a) 6 12 12
- [ ] b) 6 12 11
- [ ]  c) 2 11 12
- [ ] d) None of the others




---
### Q14 (2 pts):
### **#3**: Output of `PRINT(i);`
- [ ]  a) 3
- [ ]  b) 4
- [ ]  c) 2
- [ ] d) None of the others




---
### Q15 (2 pts):
### **#4**: Output of `PRINT_A(A);`
- [ ] a) 2 12 11
- [ ]  b) 6 12 11
- [ ]  c) 11 11 11
- [ ]  d) None of the other answers



---
---

## Q16 (3 pts): What does this evaluate to in Lisp?

```lisp
(car (cdr (cdr '( (Happy New Year) Toys ((Merry X-Mas) to you) Dec25 Break yea!))))
```

```lisp
(car
	(cdr
		(cdr
			'(
				(Happy New Year)
				 Toys
				(
					 (Merry X-Mas)
					 to you
				)
				 Dec25 Break yea!
			 )
		)
	)
	 
)
```
### Options:

- [ ]  a) `(Dec25 Break yea!)`
- [ ]  b) `(Merry X-Mas)`
- [ ]  c) `Merry X-Mas to you`
- [x] d) `((Merry X-Mas) to you)` ✅ 2024-12-13
- [ ]  e) None of the others

---

## Q17 (3 pts): How many members are in the following Lisp list?

```lisp
( (a b (c (d f)) c (((y (f))) ) ) )
```

```lisp
(
	 (
		a
		b
		(
			c
			(
				d
				f
			)
		) 
		c
		(
			(
				(
					y 
					(f)
				)
			)
		)
	)
)
```
### Options:

- [ ]  a) 1
- [ ]  b) 2
- [ ]  c) 8
- [ ]  d) 3
- [ ]  e) None of the others

---

## Fig 1: Scope Diagram for Program P
![](Fig%201-Scope%20Diagram%20for%20Program%20P.png)
Assume Program P always starts in **MAIN**.

The image represents a **scope diagram** for a program labeled "Program P."
### Global Scope
- The topmost section is labeled **GLOBAL**. It contains three variables:
    - **X**
    - **A**
    - **B**
These variables are declared globally and accessible to all functions, unless shadowed by local variables with the same name.
---
### Functions and Their Scopes
Below the GLOBAL scope, there are several nested rectangles representing functions and their local variable scopes. Each function is outlined and contains variables specific to that function:
1. **MAIN (Outer Function)**
    - The bottom-most rectangle is labeled **MAIN**, representing the starting point of the program.
    - **MAIN** has one variable: **X**. This variable exists in the local scope of MAIN and can shadow the global variable **X**.
2. **F1 (Nested inside MAIN)**
    - A rectangle labeled **F1** is nested inside MAIN. This represents the scope of function **F1**.
    - **F1** has one local variable: **W**.
    - Inside **F1**, there are two other functions nested further:
        - **F3 (Nested inside F1)**:
            - A rectangle labeled **F3** is nested within F1.
            - **F3** has one local variable: **A**.
            - This **A** can shadow both the global **A** and any other **A** in an outer scope.
        - **F4 (Nested inside F1)**:
            - A rectangle labeled **F4** is also nested within F1.
            - **F4** has one local variable: **B**.
            - This **B** can shadow both the global **B** and any other **B** in an outer scope.
3. **F2 (Independent Function)**
    - Another rectangle labeled **F2** is shown at the same level as MAIN but not nested inside it. This suggests that **F2** is a standalone function, not called or defined inside MAIN.
    - **F2** has two local variables:
        - **A**
        - **B**
    - These variables exist only in the local scope of **F2** and shadow the global **A** and **B**.
---
### Key Assumptions
- The program always starts in the **MAIN** function.
- Variables in inner scopes can shadow variables of the same name in outer or global scopes.
---
### Overall Layout
- The diagram is structured hierarchically to visually represent the scoping rules and nesting of functions.
- Global variables are at the topmost level, accessible throughout unless shadowed.
- Functions are nested inside MAIN or other functions, with rectangles showing their respective local variables and scope boundaries.


---

## Q18 (3 pts): In Fig 1, using STATIC Scoping, what is the referencing environment if in MAIN?

### Options:
- [ ]  a) `{Global: (A and B), MAIN:X}`
- [ ]  b) `{MAIN: X, F1:W, F3:A, F4:B}`
- [ ]  c) `{Global: A, MAIN: X, F1:W, F4:B}`
- [ ]  d) `{Global: (X and A), F1:W, F4:B}`
- [ ]  e) Can’t tell by looking at Fig 1




---
## Q19 (3 pts): In Fig 1, assuming the program starts executing in MAIN and then calls F1, which then calls F3, using STATIC Scoping, what is the referencing environment if in F3?

### Options:
- [ ]  a) `{Global: (X and B), F1:W, F3:A}`
- [ ]  b) `{MAIN: X, F1:W, F3:A, F4:B}`
- [ ]  c) `{Global: A, MAIN: X, F1:W, F4:B}`
- [ ]  d) `{Global: (X and B), F1:W, F4:B}`
- [ ]  e) Can’t tell by looking at Fig 1




---
## Q20 (3 pts): In Fig 1, assuming the program starts executing in MAIN and then calls F1, which then calls F2. Using DYNAMIC Scoping, what is the referencing environment if in F4?

### Options:

- [ ]  a) `{Global: (X and A and B), F1:W, F4:B}`
- [ ]  b) `{MAIN: X, F1:W, F3:A, F4:B}`
- [ ]  c) `{Global: A, MAIN: X, F1:W, F4:B}`
- [ ]  d) `{MAIN: X, F1:W, F2: (A and B)}`
- [ ]  e) Can’t tell by looking at Fig 1



---
## Q21 (3 pts): In Fig 1, assuming the program starts executing in MAIN and then calls F2, which then calls F1, which then calls F3, that then calls F4. Using STATIC Scoping, what variables are “ALIVE” if in F4?

### Options:
- [ ]  f) `{Global: (X and A and B), F1:W, F4:B}`
- [ ]  g) `{Global: (X and A and B), MAIN: X, F2: (A and B), F1:W, F3: A, F4:B}`
- [ ]  h) `{Global: A, MAIN: X, F1:W, F4:B}`
- [ ]  i) `{Global: (X and A), F1:W, F4:B}`
- [ ]  j) Can’t tell by looking at Fig 1



---
## Q22 (3 pts): In Fig 1, assuming the program starts executing in MAIN and then calls F1, which then calls F3, that then calls F4. Using DYNAMIC Scoping, what variables are “ALIVE” if in F4?

### Options:
- [ ]  a) `{Global: (X and A and B), F1:W, F4:B}`
- [ ]  b) `{Global: (X and A and B), MAIN: X, F1:W, F3: A, F4:B}`
- [ ]  c) `{MAIN: X, F1:W, F3:A, F4:B}`
- [ ]  d) `{Global: (X and A), F1:W, F4:B}`
- [ ]  e) Can’t tell by looking at Fig 1




---
## Q23 (3 pts): Variable Descriptors need NOT stay around for the life of the variable if:
- [ ]  a) The variable storage binding is stack-dynamic
- [ ]  b) The variable descriptor is used during compile time
- [ ]  c) None of the variable descriptor’s attributes are dynamic
- [ ]  d) The variable is stored on the Heap




---
## Q24 (3 pts): Many languages set the lower bound for an array range to 1 (one) because:

- [ ]  a) Most languages use row-major data storage for arrays
- [ ]  b) It is more readable and writable for users
- [ ]  c) No language can use a negative number as an index value
- [ ]  d) It makes indexing more efficient




---
## Q25 (3 pts): References, unlike Pointers, will:
- [ ]  a) Never be used with anonymous variables on the heap
- [ ]  b) Never need to be dereferenced by the programmer
- [ ]  c) Often allow their memory cell’s values to be manipulated by the programmer
- [ ]  d) Actually reference other things




---
## Q26 (3 pts): A Multiple Selection statement:
- [ ]  a) Will always enforce mutual exclusion
- [ ]  b) Cannot use compound statements
- [ ]  c) Can be written to enforce mutual exclusion
- [ ]  d) ALL of these



---

## Q27 (3 pts): Our pseudo-code language we developed at the start of the semester has the MOVE operation (+0). Given the limited number of statements our design allowed (only 20), what unimplemented operation did we also use it for?
- [ ]  a) Jump
- [ ]  b) Increment
- [ ]  c) Invert
- [ ]  d) Assignment



---
## Q28 (3 pts): Early programming languages often only implemented Static variable storage binding, which:
- [ ]  a) Limited the number of characters a variable name could have
- [ ]  b) Did not allow for recursion
- [ ]  c) Made things run less efficiently
- [ ]  d) All of the others




------

## Q29-33: Given the following Extended BNF, determine whether the strings are valid or invalid “LINE”.

### Extended BNF Rules:
- **`<run>`** → `*` (zero or more)
- **`+`** → `one or more`
- **`<squeeze>`** → `{010}+` | `{101}*`
- **`<LINE>`** → `<squeeze> <run> <squeeze>`
Given the following Extended BNF , which strings are a valid or invalid “LINE”?
* `*` is zero or more
* `+` is one or more 

`<run>` → {0|1}
`<squeeze>` → {010}+ | {101}*
`<LINE>` → `<squeeze>` `<run>` `<squeeze>`
- (NOTE: This is the LINE to check)

### Strings to Check:
**Q29 (2 pts):**
`1011010`
- [ ]  Valid
- [ ]  Invalid


**Q30 (2 pts):**
`1010100101`
- [ ]  Valid
- [ ]  Invalid


**Q31 (2 pts):**
`01001010`
- [ ]  Valid
- [ ]  Invalid


**Q32 (2 pts):**
`1101`
- [ ]  Valid
- [ ]  Invalid


**Q33 (2 pts):**
`0`
- [ ]  Valid
- [ ]  Invalid




---
## Q34 (3 pts): Ambiguous Grammar and Parse Trees
A **rightmost**, **leftmost**, or neither right nor leftmost approach can be used in the derivation of a sentence in an ambiguous grammar.
**Question:** If each approach is used on the same one sentence of such a language, how many possible different parse trees could be involved?
- [ ]  a) 1
- [ ]  b) 2
- [ ]  c) 3
- [ ]  d) More than 3 are possible




---

## Q35 (3 pts): The Usefulness of a Language Recognizer
**Question:** What is the primary purpose of a language recognizer?
- [ ]  a) To generate useful syntactically correct code for a given language (like a button to be pushed)
- [ ]  b) To determine if a statement is syntactically correct for a given language
- [ ]  c) Provide a set of rules for syntactically correct statements to help users understand the language
- [ ]  d) None of the others




---
## Q36 (3 pts): The Scope and Lifetime of a Variable
**Question:** What determines the scope and lifetime of a variable?
- [ ]  a) If a Global STATIC variable, will be from the start of execution to the end of execution of the program
- [ ]  b) If a STACK-DYNAMIC variable, will be from the function invocation to the end of the function
- [ ]  c) Both answer a) and b)
- [ ]  d) Neither answer a) nor b)




---
## Q37 (3 pts): Are you glad the semester is over?
- [ ]  a) Yes




---