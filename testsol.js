
/**********1번***********/
function solution(amounts) {
    
    var answer = 0;

    for (var i=0; i<amounts.length; i++){
        var pos = amounts[i].replace(',','');
        while(1){
            pos = pos.replace(',','');
            if(parseInt(pos.indexOf(',')) === -1){
                //console.log(pos);
                break;
            }
        }
        answer += parseInt(pos.replace('원',''));
    }
    //console.log(answer);
    return answer;
}

/**********3번***********/
function solution(id) {
    var answer = '';
    var i = id.length;
    var a = parseInt((i/2) - ((i-1)/2/2)); // * 시작값
    answer = id.substr(0, a)+id.substr(a, i/2).replace(/[0-9a-zA-Z]/g,"*")+id.substr(i/2+a, id.length);

    return answer;
}
id = "dkadskdkasdaksdsk";

console.log(solution(id));

