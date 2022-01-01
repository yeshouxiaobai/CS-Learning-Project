#lang racket
(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

;(define (abs x)
;  (cond ((< x 0) (- x))
;        (else x )))

;(define (abs x)
;  (if (< x 0)
;      (- x)
;      x))

(define (x-in-5-10 x)
  (and (> x 5) (< x 10)))

(x-in-5-10 6)

(define (>= x y)
  (or (> x y) (= x y)))

(>= 20 20)

;(define (>= x y)
;  (not (< x y)))

(define (p) (p))
(define (test x)
  (cond ((> x 0) x)
        (else (p))))
(test 1)
