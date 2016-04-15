data ages;
   set four_dates;
   Visit_Age = round(yrdif(DOB,VisitDate,'Actual'));
   Current_Age = round(yrdif(DOB, today(),'Actual'));
   Age_to_2009 = round(yrdif(DOB, '01Jan2009'd, 'Actual'));
label visit_age = 'age at visit'
	current_age = 'age of today'
	age_to_2009 = 'age on 01/01/2009';
run;
