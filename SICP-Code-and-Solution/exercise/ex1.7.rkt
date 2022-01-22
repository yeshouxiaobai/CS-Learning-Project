#lang racket
(define (sqrt-iter guess x)
  (if (good-enough? guess (improve guess x) x)
      (improve guess x)
      (sqrt-iter (improve guess x) x)))

(define (improve guess x)
  {average guess (/ x guess)})

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? old-guess new-guess x)
      (< (/ (abs (- old-guess new-guess))
            old-guess)
          0.00001))

(define (abs x)
  (cond ((< x 0) (- x))
        ((> x 0) x)
        ((= x 0) 0)))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(sqrt 0.000000000000000000009)
(sqrt 900000000000000000000000000000000000000000000000000000000000000000000000000000000000)
