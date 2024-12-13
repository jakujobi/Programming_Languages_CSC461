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



;==========================================================================================================================================================`
;******  Divider Line ***************
;==========================================================================================================================================================
; This prints a line of = signs  and 2 empty lines after to separate the output and it is used to separate the output of different functions
; it does so by rpeating the = sign 40 times
;********************************
(defun divider ()
  (print (make-string 40 :initial-element #\=))
  (print "")
  (print "")
  )

(divider)


;==========================================================================================================================================================
;******  title lines ***************
;==========================================================================================================================================================
; This prints the name of the function being run in the middle of a line of = signs at bothe sides
; it does so by rpeating the = sign 40 times and then adding the name of the function in the middle
;********************************
(defun title (name)
  (print (concatenate 'string (make-string 20 :initial-element #\=) " " name " " (make-string 20 :initial-element #\=)))
  (print "")
  )


;==========================================================================================================================================================
;****** lookupempl ***************
;==========================================================================================================================================================

(title "lookupempl")

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

(defun lookupempl (empl-list key)
  (cond
    ((null empl-list)
     'NOT-FOUND)
    ((eq (car (car empl-list)) key)
     (car empl-list))
    (t
     (lookupempl (cdr empl-list) key))))
; print empty new line
(print "")
(print (lookupempl Empl 10))



;*****************************************
; lookupEmpl1: 
;   - Recursively scans Empl list 
;   - Returns record if found, else 'NOT-FOUND.
;*****************************************

(defun lookupEmpl1 (empl-list key)
  "Look up an employee record by KEY in EMPL-LIST using basic recursion."
  (cond
    ;; If empl-list is empty, return 'NOT-FOUND
    ((null empl-list)
     'NOT-FOUND)

    ;; Compare the car of the first record to KEY
    ((eq (car (car empl-list)) key)
     (car empl-list))

    ;; Otherwise, recurse down the list
    (t
     (lookupEmpl1 (cdr empl-list) key))))

; print empty new line
(print "")
(print (lookupEmpl1 Empl 10))





;==========================================================================================================================================================
;****** Doubleodd ***************
;==========================================================================================================================================================

(title "Doubleodd")

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
(divider)





;==========================================================================================================================================================
;****** addAll ***************
;==========================================================================================================================================================

(title "addAll")

;****** addAll ******************
; addall: returns the sum of nested list of positive integers
; Example: (addAll C) --> 15
; Return 0 if the list is empty
; Assume that it may be a nested level list
;********************************


(defun addAll (lst)
  (cond
    ((null lst) 0)
    ((numberp lst) lst)
    (t
     (+ (addAll (car lst)) (addAll (cdr lst))))))

; print empty new line
(print "")
(print (addAll C))



;==========================================================================================================================================================
;****** large_atom ***************
;==========================================================================================================================================================

(title "large_atom")

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













