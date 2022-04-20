//숫자형

let integer = 10;
let hex = 0xa;
let binary = 0b1010;
let octal = 0o12;

console.log(integer,hex,binary,octal);

let negative = -10
let indices = 1.0e1;
let double = 10.12;

console.log(negative,indices,double);

//javascript 는 모든 숫자를 10진수로 표현

let IsInfinity = 10/0;
let IsNaN = 10/"칠";

console.log(IsInfinity, IsNaN);

//무한대는 infinity로 출력, 숫자가 아닌경우 NaN으로 출력

let sum = 0.1 + 0.2;

console. log(sum)

//실수끼리 사칙연산을 하더라도 컴퓨터가 이진수로 저장을 하기 떄문에 오류 발생가능