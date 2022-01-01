#lang racket
(define (max-of-3 x y z)
  (max-of-2 x
            (max-of-2 y z)))

;(define (max-of-2 x y)
;  (cond ((> x y) x)
;        (else y)))

(define (max-of-2 x y)
  (if (> x y) x y))
