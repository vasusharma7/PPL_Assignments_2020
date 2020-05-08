airport(torronto,50,60).
airport(madrid,75,45).
airport(malaga,50,30).
airport(london,75,80).
airport(paris,50,60).
airport(toulouse,40,30).
airport(valencia,40,20).
airport(barcelona,40,30).


flight(torronto,london,united,650,420).
flight(torronto,london,air_canada,500,360).
flight(torronto,madrid,air_canada,900,480).
flight(torronto,madrid,united,950,540).
flight(torronto,madrid,iberia,800,450).
flight(london,barcelona,iberia,220,240).
flight(barcelona,madrid,air_canada,100,60).
flight(barcelona,madrid,iberia,120,65).
flight(barcelona,valencia,iberia,110,75).
flight(madrid,valencia,iberia,40,50).
flight(madrid,malaga,iberia,50,30).
flight(malaga,valencia,iberia,80,120).
flight(paris,toulouse,united,40,30).

%correctly_gives Torronto to Valencia


query(A,B,D,E,A - B) :- flight(A,B,C,D,E).
query(A,B,D+R,E + T,A - Y) :- flight(A,Z,C,D,E), query(Z,B,R,T,Y).



%incorrect -> gives repeated routes also when querried for Valencia to Torronto


%checkFlight(A,B,C,D,E) :- flight(A,B,C,D,E) ->flight(A,B,C,D,E);flight(B,A,C,D,E).

%query(A,B,D,E,A - B) :- checkFlight(A,B,C,D,E);

%query(A,B,D+R,E + T,A - Y) :- checkFlight(A,Z,C,D,E), query(Z,B,R,T,Y).





airport(C,T,D) :- airport(C,T,D).

isFlight(A,B) :- flight(A,B,C,D,E) ; flight(B,A,C,D,E).

