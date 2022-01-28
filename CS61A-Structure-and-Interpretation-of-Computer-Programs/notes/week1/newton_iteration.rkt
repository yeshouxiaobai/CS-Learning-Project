#lang racket

(define (improve update good-enough guess)
  (if (good-enough guess (update guess))
      guess
      (improve update good-enough (update guess))))
  
(define (get-newton-update f df)
  (define (update x)
    (- x (/ (f x) (df x))))
  update)

(define (sqrt a)
  (define (f x) (- (* x x) a))
  (define (df x) (* x 2.0))
  (define (good_enough guess new-guess)
    (< (abs (/ (- guess new-guess)
               guess))
       1e-9))
  (define update (get-newton-update f df))
  (improve update good_enough 1.0))

(sqrt 0.0000000003)
(sqrt 1000000000000000000000000000000000000000000000)
