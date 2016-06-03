libname learn "C:\Users\mainlab\Downloads\SAS_dataset";

title;

*Program 26-12 Using PROC SQL to perform a fuzzy match;
proc sql;
title "Example of a Fuzzy Match";
select Subj,
h.Name as health_name,
i.Name as insurance_name
from learn.demographic as h,
learn.insurance as i
where spedis(health_name,insurance_name) le 25;
quit;
