%a
access(X, Y):-weapon_access(X, Y), key_access(X), crime_access(X).

%b
weapon_access(X, patties):-whereabouts(X, thursday, havener); whereabouts(X, 
      wednesday, library).
weapon_access(X, toiletseat):-whereabouts(X, wednesday, csbuilding); whereabouts(X, 
      thursday, csbuilding).

%c
key_access(X):-whereabouts(X, monday, library); whereabouts(X, tuesday, havener).
key_access(wallen).

%d
crime_access(X):-whereabouts(X, thursday, csbuilding); whereabouts(X, friday, 
      csbuilding).

%e
whereabouts(gosnell, monday, library). 
whereabouts(gosnell, tuesday, library). 
whereabouts(gosnell, wednesday, havener). 
whereabouts(gosnell, thursday, library). 
whereabouts(gosnell, friday, csbuilding).

whereabouts(cen, monday, havener).
whereabouts(cen, tuesday, havener).
whereabouts(cen, wednesday, havener). 
whereabouts(cen, thursday, library).
whereabouts(cen, friday, csbuilding).

whereabouts(markowsky, monday, csbuilding).
whereabouts(markowsky, tuesday, havener).
whereabouts(markowsky, wednesday, csbuilding).
whereabouts(markowsky, thursday, csbuilding).
whereabouts(markowsky, friday, csbuilding). 

whereabouts(wallen, monday, csbuilding). 
whereabouts(wallen, tuesday, havener). 
whereabouts(wallen, wednesday, havener).
whereabouts(wallen, thursday, library).
whereabouts(wallen, friday, csbuilding).

whereabouts(madria, monday, csbuilding).
whereabouts(madria, tuesday, csbuilding).
whereabouts(madria, wednesday, library).
whereabouts(madria, thursday, csbuilding).
whereabouts(madria, friday, csbuilding). 

whereabouts(zhu, monday, csbuilding).
whereabouts(zhu, tuesday, havener).
whereabouts(zhu, wednesday, havener).
whereabouts(zhu, thursday, library).
whereabouts(zhu, friday, library).

whereabouts(price, monday, library).
whereabouts(price, tuesday, library).
whereabouts(price, wednesday, library).
whereabouts(price, thursday, havener).
whereabouts(price, friday, csbuilding).

whereabouts(banarjee, monday, csbuilding).
whereabouts(banarjee, tuesday, library).
whereabouts(banarjee, wednesday, library).
whereabouts(banarjee, thursday, library).
whereabouts(banarjee, friday, csbuilding).

%f
victim(leopold).
motive(X, jealous):-jealous(X, leopold); jealous(leopold, X).
motive(X, insane):-insane(X).
motive(X, poor):-poor(X).

%g
insane(madria).
insane(banerjee).

%h
poor(wallen).
poor(price).
poor(gosnell).
poor(banarjee).

%i
jealous(X, Y):-involved_with(X, Z), involved_with(Y, Z).

%j
involved_with(X, Y):-involved(X, Y); involved(Y, X).

%k
involved(leopold, price).
involved(price, cen).
involved(leopold, gosnell).
involved(gosnell, zhu).
involved(zhu, markowsky).
involved(markowsky, banerjee).
involved(madria, banerjee).
involved(madria, cen).

%l
murderer(X, Y, Z):-motive(X, Z), access(X, Y).