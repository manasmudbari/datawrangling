data four_dates;
   	input 	@1  Subject   $3.
         	@5 DOB       mmddyy10.
         	@16 VisitDate mmddyy8.
         	@26 TwoDigit  mmddyy8.
         	@34 LastDate  date9.;
	format 	DOB VisitDate date9.
       		TwoDigit LastDate mmddyy10.;
datalines;
001 10/21/1950 05122003 08/10/65 23Dec2005
002 01/01/1960 11122005 09/13/02 02Jan1960
;

run;

proc print;
