data extract;
   set four_dates;
   Day = weekday(DOB); 
   DayOfMonth = day(DOB);
   Month = Month(DOB);
   Year = year(DOB);
run;

title "Listing of EXTRACT";
proc print data=extract noobs;
   var DOB Day -- Year;
run;
