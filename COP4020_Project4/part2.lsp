(DEFUN demo()
	(setq fp (open "theString.txt" :direction :input))
	(setq list (read fp "done"))
	(princ "processing ")
	(princ list)
	(fsa list)
)

(DEFUN fsa(list)
	(cond 
		((null list) "illegal")
		(t(state0 list))
	)
)

(DEFUN state0(list)
	(cond 
		((null list) "illegal -- error caught in state 0 -- null")
		((equal 'x (car list)) (state0(cdr list)))
		((equal 'y (car list)) (state1(cdr list)))
	)
)

(DEFUN state1(list)
	(cond 
		((null list) "legal")
		((equal 'x (car list)) (state2(cdr list)))
	)
)

(DEFUN state2(list)
	(cond 
		((null list) "illegal -- error caught in state 2 -- null")
		((equal 'x (car list)) (state2(cdr list)))
		((equal 'y (car list)) (state3(cdr list)))
	)
)

(DEFUN state3(list)
	(cond 
		((null list) "legal")
		((equal 'x (car list)) (state3(cdr list)))
		((equal 'z (car list)) (state4(cdr list)))
	)
)

(DEFUN state4(list)
	(cond 
		((null list) "illegal -- error caught in state 4 -- null")
		((equal 'x (car list)) (state4(cdr list)))
		((equal 'a (car list)) (state1(cdr list)))
	)
)

