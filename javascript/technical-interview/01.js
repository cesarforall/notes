function solution(param1, param2) {
    const isParam1Between = param1 > -1001 && param1 < 1001
    const isParam2Between = param2 > -1001 && param2 < 1001
    if (isParam1Between && isParam2Between) {
        const sum = param1 + param2;
        return sum;     
    }
}
