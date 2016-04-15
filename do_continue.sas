data continue_on;
   Interest = .15;
   Total = 100;
   do Year = 1 to 100 until (Total ge 200);
      Total = Total + Interest*Total;
	  *output;
      if Total le 150 then continue; /* go back to the top when total is less than 150 */
      output;
   end;
   format Total dollar10.2;
run;
