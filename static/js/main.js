function validateForm() {
var a = document.forms["myForm"]["Pregnancies"].value;
if (a<0 || a>17){
  alert ("Pregnancies can be in range 0-17");
  return false;
   }

var b = document.forms["myForm"]["Glucose"].value;
if (b<0 || b>199){
  alert ("Glucose can be in range 0-199");
  return false;
   }

var c = document.forms["myForm"]["BloodPressure"].value;
if (c<0 || c>122){
  alert ("BloodPressure can be in range 0-122");
  return false;
   }

var d= document.forms["myForm"]["SkinThickness"].value;
if (d<0|| d>99){
  alert ("Skin Thickness can be in range 0-99");
  return false;
   }

var e = document.forms["myForm"]["Insulin"].value;
if (e<0 || e>846){
  alert ("Insulin can be in range 0-846");
  return false;
   }

var f= document.forms["myForm"]["BMI"].value;
if (f<0 || f>67){
  alert ("BMI can be in range 0-67");
  return false;
   }

var g = document.forms["myForm"]["DiabetesPedigreeFunction"].value;
if (g<0.078 || g>2.42){
  alert ("Diabetes Pedigree Function can be in range 0.078-2.42");
  return false;
   }

var h= document.forms["myForm"]["Age"].value;
if (h<21){
  alert ("Testers Age should be above 21");
  return false;
   }




}