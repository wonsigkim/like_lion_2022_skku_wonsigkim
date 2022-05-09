//템플릿 문자열
//백틱으로 값 작성 (`) = 백틱



let str1 = "I'm fine thankyou";
console.log(str1);
let str2 = '"시작이 반이다"';
console.log(str2);
let str3 = `"여러분, '시작이 반이다'들어 보셨죠?"`;
console.log(str3);

//''""가 중복될때 `를 사용하여 표현

let name1 = '철수'
let name2 = '영희'

let string = `${name1}는 ${name2}를 좋아한다.`;
console.log(string);