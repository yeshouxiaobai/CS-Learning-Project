#lang racket
(define size 2)

size

(* 5 size)

(define pi 3.14159)

(define radius 10)

(* pi (* radius radius))

(define circumference (* 2 pi radius))

circumference



(define (square x) (* x x))

(square 21)

(square (+ 2 5))

(square (square 3))

(define (sum-of-squares x y)
  (+ (square x) (square y)))

(sum-of-squares 3 4)