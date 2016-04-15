data six_months;
set four_dates;
reminder = intnx('month',VisitDate,6);
next_visit= intnx('month',VisitDate,6,'sameday');
format reminder next_visit date9.;
run;
