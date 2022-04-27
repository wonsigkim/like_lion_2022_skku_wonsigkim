//인수와 매개변수
//

function printFruits(name){
    console.log(name);
};

printFruits('banana');
printFruits('apple');


function printFruitsArr(arr){
    console.log(arr[0]+"은"+arr[1]+"원 입니다");
    }
printFruitsArr(['banana','2000']);


function printFruitsObj(obj){
    console.log(obj.name + "은" + obj.price + "원 입니다");
}
printFruitsObj({name: 'banana', price : '2000'});


//obj/arr=임의의 변수=매개 변수 //데이터에 들어가는 값=인수