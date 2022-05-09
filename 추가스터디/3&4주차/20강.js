//조건문
//if, switch

//switch (key){
//    case value1:
//        break;
//    case value2:
//        break;
//    case value3:
//        break;
//        default:
//        break;
//}



let animal = 'Dog'

switch(animal){
    case 'Cat':
        console.log('야옹');
        break;
    case 'Chick':
        console.log('짹짹');
        break;
    case 'Dog':
        console.log('멍멍');
        break;
    case 'Cow':
        console.log('음메');
        break;
    default:
        console.log('일치하는 동물이 없습니다');
        break;
}


//break가 없으면 break가 나오기 전까지 실행