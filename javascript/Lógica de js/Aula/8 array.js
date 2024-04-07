oi = [1,2 ,[3,4]]
console.log(oi[2][0])

console.log('')
function sss(arr){
    let contar = 0
    for(i in arr){
        console.log(i)
        contar++
    }
    return contar
}

meuarr = [1, 2, 4, 3, 6]
console.log(sss(meuarr))