(format t "TEST")

(setq A `((1 2)  3 ( 2 3 (1 9))))
(setq B `(1 2 3 4 5))
(setq C `((1 2) ((3)) 4 (5)))
(setq D `(1 2 (6 3) 4 5))

(defun doubleodd (lst)
  (mapcar (lambda (x)
            (if (oddp x)
                (* x 2)
                x))
          lst))

(write-line (doubleodd B))
(write-line "Hello World")