data double;
   Interest = .15;
   Total = 100;
   Year=0;
   do until (Total ge 200);
      Year=Year + 1;
      Total=Total + Interest*Total;
	  output;
   end;
   format Total dollar10.2;
run;

proc print data='double';
run;
