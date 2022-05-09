//조건문
//if, switch

if(10<20){
    console.log('10은 20보다 작습니다');
}

//if 조건문은 참일때만 실행됨

if(10>20){
    console.log('10은 20보다 작습니다');
}else{
    console.log('10은 20보다 큽니다');
}

//else 는 한번만 사용가능

if(10>30){
    console.log('10은 30보다 큽니다');
}else if(10>20){
    console.log('10은 20보다 큽니다');
}else if(10<20){
    console.log('10은 20보다 작습니다');
}

//else if 는 여러번 사용 가능

if(10>30){
    console.log('10은 30보다 큽니다');
}else if(10>20){
    console.log('10은 20보다 큽니다');
}else {
    console.log('모두 거짓입니다');
}
