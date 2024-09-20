
const mainDiv = document.getElementById('main')
console.log(mainDiv)
let res
const fun = async(name)=>{
    const data = await fetch(`/${name}.html`)
    if(data.ok)
    {
        res = await  data.text()
        mainDiv.innerHTML = res
    }else
    {
        fun("404")
    }

}

fun("test")
