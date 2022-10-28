male('Hasib').
male('Rakib').
male('Sohel').
male('Rashid').
male('Nahin').
female('Rebeka').
female('Sabiha').
parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').
parent('Hasib','Nahin').
parent('Hasib','Sabiha').

brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
uncle(X,Z):-brother(X,Y),parent(Y,Z).
auntie(X,Z):-sister(X,Y),parent(Y,Z).

findBr :- write('Name: '), read(P), write('Brother: '),
brother(Br, P), write(Br), tab(5), fail.
findBr.
findSr :- write('Name: '), read(P), write('Sister: '),
sister(Sr, P), write(Sr), tab(5), fail.
findSr.
findUn :- write('Name: '), read(P), write('Uncle: '),
uncle(Un, P), write(Un), tab(5), fail.
findUn.
findAu :- write('Name: '), read(P), write('Aunt: '),
auntie(Au, P), write(Au), tab(5), fail.
findAu.






