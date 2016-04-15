data count;
   input x;
   if missing(x) then MissCounter + 1;
datalines;
2
.
7
.
;
