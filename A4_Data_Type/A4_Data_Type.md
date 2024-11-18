# CSC 461 Programming Languages
**Fall 2024**  
**Instructor:** Dr. Stephen Krebsbach  
**Assignment #4** - **10 Points**  
**Due Date:** Monday, November 11th, 11:59 PM  

**Instructions:**  
Please complete and answer the following questions. Record your responses using the Online Quiz format. Each question is worth 1 point.

---
### Questions
1. A Primitive data type is defined as:
   - [x] a. Data type not being defined in terms of other types ✅ 2024-11-11
   - [ ] b. Those with highest precedence
   - [ ] c. Those that can hold primary numbers
   - [ ] d. A collection of secondary data types
A primitive data type is a basic data type built into a programming language that represents simple values. Here are the key characteristics and examples of primitive data types:
## Characteristics
- **Simplicity**: Primitive data types are the most basic form of data that cannot be broken down further.
- **Fixed size**: They typically have a fixed size in memory, which varies depending on the specific type and programming language.
- **Efficiency**: Operations on primitive types are usually very efficient, as they are directly supported by the hardware.
- **Immutability**: In most languages, primitive values are immutable, meaning their value cannot be changed once created.

## Common Primitive Data Types
1. **Integer types**: Used for whole numbers
    - Examples: byte, short, int, long
2. **Floating-point types**: Used for decimal numbers
    - Examples: float, double
3. **Boolean**: Represents true/false values
    - Usually stored as a single bit or byte
4. **Character**: Represents a single character
    - Often uses Unicode encoding
---
2. Boolean values could be represented as 0/1 and only use one bit but usually use a larger memory cell than 1 bit. Why?
   - [x] a. Most machines do not access a single bit of memory efficiently ✅ 2024-11-11
   - [ ] b. So they can compact bits together
   - [ ] c. It is more readable
   - [ ] d. True or false is better than 0 or 1

---
3. One of the most important design issues for Character strings is:
   - [x] a. Does it have a Dynamic or Static length ✅ 2024-11-11
   - [ ] b. What language is it in
   - [ ] c. Are white spaces used
   - [ ] d. If we use the word "string" or "str" to define it

4. Requiring that the range of an array subscript be checked to see if it is in bounds helps mainly with:
   - [x] a. Reliability ✅ 2024-11-11
   - [ ] b. Multi-dimensional arrays
   - [ ] c. Arrays of Boolean type
   - [ ] d. Writability

5. If the programmer wants to use an array to hold a look-up table to be used for the whole program, they should choose what type of storage binding?
   - [ ] a. A fixed stack-dynamic Array
   - [x] b. A static Array ✅ 2024-11-11
   - [ ] c. Explicit heap-dynamic Array
   - [ ] d. Static scoping

6. The Pointer type is designed to be used for two distinct purposes. One is to provide a form of indirect addressing. The other is to:
   - [x] a. Access anonymous variables. ✅ 2024-11-11
   - [ ] b. Make code more readable
   - [ ] c. Make code more reliable
   - [ ] d. Allow Pass-by-value

7. Anonymous variables can cause issues in a type checking system that uses:
   - [x] a. Name equivalence ✅ 2024-11-11
   - [ ] b. Real numbers
   - [ ] c. Static scoping
   - [ ] d. Stacks

8. Including Type Coercion may be seen as a detriment because it:
   - [x] a. can be seen as weakening a strongly typed language ✅ 2024-11-11
   - [ ] b. makes the user explicitly handle mixed-mode typing issues
   - [ ] c. complicates static scoping
   - [ ] d. hurts writability

9. A language is considered Strongly Typed if:
   - [ ] a. real numbers are not allowed
   - [x] b. type errors are always detected ✅ 2024-11-11
   - [ ] c. all types are set at compile time
   - [ ] d. all typing errors can be detected at compile time

1. A major difference between a Pointer type and Reference type is that:
   - [ ] a. Only Pointer types are used in Heap Management
   - [ ] b. Only Reference types are used in Heap Management
   - [x] c. Arithmetic can be done on Pointers ✅ 2024-11-11
   - [ ] d. They are the same thing, but languages just use different words for it
