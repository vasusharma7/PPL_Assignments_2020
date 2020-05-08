(defvar a)

(setq a (read))

(setq n 1)

;Using loop :

;(loop for x from 1 to a
; do (setq n (* n  x)))

; Using recursion : 

(defun fact(n)	
 (if (= n 0) ( return-from fact 1))
  ( return-from fact (* n (fact (- n 1) )))
 )

(format t "The factorial of ~d is ~d" a  (fact a ))
;(write  "The Factorial Of" ) ( write a )( write "is")( write  n )

