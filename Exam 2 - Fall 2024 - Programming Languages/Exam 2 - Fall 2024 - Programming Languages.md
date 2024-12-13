# CSC 461 Exam II - Fall 2024
**Instructions:**  
Record your answers using the QUIZ FOR Exam 2.

---
### Q1 (4 pts)
The Pointer type is designed to be used for two distinct purposes. One is to access anonymous variables. The other is to ___
- [ ]  a. Make code more readable.
- [ ]  b. Make code more reliable.
- [ ]  c. Allow Pass-by-reference. ===
- [x] d. Provide a form of indirect addressing. ✅ 2024-11-27
---
### Q2 (4 pts)
User-defined data types are helpful as they:
- [ ]  a. Always use the type name to do type checking.
- [x] b. Allow the compiler to help type-check new data types not in the language. ✅ 2024-11-27
- [ ]  c. Force the user to always use meaningful type names.
- [ ]  d. All of the others.
---
### Q3 (4 pts)
Variable Descriptors need NOT stay around for the life of the variable if:
- [x] a. The variable storage binding is stack-dynamic. ✅ 2024-11-27
- [ ]  b. The variable descriptor is used during compile time.
- [ ]  c. None of the variable descriptor’s attributes are dynamic.
- [ ]  d. The variable is stored on the Heap.
---
### Q4 (4 pts)
Strings in the language C are stored as an array of characters (often called a C-string). A library of manipulation functions is provided to allow the strings to be copied or appended, making them fairly user-friendly. However, there are issues with this approach because:
- [ ]  a. The language cannot be embodied by the user because it adds too much complexity.
- [x] b. Safety issues may occur if the language does not do range checking of array indexes. ✅ 2024-11-27
- [ ]  c. It is too much of a burden to make users include the library.
- [ ] d. None of the others.
---
### Q5 (4 pts)
An enumeration type is one in which all of the possible values, which are named constants, are provided, or enumerated, in the definition. If the enumeration type variable can be coerced into an integer, then:
- [x] a. It could be seen as weakening the Typing system. ✅ 2024-11-27
- [ ]  b. Using enumeration types are not useful.
- [ ]  c. It cannot be used in integer operations.
- [ ]  d. All of these.
---
### Q6 (4 pts)
Many languages set the lower bound for an array range to 0 (zero) because:
- [ ]  a. Most languages use row-major data storage for arrays.
- [ ]  b. It is more readable and writable for users.
- [ ]  c. No language can use a negative number as an index value.
- [x] d. It makes indexing more efficient. ✅ 2024-11-27
---
### Q7 (4 pts)
The type of array whose memory allocation is managed by the system in terms of allocation and deallocation, but size may be set by the programmer code during execution is a:
- [ ]  a. Static Array.
- [ ]  b. Fixed-Stack Dynamic Array.
- [ ]  c. Stack Dynamic Array. ===
- [x] d. Heap Dynamic Array. ✅ 2024-11-27
- [ ]  e. Fixed-Heap Dynamic Array.
---
### Q8 (4 pts)
For more complex structures such as arrays and structs, type compatibility rules are not as easy as for scalar types. Instead of coercion, another definition is used that does not require coercion. What is the name we give to this?
- [x] a. Equivalence. ✅ 2024-11-27
- [ ]  b. Short Circuit.
- [ ]  c. Matching.
- [ ]  d. Deep Pairing.
---
### Q9 (4 pts)
Unions are a form of Record type where you can have different variations of the fields for the same record type:
- [ ]  a. Unions help make languages more strongly typed.
- [x] b. Variables of the same Union type will have the same size memory storage. ✅ 2024-11-27
- [ ]  c. Union variables can only be bound to static memory storage.
- [ ]  d. Union types are not found in modern languages.
---
### Q10 (4 pts)
Pointers, unlike References, will:
- [ ]  a. Be used with anonymous variables on the heap. ===
- [ ]  b. Never need to be dereferenced by the programmer.
- [x] c. Often allow their memory cell’s values to be manipulated by the programmer. ✅ 2024-11-27
- [ ]  d. Actually reference other things.
---
### Q11 (4 pts)
When it comes to Flow-of-Control statements in a language, it is widely agreed that they can be limited to three types: Sequence, Selection, and Iteration. However, having a large number of variations available in a language:
- [x] a. May hurt Readability. ✅ 2024-11-27
- [ ]  b. May help with Readability.
- [ ]  c. Allows programs to solve more problems.
- [ ]  d. Makes executable code of user programs bigger.
---
### Q12 (4 pts)
The if-then-else statement is not required, as using separate if-then statements can achieve the same outcome. Most languages implement the if-then-else statement because:
- [ ]  a. It can make the code more readable.
- [ ]  b. It enforces mutual exclusion.
- [ ]  c. It can help with reliability.
- [x] d. ALL of the others. ✅ 2024-11-27
---
### Q13 (4 pts)
Nested if-then-else statements can result in:
- [x] a. A dangling else ambiguity issue. ✅ 2024-11-27
- [ ]  b. Easier scoping rules.
- [ ]  c. A stronger typed language.
- [ ]  d. No need for compound statements.
---
### Q14 (4 pts)
A Multiple Selection statement can:
- [ ]  a. Help with readability.
- [ ]  b. Help with writability.
- [ ]  c. Be written to enforce mutual exclusion.
- [x] d. ALL of these. ✅ 2024-11-27
---
### Q15 (4 pts)
The difference between a Fixed loop and a Counting loop is that:
- [ ]  a. A Fixed loop cannot be used to implement the logic of a counting loop.
- [ ]  b. A Counting loop guarantees it will not go into an infinite loop.
- [x] c. A Fixed loop guarantees it will not go into an infinite loop. ✅ 2024-11-27
- [ ]  d. A Fixed loop cannot use a variable for the upper bound.
---
### Q16 (4 pts)
It has been proven that the GOTO statement is not required and can be dangerous:
- [ ]  a. That is why imperative languages now do not implement the GOTO statement.
- [ ]  b. Only experienced programmers should use them frequently in their code.
- [ ]  c. They are also less writable and therefore never used.
- [x] d. They are still implemented in most imperative languages because there are special cases where they can make the logic more readable or efficient. ✅ 2024-11-27
---
### Q17 (4 pts)
Short-Circuiting logic can never be used with the logical operator(s):
- [ ]  a. and.
- [ ]  b. or.
- [x] c. xor. ✅ 2024-11-27
- [ ]  d. Can be used with all of these 3. ===
---
### Q18 (4 pts)
Type Casting and Type Coercion are both examples of converting one type to another:
- [x] a. TRUE. ✅ 2024-11-27
- [ ]  b. FALSE.
---
### Q19 (4 pts)
Which of these is considered a possible arithmetic expression error:
- [ ]  a. Overflow.
- [ ]  b. Underflow.
- [ ]  c. Division by Zero.
- [x] d. All of these. ✅ 2024-11-27
---
### Q20 (4 pts)
Not including a Boolean type but instead representing a Boolean as an integer can weaken the Typing system of a language:
- [x] a. TRUE. ✅ 2024-11-27
- [ ]  b. FALSE.
---
### Q21 (4 pts)
The assignment statement may be of mixed-mode, where the LHS is NOT the same as the RHS. To handle this, many languages will use coercion on the RHS. In that case, they usually limit the type of coercion to _________ to help with reliability:
- [ ]  a. A Narrowing form.
- [x] b. A Widening form. ✅ 2024-11-27
- [ ]  c. None of the others.
---
### Q22 (4 pts)
Functional side effects cannot occur when:
- [ ]  a. No parameters are passed.
- [ ]  b. If only 1 parameter is passed.
- [ ]  c. There are no logical errors in the function (it works correctly).
- [x] d. Only constants are involved. ✅ 2024-11-27
---
### Q23 (4 pts)
A language is considered Strongly Typed if:
- [ ]  a. Real numbers are not allowed.
- [x] b. Type errors are always detected. ✅ 2024-11-27
- [ ]  c. All types are set at compile time.
- [ ]  d. All typing errors can be detected at compile time.
---
### Q24 (4 pts)
If the programmer wants to use an array to hold a look-up table to be used for the whole program, they should choose what type of storage binding?
- [ ]  a. A fixed stack-dynamic Array.
- [x] b. A static Array. ✅ 2024-11-27
- [ ]  c. Explicit heap-dynamic Array.
- [ ]  d. Static scoping.
---
### Q25 (4 pts)
Type Casting is used to:
- [ ]  a. Coerce a variable type to a different type.
- [x] b. Convert a variable type to another type. ✅ 2024-11-27
- [ ]  c. Allow the system to automatically apply a rule to make types compatible.
- [ ]  d. Set the type of a variable from that point until cast into another type in a later statement. ===
---