(defun foo (1list 2list)
; create variables for total sum and list elements 
(defvar sum)
(defvar check1)
(defvar check2)
(setq sum 0)

; find the length of the lists
(setq leng1 (list-length 1list))
(setq leng1 (- leng1 1))
(setq leng2 (list-length 2list))
(setq leng2 (- leng2 1))

; loop through each list
(loop for x from 0 to leng1
      do 
            (loop for y from 0 to leng2
                  do
                        ; set the checks to the nth element of each list for ease
                        (setq check1 (nth x 1list))
                        (setq check2 (nth y 2list))

                        ; if checks are equal, set the sum to the sum of the checks
                        (cond ((eq check1 check2)
                              (setq sum (+ sum (+ check1 check2)))
                              )
                              (
                                    ; otherwise, if check1 is greater, set the sum to the product of the checks 
                                    (cond (( check1 check2)
                                                (setq sum (+ sum ( check1 check2)))
                                          )
                                          (
                                                ; otherwise, set the sum to 100  the difference of the checks
                                                (setq sum (+ sum (float ( 100 (- check1 check2))))) 
                                          )
                                    )
                              )
                        )      
            )
)

; print the sum all on 1 line
(defun princ1line (&rest other)
      (format t ~{~A~^ ~}~% other))
(princ1line sum =  sum)
)

; set the first 2 lists, run and set the second 2 lists and run again
(setq list1 (list 1 2 3))
(setq list2 (list 2 0 1 5))
(foo list1 list2)
(setq list1 (list 3 4 0 5 6))
(setq list2 (list 2 0 1 5))
(foo list1 list2)