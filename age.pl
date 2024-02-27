% Define the DOB of individuals
dob(john, date(1990, 5, 15)).
dob(mary, date(1985, 8, 25)).
dob(peter, date(1978, 12, 10)).
dob(jane, date(1995, 3, 7)).
dob(alice, date(2000, 10, 20)).

% Calculate age based on DOB
age(Person, Age) :-
    dob(Person, date(Year, Month, Day)),
    get_date(Year, Month, Day, DOB),
    get_date(Y, M, D, now),
    Age is Y - Year - (M < Month; (M == Month, D < Day)).

get_date(Year, Month, Day, date(Year, Month, Day)).

% Find individuals older than a certain age
older_than(Age, Person) :-
    age(Person, AgePerson),
    AgePerson > Age.

% Determine the youngest person in the database
youngest(Person) :-
    dob(Person, DOB),
    \+ (dob(_, OtherDOB), OtherDOB @> DOB).

% Check if one person is older than another
:- discontiguous older_than/2.
older_than(Person1, Person2) :-
    age(Person1, Age1),
    age(Person2, Age2),
    Age1 > Age2.