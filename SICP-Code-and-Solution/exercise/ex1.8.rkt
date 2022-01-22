#lang racket
(define (curt-iter guess x)
  (if (good-enough? guess (improve guess x) x)
      (improve guess x)
      (curt-iter (improve guess x) x)))

(define (improve guess x)
  (/ (+ (/ x (square guess))
      (* 2 guess))
  3))

(define (square x) (* x x))

(define (good-enough? old-guess new-guess x)
      (< (/ (abs (- old-guess new-guess))
            old-guess)
          0.00001))

(define (abs x)
  (cond ((< x 0) (- x))
        ((> x 0) x)
        ((= x 0) 0)))

(define (curt x)
  (curt-iter 1.0 x))

(curt 0.000000000000000000009)
(curt 900000000000000000000000000000000000000000000000000000000000000000000000000000000000)
