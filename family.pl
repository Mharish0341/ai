% Define family relationships
father(john, lisa).
father(mike, emma).
father(tom, mary).

mother(mary, lisa).
mother(mary, mike).
mother(emma, olivia).

% Define sibling relationship
sibling(lisa, mike).

% Define parent relationship
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% Define grandparent relationship
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Define sibling relation
sister(X, Y) :- sibling(X, Y), female(X).

% Define gender
male(john).
male(mike).
male(tom).

female(lisa).
female(mary).
female(emma).
female(olivia).

% Query predicates
father_of_emma(X) :- father(X, emma).
sister_of_mike(X) :- sister(X, mike).
grandmother_of_olivia(X) :- grandparent(X, olivia).
john_grandfather_of_olivia :- grandparent(john, olivia).