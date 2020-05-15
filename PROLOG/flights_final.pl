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



%flight(london,torronto,united,650,420).
%flight(london,torronto,air_canada,500,360).
%flight(madrid,torronto,air_canada,900,480).
%flight(madrid,torronto,united,950,540).
%flight(madrid,torronto,iberia,800,450).
%flight(barcelona,london,iberia,220,240).
%flight(madrid,barcelona,air_canada,100,60).
%flight(madrid,barcelona,iberia,120,65).
%flight(valencia,barcelona,iberia,110,75).
%flight(valencia,madrid,iberia,40,50).
%flight(malaga,madrid,iberia,50,30).
%flight(valencia,malaga,iberia,80,120).
%flight(toulouse,paris,united,40,30).



query(A,B,D,E,A - B) :- flight(A,B,C,D,E).
query(A,B,D + R,E + T,A - Y) :- flight(A,Z,C,D,E), query(Z,B,R,T,Y).

find(A,B,C,D,E) :- query(A,B,C,D,E) ; query(B,A,C,D,E).


%query (b) -> must produce all the cities with the airport tax in dollars and the minimum security delay in minutes. 
airport(C,T,D) :- airport(C,T,D).

%query ->torronto to paris in 2 flights can be resolved using query(torronto,paris,A,B,C) .. ..

%query(a) -> Is there a flight from A to B ? 
isFlight(A,B) :- flight(A,B,C,D,E) ; flight(B,A,C,D,E).


%query -> cheap < 400 or with airline 'R' ? 
cheap(A,B,R) :- flight(A,B,C,D<400 ,E) ; flight(A,B,R,G,H).


%query (e) -> If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. 
checkExistence(A,B,C,D) :- flight(A,B,C,F,E)  -> flight(A,B,D,G,H) ; flight(B,A,C,F,E)  -> flight(B,A,D,G,H).



