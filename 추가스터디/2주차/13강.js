//return: 함수를 호출한 시점으로 데이터를 전달(반환)

function sum(number1,number2){
    return number1+number2;
}

const sum_result_1 = sum(10,20);
const sum_result_2 = sum(30,50)

const sum_result = sum_result_1 + sum_result_2;

console.log("총합은"+sum_result+"입니다")


function PrintReturn(){
console.log('return 실행전');
return
console.log('return 실행후');
}

PrintReturn();