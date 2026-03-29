%fatos
mochila(verde).
mochila(azul).
mochila(vermelho).
mochila(amarelo).
mochila(branco).
nome(otavio).
nome(will).
nome(denis).
nome(joao).
nome(lenin).
mes(janeiro).
mes(agosto).
mes(dezembro).
mes(setembro).
mes(maio).
jogo(cacapalavras).
jogo(tresoumais).
jogo(forca).
jogo(logica).
jogo(cubovermelho).
materia(geografia).
materia(historia).
materia(matematica).
materia(portugues).
materia(biologia).
suco(limao).
suco(maracuja).
suco(morango).
suco(uva).
suco(laranja).

alldifferent([]).
alldifferent([H|T]) :-
    \+ member(H, T),
    alldifferent(T).

modelo([ %modelo define a estrutura, como os elementos se relacionam
    (M1,N1,MS1,J1,MA1,S1),
    (M2,N2,MS2,J2,MA2,S2),
    (M3,N3,MS3,J3,MA3,S3),
    (M4,N4,MS4,J4,MA4,S4),
    (M5,N5,MS5,J5,MA5,S5)
]) :-
    mochila(M1), mochila(M2), mochila(M3), mochila(M4), mochila(M5),
    nome(N1), nome(N2), nome(N3), nome(N4), nome(N5),
    mes(MS1), mes(MS2), mes(MS3), mes(MS4), mes(MS5),
    jogo(J1), jogo(J2), jogo(J3), jogo(J4), jogo(J5),
    materia(MA1), materia(MA2), materia(MA3), materia(MA4), materia(MA5),
    suco(S1), suco(S2), suco(S3), suco(S4), suco(S5),

    alldifferent([M1,M2,M3,M4,M5]),
    alldifferent([N1,N2,N3,N4,N5]),
    alldifferent([MS1,MS2,MS3,MS4,MS5]),
    alldifferent([J1,J2,J3,J4,J5]),
    alldifferent([MA1,MA2,MA3,MA4,MA5]),
    alldifferent([S1,S2,S3,S4,S5]),

    S3 = morango,
    S1 = limao,
    N5 = lenin.


%main
main :-
    modelo(L), 
    write(L),nl. %imprime o modelo
    %fail.
main.