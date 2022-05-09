//화살표 함수
//const sum = function sum(){}

()=>{}
//식별자가 없음

//const sum = (num1,num2)=> num1 + num2;
//
//const result = sum(10,20);
//console.log(result);


//const pow = x => x*x
//
//const result = pow(10);
//console.log(result);

//const printpie = () =>3.14
//
//const result = printpie()
//console.log(result);

//const getObject = () =>({
//    name: "철수",
//    age:25
//})
//
//const obj = getObject()
//console.log(obj.name);

//function outer(x){
//    return function inner(){
//        return x*x
//    }
//
//}
//
//const innerFunc = outer(10);
//const result = innerFunc();
//console.log(result);

//const outer = (x)=>function inner(){
//        return x*x
//    }
//
//
//const innerFunc = outer(10);
//const result = innerFunc();
//console.log(result);


const outer = (x)=>() =>x*x



const innerFunc = outer(10);
const result = innerFunc();
console.log(result);