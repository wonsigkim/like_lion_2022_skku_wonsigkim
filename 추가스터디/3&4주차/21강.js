//while, do-while, for

//while(조건식){
//    반복코드
//}
//
//항상 참일시 끝나지 않음


let i =1;
while (i<10){
    console.log(i);
    i = i+1;
}


let flag = false;
do{
    console.log('do-while');
}while (flag ==true);

//do while 한번 실행하고 반복의 여부를 판단
//조건을 판단하고 반복을 결정 while