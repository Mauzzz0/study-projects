var weeks = 0;

function setDates(){
    var date = new Date(),
    targetDay = 1, 
    targetDate = new Date();
    var delta = targetDay - date.getDay();

    if (delta > 0) {targetDate.setDate(date.getDate()-6)}
    
    else {
        targetDate.setDate(date.getDate() + delta);
        document.getElementById("day_"+date.getDay()).style.backgroundImage = "linear-gradient(-60deg, #ff5858 0%, #f09819 100%)";
    }
    
    const months = ['01','02','03','04','05','06','07','08','09','10','11','12'];
    const w_days = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
    const days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
    
    var t_year = targetDate.getFullYear();
    let a = String(t_year)[2];
    let b = String(t_year)[3];
    
    var month = months[targetDate.getMonth()];
    var w_day = w_days[targetDate.getDay()];
    var day = days[targetDate.getDate()-1]
    let year = a+b;
    var res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_1").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_2").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_3").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_4").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_5").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_6").innerHTML = res;
    
    
}

function load(key, a) {
    text = a.value.toUpperCase();
    if (key == "Enter"){
        if(text.length != 10){
            a.value="";
            alert("Введите группу!");
            
        } 
        else{
            alert("Расписание для группы: "+text);
            document.getElementById('now_week').scrollIntoView();
        }
    }
}


 
function set_next_week(){
    weeks+=1;
    var date = new Date();
    date.setDate(date.getTime()+(86400000*7*weeks));
    var targetDay = 1, 
    targetDate = new Date(),
    delta = targetDay - date.getDay();
    
    if(delta=1){
        targetDate.setDate(date.getDate()+1)
    }
    
    else{
    if (delta >= 0) {targetDate.setDate(date.getDate() - delta)}
    
    
    else {targetDate.setDate(date.getDate() + delta)}
    }
    
    let months = ['01','02','03','04','05','06','07','08','09','10','11','12'];
    let w_days = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
    let days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
    t_year = targetDate.getFullYear();
    let a = String(t_year)[2];
    let b = String(t_year)[3];
    
    var month = months[targetDate.getMonth()];
    var w_day = w_days[targetDate.getDay()];
    var day = days[targetDate.getDate()-1]
    let year = a+b;
    var res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_1").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_2").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_3").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_4").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_5").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_6").innerHTML = res;
    
}

function set_previous_week(){
    weeks-=1;
    var date = new Date();
    date.setDate(date.Date()+(7*weeks));
    var targetDay = 1, 
    targetDate = new Date(),
    delta = targetDay - date.getDay();
    
    if(delta=1){
        targetDate.setDate(date.getDate()+1)
    }
    
    else{
    if (delta >= 0) {targetDate.setDate(date.getDate() - delta)}
    
    
    else {targetDate.setDate(date.getDate() + delta)}
    }
    
    let months = ['01','02','03','04','05','06','07','08','09','10','11','12'];
    let w_days = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
    let days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
    t_year = targetDate.getFullYear();
    let a = String(t_year)[2];
    let b = String(t_year)[3];
    
    var month = months[targetDate.getMonth()];
    var w_day = w_days[targetDate.getDay()];
    var day = days[targetDate.getDate()-1]
    let year = a+b;
    var res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_1").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_2").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_3").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_4").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_5").innerHTML = res;
    
    targetDate.setDate(targetDate.getDate()+1);
    month = months[targetDate.getMonth()];
    w_day = w_days[targetDate.getDay()];
    day = days[targetDate.getDate()-1]
    year = a+b;
    res = w_day+" "+"("+day+"."+month+"."+year+")";
    document.getElementById("day_6").innerHTML = res;
}