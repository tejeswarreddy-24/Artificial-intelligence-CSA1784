female(indu). %clauses
female(lie).

male(ramu).
male(varun).

parent(lie,ramu).
parent(indu,varun).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(Y).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parents(Z,X),parent(Z,Y),male(X),X\==Y.
