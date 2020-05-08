(defvar a)

(setq a (read))

(setq n 1)

(loop for x from 1 to a
 do (setq n (* n  x)))


(format t "The factorial of ~d is ~d" a n)

