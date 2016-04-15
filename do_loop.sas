data grades1;
   length Gender $ 1
          Quiz   $ 2
          AgeGrp $ 13;
   *infile 'c:\books\learning\grades.txt' missover;
		  *missover: tells SAS to set all the remianing variables to missing if you have more variables than there are data values in one line of raw data;
 	input Age Gender Midterm Quiz FinalExam;
	if missing(Age) then delete; /* go back to the top of DATA step */
	if Age le 39 then do;
		Agegrp = 'Younger group';
      	Grade = .4*Midterm + .6*FinalExam;
   	end;
   	else if Age gt 39 then do;
      	Agegrp = 'Older group';
      	Grade = (Midterm + FinalExam)/2;
   	end;
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
