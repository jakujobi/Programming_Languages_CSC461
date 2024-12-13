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



;==========================================================================================================================================================
;****** lookupempl ***************
;==========================================================================================================================================================
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








;==========================================================================================================================================================
;****** Doubleodd ***************
;==========================================================================================================================================================
;****** Doubleodd ***************
; Doubleodd: return a list where all the odd numbers have been doubled.
; Example: (doubleodd B) --> (2 2 6 4 10)
; Assume single level list
;********************************
(defun doubleodd (lst)
  (mapcar (lambda (x)
            (if (oddp x)
                (* x 2)
                x))
          lst))
; print empty new line
(print "")
(print (doubleodd B))





;==========================================================================================================================================================
;****** addAll ***************
;==========================================================================================================================================================
;****** addAll ******************
; addall: returns the sum of nested list of positive integers
; Example: (addAll C) --> 15
; Return 0 if the list is empty
; Assume that it may be a nested level list
;********************************






;==========================================================================================================================================================
;****** large_atom ***************
;==========================================================================================================================================================
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