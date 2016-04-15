data survey;
	infile 'C:\Users\mainlab\Downloads\Original dataset\survey.txt';
	input 	ID: $3.
			Gender : $1.
			Age
			Salary
			(Ques1-Ques5) (: $1.);

		label 	ID = 'Subject ID'
				Gender = 'Gender'
				Age = 'Age as of 1/1/2006'
				Salary = 'Yearly Salary'
				Ques1 = 'The governor doing a good job?'
				Ques2  = 'The property tax should be lowered'
         		Ques3  = 'Guns should be banned'
         		Ques4  = 'Expand the Green Acre program'
         		Ques5  = 'The school needs to be expanded';
run;

proc format;
	value $gender 	'M'='Male'
					'F'='Female'
					' '='Not entered'
					other='Miscoded';
	value age 		low-29='less than 30'
					30-50='30 to 50'
					51-high='51+';
	value $likert	'1'='Strongly disagree'
					'2'='Disagree'
					'3'='neutral'
					'4'='Agree'
					'5'='Strongly agree';
run;

proc format;
	value $three '1', '2' ='Disagreement'
	'3' = ' No opinion'
	'4','5' ='Agreement';
run;

proc freq;
	tables ques1-ques5;
	format ques1-ques5 $three.;
run;

libname sasfmts 'C:\Users\mainlab\Downloads\SAS_dataset';
/* creating permanent formats */
proc format library=sasfmts;
	value $gender 		'M'='Male'
					'F'='Female'
					' '='Not entered'
					other='Miscoded';
run;

libname sasfmts 'C:\Users\mainlab\Downloads\SAS_dataset';
options fmtsearch=(sasfmts); /* also search sasfmts for formats */
/* display your formats */
proc format library=sasfmts fmtlib;
run;
