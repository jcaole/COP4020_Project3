(DEFUN demo()
	(setq fp (open "theString.txt" :direction :input))
	(setq l (read fp "done"))
	(princ "processing ")
	(princ l)
	(fsa l)
)

(DEFUN fsa(l)
	(cond 
		((null l) "illegal")
		(t(state0 l))
	)
)

(DEFUN state0(l)
	(cond 
		((null l) "illegal character in state 0")
		((equal 'x (car l)) (state0(cdr l)))
		((equal 'y (car l)) (state1(cdr l)))
		(t "illegal character in state 0")
	)
)

(DEFUN state1(l)
	(cond 
		((null l) "legal")
		((equal 'x (car l)) (state2(cdr l)))
		(t "illegal character in state 1")
	)
)

(DEFUN state2(l)
	(cond 
		((null l) "illegal character in state 2")
		((equal 'x (car l)) (state2(cdr l)))
		((equal 'y (car l)) (state3(cdr l)))
		(t "illegal character in state 2")
	)
)

(DEFUN state3(l)
	(cond 
		((null l) "legal")
		((equal 'x (car l)) (state3(cdr l)))
		((equal 'z (car l)) (state4(cdr l)))
		(t "illegal character in state 3")
	)
)

(DEFUN state4(l)
	(cond 
		((null l) "illegal character in state 4")
		((equal 'x (car l)) (state4(cdr l)))
		((equal 'a (car l)) (state1(cdr l)))
		(t "illegal character in state 4")
	)
)