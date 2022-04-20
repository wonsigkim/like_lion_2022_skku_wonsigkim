let str = "a,b,c";
let str2 = "A,B,C";

console. log(str,str2)

//작은 따옴표로 시작할 경우 장은 따옴표로 마무리, 큰따옴표로 시작을 했으면 큰 따옴표로 마무리

let str4 ="I'm fine thank you";
let str3 ='I"m fine thank you';

console. log(str3,str4)

//표현하고자 하는 문자열에 따옴표가 포함이 되어있다면 묶어주는 따옴표는 다른 따옴 표로 표현

let str5 ="I'm fine thank you \"And, you?\"";

console. log(str5)

//문자열 안에 따옴표 두종류가 모두 포한 될 시 따옴표 앞에 '\'(역슬래시)를 이용하여 해당 따옴표가 문자임을 표현