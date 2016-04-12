Data HTWT;
Input 	GENDER $
		HEIGHT
		WEIGHT
		COLLEGE $;
DATALINES;
M 68.5 155 Sci
F 61.2 99 Bsns
F 63.0 115 Bsns
M 70.0 205 Sci
M 68.6 170 Arts
F 65.1 125 Bsns
M 72.4 220 Arts
M 69.5 188 Sci
;
RUN;

proc freq data=HTWT;
	TITLE "Frequency Table";
	Tables GENDER*COLLEGE;
Run;

proc GCHART data=HTWT;
	TITLE "Bar Chart";
	Vbar GENDER COLLEGE;
Run;
