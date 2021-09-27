price=document.querySelectorAll(".price")
add=document.querySelectorAll(".add")
sub=document.querySelectorAll(".sub")
amountvalue=document.querySelector(".amountvalue")
value=document.querySelector(".cartvalue")
function control(data){
    fetch('http://127.0.0.1:8000/additem', {method:'post',headers:{'Accept':'application/json','Content-Type':'application/json'},body:JSON.stringify(data)}).then((res)=>res.json()).then((data)=>{
        data=JSON.parse(data)
console.log(data)
        a=0

        amount=0
for (l of data){
    
   document.getElementById(`value${l[0]}`).innerHTML=l[1][0]
   document.getElementById(`price${l[0]}`).innerHTML=l[1][0]*l[1][1]

   a=a+l[1][0]
   amount=amount+(l[1][0]*l[1][1])
   

   }
  value.innerHTML=a
  console.log(amount)
  amountvalue.innerHTML=amount
    })
}

add.forEach((btn)=>btn.addEventListener("click",()=>{
    id=btn.id
    data={"p_id":parseInt(id.slice(3)), "action":"add" }
 
    
    control(data)
    } ))




    sub.forEach((btn)=>btn.addEventListener("click",()=>{
        
    id=btn.id
    data={"p_id":parseInt(id.slice(3)), "action":"sub" }
   
    cv=document.getElementById(`value${data["p_id"]}`).innerHTML
    
   
    if (cv=="1"){
        console.log("yes")
        document.getElementById(`sub${data["p_id"]}`).className=hvalue
    }
    if (cv!="1"){
    
    control(data)
    }
    
    
    
    } ))