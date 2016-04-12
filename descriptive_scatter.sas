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

/*sorting the data to be used in the side by side boxplot*/
proc sort data = htwt OUT=HTWT_SORTED;
	by GENDER;
run;

proc boxplot data=HTWT_SORTED;
	Title "Side-by-side Boxplot for gender and height";
	plot height*gender; /*quantitative * categorical*/
run;

proc gplot data=HTWT;
	Title "Scatterplot of weight vs. height";
	plot WEIGHT*HEIGHT; /*Y*X*/
run;


proc gplot data=HTWT;
	Title "Scatterplot of weight vs. height with gender group";
	plot WEIGHT*HEIGHT=GENDER; /*Y*X*/
run;


proc sort data=HTWT;
	by college gender;
run;

/*Printing the side by side boxplot of height by college and gender*/
proc boxplot data=HTWT;
	Title "boxplot of height by college and gender";
	plot WEIGHT*HEIGHT (GENDER); /*Y*X*/
run;
