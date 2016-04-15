data conditional0;
   length Gender $ 1
          Quiz   $ 2;
   input Age Gender Midterm Quiz FinalExam;
   if Missing(Age) then AgeGroup='.';
   	if Age lt 20 then AgeGroup = 1;
   	if Age ge 20 and Age lt 40 then AgeGroup = 2;
   	if Age ge 40 and Age lt 60 then AgeGroup = 3;
   	if Age ge 60 then AgeGroup = 4;

	if  Quiz in ('A+' 'A' 'A-' 'B+' 'B' 'B-' 'C' 'C+' 'C-') then grade="pass";
	else grade="fail";

datalines;
21 M 80 B- 82
.  F 90 A  93
35 M 87 B+ 85
48 F  . .  76
59 F 95 A+ 97
15 M 88 .  93
67 F 97 A  91
.  M 62 F  67
35 F 77 C- 77
49 M 59 C  81
;
run;

data female;
	set conditional0;
	if gender eq 'F';
run;
