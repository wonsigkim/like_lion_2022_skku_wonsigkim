//function(함수) 연관된 코드들을 모아놓은 자료형
// 함수 선언식      fuction 함수명(){}
// 함수 표현식      const[변수명] = fuction[함수명](){}//code  *중요한건 변수의 이름
// 함수 표현식에서 함수의 이름이 없는 경우 '익명함수'라고 불린다 anonymous funstion

console.log("3*1=3")
console.log("3*2=6")
console.log("3*3=9")
console.log("3*4=12")
console.log("3*5=15")
console.log("3*6=18")
console.log("3*7=21")
console.log("3*8=24")
console.log("3*9=27")
console.log("3*10=30")

function gugudan(){
    console.log("3*1=3");
    console.log("3*2=6");
    console.log("3*3=9");
    console.log("3*4=12");
    console.log("3*5=15");
    console.log("3*6=18");
    console.log("3*7=21");
    console.log("3*8=24");
    console.log("3*9=27");
    console.log("3*10=30");
}

gugudan();


const gugudan = function gugudan(){
    console.log("3*1=3");
    console.log("3*2=6");
    console.log("3*3=9");
    console.log("3*4=12");
    console.log("3*5=15");
    console.log("3*6=18");
    console.log("3*7=21");
    console.log("3*8=24");
    console.log("3*9=27");
    console.log("3*10=30");
};

gugudan();