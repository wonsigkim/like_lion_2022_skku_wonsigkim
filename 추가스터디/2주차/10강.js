//object 는 key와 value로 구성

let student1 = {
    koreanlag:90,
    english:80,
    math:70,
    science:60
};

console.log(student1)

//대괄호 연산자 [변수이름"key"]

console.log(student1["koreanlag"]);

//.(점)연산자 변수이름.key

console.log(student1.english);

//문자열로 key를 적어도 문제 없음
//차이점 key의 이름 띄어쓰기 가능
//띄어쓰기가 있는 경우 (점)연산자는 사용 불가