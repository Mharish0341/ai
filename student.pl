 Define facts about students, teachers, subjects, and codes
student(john, 101).
student(mary, 102).
student(peter, 103).

teacher(mr_smith, math).
teacher(mrs_jones, science).
teacher(mr_doe, history).

subject(math, algebra).
subject(science, biology).
subject(history, world_war_II).

% Generate "fill in the blank" questions
generate_question(Question) :-
    random_student(Student),
    format(atom(Question), 'What is the code of ~w?', [Student]).

generate_question(Question) :-
    random_teacher(Teacher),
    format(atom(Question), 'Who teaches ~w?', [Teacher]).

generate_question(Question) :-
    random_subject(Subject),
    format(atom(Question), 'What is the topic of ~w?', [Subject]).

generate_question(Question) :-
    random_code(Code),
    format(atom(Question), 'Which subject has the code ~w?', [Code]).

% Randomly select a student
random_student(Student) :-
    findall(S, student(S, _), Students),
    random_member(Student, Students).

% Randomly select a teacher
random_teacher(Teacher) :-
    findall(T, teacher(T, _), Teachers),
    random_member(Teacher, Teachers).

% Randomly select a subject
random_subject(Subject) :-
    findall(Sub, subject(Sub, _), Subjects),
    random_member(Subject, Subjects).

% Randomly select a code
random_code(Code) :-
    findall(C, student(_, C), Codes),
    random_member(Code, Codes).