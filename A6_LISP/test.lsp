;; Provided test data
(defvar Empl '(
   (10 Mary Smith 36 12)
   (5  Bob Olsen 33 12)
   (130 Lace Smith 44 16)
))

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

;*****************************************
; lookupEmpl2:
;   - Uses assoc to find employee by key
;*****************************************

(defun lookupEmpl2 (empl-list key)
  "Look up an employee record by KEY in EMPL-LIST using assoc."
  (let ((result (assoc key empl-list)))
    (if result
        result
        'NOT-FOUND)))

;*****************************************
; lookupEmpl3:
;   - Uses find with key and appropriate keyword arguments
;*****************************************

(defun lookupEmpl3 (empl-list key)
  "Look up an employee record by KEY in EMPL-LIST using find."
  (find key empl-list :key #'car :test #'eq :if-not-found 'NOT-FOUND))

;; Testing each version:
(write-line (format nil "~a" (lookupEmpl1 Empl 10)))  ; Expected: (10 Mary Smith 36 12)
(write-line (format nil "~a" (lookupEmpl1 Empl 5)))   ; Expected: (5 Bob Olsen 33 12)
(write-line (format nil "~a" (lookupEmpl1 Empl 99)))  ; Expected: NOT-FOUND

(write-line (format nil "~a" (lookupEmpl2 Empl 10)))  ; Expected: (10 Mary Smith 36 12)
(write-line (format nil "~a" (lookupEmpl2 Empl 5)))   ; Expected: (5 Bob Olsen 33 12)
(write-line (format nil "~a" (lookupEmpl2 Empl 99)))  ; Expected: NOT-FOUND

(write-line (format nil "~a" (lookupEmpl3 Empl 10)))  ; Expected: (10 Mary Smith 36 12)
(write-line (format nil "~a" (lookupEmpl3 Empl 5)))   ; Expected: (5 Bob Olsen 33 12)
(write-line (format nil "~a" (lookupEmpl3 Empl 99)))  ; Expected: NOT-FOUND