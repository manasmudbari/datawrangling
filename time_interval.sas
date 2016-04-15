data months_since_visit;
set four_dates;
months = intck('month',VisitDate,today());
run;
