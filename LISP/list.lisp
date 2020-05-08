(defvar a )
(defvar n)
(print "Enter list")

(setq a (read-from-string (concatenate 'string "(" (read-line) ")")))


(print a)

(print "Enter the index in list")

(setq n (read))
(print "The element is - ")
(print (nth n  a))

