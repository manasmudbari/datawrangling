data veg5;
infile 'C:\Users\mainlab\Documents\SAS_data\veggies_fixed.txt';
informat	Name $8. 
			Code $7. 
			Days 2.
			Number 4.
			Price 3.;
input name code days number price;
run;

title "reading using informat";
proc print data=veg5;
format price dollar4.0;
run;
