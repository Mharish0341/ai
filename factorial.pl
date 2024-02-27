 Base case: Factorial of 0 is 1
factorial(0, 1).

% Recursive case: Factorial of N is N multiplied by the factorial of N-1
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, SubResult),
    Result is N * SubResult.

% Base case: Fibonacci of 0 is 0, Fibonacci of 1 is 1
fibonacci(0, 0).
fibonacci(1, 1).

% Recursive case: Fibonacci of N is the sum of Fibonacci of N-1 and N-2
fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, Fib1),
    fibonacci(N2, Fib2),
    Result is Fib1 + Fib2.