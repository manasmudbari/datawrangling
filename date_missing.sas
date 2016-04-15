data my_dates;
input mm dd yy;
datalines;
10 21 1950
01 15 05
03 .  2005
5 7 2000
;
run;

options yearcutoff=1920; /* years from 1920 to 2019 */

data mdy_example;
   set my_dates;
   if missing(dd) then Date = mdy(mm,15,yy);
   else Date = mdy(mm,dd,yy);
   format Date mmddyy10.;
run;

proc print data=mdy_example;
