function setDates(date){
    var date = new Date(),
    targetDay = 1, 
    targetDate = new Date(),
    delta = targetDay - date.getDay();
    
    if (delta >= 0) {
        targetDate.setDate(date.getDate() - delta)
    }
    
    else {
        targetDate.setDate(date.getDate() + delta)
    }
    
    for(let i=0; i<6; i++){
    targetDate.setDate(targetDate.getDate()+i);
    
    let months = ['01','02','03','04','05','06','07','08','09','10','11','12'];
    var month = months[targetDate.getMonth()];
    let w_days = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
    var w_day = w_days[targetDate.getDay()];
    let days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
    var day = days[targetDate.getDate()-1]
    t_year = targetDate.getFullYear();
    let a = String(t_year)[2];
    let b = String(t_year)[3];
    let year = a+b;
    var res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_"+1).innerHTML = res;
    }
    
    return res;
    alert(res);
}

function test(key, a) {
        if (key == "Enter"){
            text = a.value.toUpperCase();
            
            if(text.length != 10){
                alert("Введите группу!");
                a.value = "";
            } 
         else{
               setDates(new Date());
               //document.getElementById("day_1").innerHTML = setDates(new Date());
               //document.getElementById("day_2").innerHTML = setDates(new Date());
               //document.getElementById("day_3").innerHTML = setDates(new Date());
               //document.getElementById("day_4").innerHTML = setDates(new Date());
               //document.getElementById("day_5").innerHTML = setDates(new Date());
               //document.getElementById("day_6").innerHTML = setDates(new Date());
               a.value = "";
               }
        }
}
    