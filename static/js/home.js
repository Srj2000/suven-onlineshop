add=document.querySelectorAll(".add")
value=document.querySelector(".cartvalue")
add.forEach((btn)=>btn.addEventListener("click",()=>{
    btn.innerHTML="Added"
    data={"p_id":btn.id, "action":"add"}
    fetch('http://127.0.0.1:8000/additem', {method:'post',headers:{'Accept':'application/json','Content-Type':'application/json'},body:JSON.stringify(data)}).then((res)=>res.json()).then((data)=>{
        data=JSON.parse(data)
console.log(data)
a=0
for (l of data){
   a=a+l[1][0]
   }
console.log(a)
value.innerHTML=a

    })
    } ))