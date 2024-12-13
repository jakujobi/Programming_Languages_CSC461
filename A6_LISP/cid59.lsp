; Lisp Functions **2024**
(print "************************")
(print " John Akujobi  ")
(print "************************")

; DO NOT  use higher level list funtions !!
; DO NOT use helper funtions (1 funtion solutions)
; 
;
; TEST CASE LISTS 
(setq A `((1 2)  3 ( 2 3 (1 9))))
(setq B `(1 2 3 4 5))
(setq C `((1 2) ((3)) 4 (5)))
(setq D `(1 2 (6 3) 4 5))
(setq Empl '( (10 Mary Smith 36 12) (5 Bob Olsen 33 12) (130 Lace Smith 44 16)))
;******************


;;!=========================================================================================================================================================
;;****** lookupempl ***************
;;!=========================================================================================================================================================
;********************************
;****** lookupempl ***************
; returns values related to the Key value of an
; employee tuple defined as  (KEY# Fname Lname Age Dept#)
; Example: employe tuple -->    (10 Mary Smith 36 12)
; A databasee list called Empl will contanin several Employees
; the funtion lookupEmpl will use the Key to return the Emply record list
; of the employee.  
; If no employee match return 'NOT FOUND.
; Example:  (lookupempl Empl 10) --> (10 Mary Smith 36 12)
;********************************

(defun lookupEmpl (empl-list key)
  "Look up an employee record by KEY in EMPL-LIST using basic recursion."
    (cond
        ;; If empl-list is empty, return 'NOT-FOUND
        ((null empl-list)
            'NOT-FOUND
        )

        ;; Compare the car of the first record to KEY
        (
            (eq
                (car (car empl-list))
                key
            )
            (car empl-list)
        )

        ;; Otherwise, recurse down the list
        (t
            (lookupEmpl (cdr empl-list) key
            )
        )
    )
)
(print (lookupEmpl Empl 10))






;;!=========================================================================================================================================================
;;****** Doubleodd ***************
;;!=========================================================================================================================================================
;****** Doubleodd ***************
; Doubleodd: return a list where all the odd numbers have been doubled.
; Example: (doubleodd B) --> (2 2 6 4 10)
; Assume single level list
;********************************

(defun doubleOdd (lst)
    "Return a single-level list where all odd integers in LST are doubled."
    (cond
        ;; Base case: empty list
        ((null lst) nil)

        ;; If the first element is an odd integer, double it
        (
            (and
                (numberp (car lst))
                (= 
                    (rem (car lst) 2) 1
                )
            )
            (cons
                (* 2 (car lst))
                (doubleOdd (cdr lst))
            )
        )

        ;; Otherwise keep the element as is
        (t
            (cons
                (car lst)
                (doubleOdd (cdr lst))
            )
        )
    )
)
(print (doubleOdd B))






;;!==========================================================================================================================================================
;;****** addAll ***************
;;!==========================================================================================================================================================
;****** addAll ******************
; addall: returns the sum of nested list of positive integers
; Example: (addAll C) --> 15
; Return 0 if the list is empty
; Assume that it may be a nested level list
;********************************

(defun addAll (lst)
  "Sum all positive integers in a nested list LST."
    (cond
        ;; Base case: empty list
        ((null lst) 0)

        ;; If the car is itself a nested list, recurse inside it and add to the rest
        (
            (listp (car lst))
            (+ 
                (addAll (car lst))
                (addAll (cdr lst))
            )
        )

        ;; If the car is an atom, check if it's a positive integer
        (
            (and (numberp (car lst))
                (> (car lst) 0)
            )
            (+
                (car lst) (addAll (cdr lst))
            )
        )

        ;; Otherwise, skip it and move on
        (t
            (addAll (cdr lst))
        )
    )
)
(print (addAll C))




;;!==========================================================================================================================================================
;;****** large_atom ***************
;;!==========================================================================================================================================================
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

(defun large_atom (L)
    "Return the largest positive integer in the nested list L using a recursive approach."
    (cond
        ;; Base case: if the list is empty, return 0
        ((null L)
        0)

        ;; If the car of the list is itself a list, recursively call large_atom on that list
        ((listp (car L))
            (let ((submax (large_atom (car L)))          ; largest in the sublist
                    (restmax (large_atom (cdr L)))
                )        ; largest in the rest
                (cond 
                    ((> submax restmax) submax)
                    (t restmax)
                )
            )
        )

        ;; If the car of the list is an atom and it's a positive integer:
        (
            (and
                (numberp (car L))
                (> (car L) 0)
            )
            (let 
                (
                    (restmax
                        (large_atom (cdr L))
                    )
                )        ; largest in the rest of the list
                (if (> (car L) restmax)
                    (car L)
                    restmax
                )
            )
        )

        ;; Otherwise, skip the car and move on
        (t
            (large_atom (cdr L))
        )
    )
)
(print (large_atom D))