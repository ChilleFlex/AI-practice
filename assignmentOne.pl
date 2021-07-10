parent('siddique','masum').
parent('siddique','laila').
parent('masum','raiyan').
parent('raiyan','rafsan').
parent('raiyan','ebon').
parent('raiyan','raisa').
parent('rafsan','shihab').

male('siddique'). male('masum'). male('raiyan'). male('rafsan').
male('ebon'). male('shihab'). female('laila'). female('raisa').

brother(X,Y):- parent(Z,X), parent(Z,Y), not(X=Y), male(X).
%We assume X is brother of Y


printbrother :- write('Person: '), read(BR),
	  write('Brother: '), brother(B, BR),
	  write(B), tab(5), fail.
printbrother.

sister(X,Y):- parent(Z,X), parent(Z,Y), not(X=Y), female(X).
%We assume X is sister of Y

printsister :- write('Person: '), read(SS),
	  write('Sister: '), sister(S, SS),
	  write(S), tab(5), fail.
printsister.

uncle(X,Y):- parent(Z,Y), brother(X,Z), male(X).
%We assume X is uncle, Y is nephew/niece

printuncle :- write('Person: '), read(UNC),
	  write('Uncle: '), uncle(UN, UNC),
	  write(UN), tab(5), fail.
printuncle.

aunt(X,Y):- parent(Z,Y), sister(X,Z), female(X).
%We assume X is aunt, Y is nephew/niece

printaunt:- write('Person: '), read(AUN),
	  write('Aunt: '), aunt(AU, AUN),
	  write(AU), tab(5), fail.
printaunt.
