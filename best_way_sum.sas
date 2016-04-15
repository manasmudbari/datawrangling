data revenue1;
   input Day : $3.
         Revenue : dollar6.;
   Total + Revenue;
   format Revenue Total dollar8.2;
datalines;
Mon $1,000
Tue $1,500
Wed  .     
Thu $2,000
Fri $3,000
Sat $8,000
Sun $15,000
;
run;
