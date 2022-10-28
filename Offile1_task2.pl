
parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').
parent('Hasib','Nahin').
parent('Hasib','Sabiha').
parent('Sajia','Sohel').
parent('Sohel','Arif').


grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
findGp:- write('Grandchildren: ') , read(Gc) , write('Grandparent: ') ,
 grandparent(Gp , Gc) , write(Gp) , tab(5) , fail.
findGp.
