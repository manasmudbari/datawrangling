data survey1;
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

libname newfmts 'C:\Users\mainlab\Downloads\SAS_dataset';

proc format library=newfmts;
	value YESNO	1='Yes'
				2='No';
	value $YESNO 	'Y'='Yes'
					'N'='No';
	
