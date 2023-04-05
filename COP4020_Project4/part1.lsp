(DEFUN demo ()
  (setq fp (open "theString.txt" :direction :input))
  (setq l (read fp "done"))
  (princ "processing ")
  (princ l)
  (fsa l))

(DEFUN fsa (l)
  (cond
    ((null l) "illegal")
    (t (stateZero l))))

;; state 0
(DEFUN stateZero (l)
  (cond
    ((null l) "illegal -- error caught in state 0 -- null")
    ((equal 'x (car l)) (stateZero (cdr l)))
    ((equal 'y (car l)) (stateOne (cdr l)))
    (t "illegal -- error caught in state 0 -- endpoint")))

;; state 1
(DEFUN stateOne (l)
  (cond
    ((null l) "legal")
    ((equal 'x (car l)) (stateTwo (cdr l)))
    (t "illegal -- error caught in state 1 -- endpoint")))

;; state 2
(DEFUN stateTwo (l)
  (cond
    ((null l) "illegal -- error caught in state 2 -- null")
    ((equal 'x (car l)) (stateTwo (cdr l)))
    ((equal 'y (car l)) (stateThree (cdr l)))
    (t "illegal -- error caught in state 2 -- endpoint")))

;; state 3
(DEFUN stateThree (l)
  (cond
    ((null l) "legal")
    ((equal 'x (car l)) (stateThree(cdr l)))
    ((equal 'z (car l)) (stateFour(cdr l)))
    (t "illegal -- error caught in state 3 -- endpoint")))

;; state 4
(DEFUN stateFour (l)
  (cond
    ((null l) "illegal -- error caught in state 4 -- null")
    ((equal 'x (car l)) (stateFour (cdr l)))
    ((equal 'a (car l)) (stateOne (cdr l)))
    (t "illegal -- error caught in state 4 -- endpoint")))