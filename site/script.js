let weeks = 0,
    month_delta,
    year_delta,
    t_year, a, b, month, w_day, day, year, res;

const today = new Date();

const selGroupInput = document.querySelector(".input_group"),
    nextWeek = document.querySelector('.next_week'),
    previousWeek = document.querySelector('.previous_week'),
    logo = document.querySelector('.logo');

const months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],

    w_days = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],

    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 
            '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'];

function setDates(date) {

    targetDay = 1,
        targetDate = new Date();

    if (targetDate.getYear() < date.getYear()) {
        year_delta = date.getYear() - targetDate.getYear();
        targetDate.add(1 * year_delta).year();

    } else if (targetDate.getYear() > date.getYear()) {
        year_delta = targetDate.getYear() - date.getYear();
        targetDate.add(-1 * year_delta).year();
    }

    if (targetDate.getMonth() < date.getMonth()) {
        month_delta = date.getMonth() - targetDate.getMonth();
        targetDate.add(1 * month_delta).month();

    } else if (targetDate.getMonth() > date.getMonth()) {
        month_delta = targetDate.getMonth() - date.getMonth();
        targetDate.add(-1 * month_delta).month();
    }

    let delta = targetDay - date.getDay();

    if (delta > 0) {
        targetDate.setDate(date.getDate() + 1)
    } 
    else {
        targetDate.setDate(date.getDate() + delta);
        if (date.getDate() === (new Date()).getDate()) {
            document.getElementById("day_" + today.getDay()).style.backgroundImage = "linear-gradient(-60deg, #ff5858 0%, #f09819 100%)";
        } else {
            document.getElementById("day_" + today.getDay()).removeAttribute('style');
        }
    }

    for (let i = 1; i < 7; i++) {
        t_year = targetDate.getFullYear();
        a = String(t_year)[2];
        b = String(t_year)[3];
        month = months[targetDate.getMonth()];
        w_day = w_days[targetDate.getDay()];
        day = days[targetDate.getDate() - 1]
        year = a + b;
        res = w_day + " " + "(" + day + "." + month + "." + year + ")";
        document.getElementById("day_" + i).innerHTML = res;
        targetDate.setDate(targetDate.getDate() + 1);
    }
}

function load(key, a) {
    const text = a.value.toUpperCase();
    if (key == "Enter") {
        if (text.length != 10) {
            a.value = "";
            alert("Введите группу!");
        } else {
            console.log("Расписание для группы: " + text);
            document.getElementById('now_week').scrollIntoView();
        }
    } else {}
}


document.addEventListener("DOMContentLoaded", () => {
    let date = new Date();
    setDates(date, 'y');
});

selGroupInput.addEventListener('keydown', (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
    }
    load(event.key, selGroupInput);
});

nextWeek.addEventListener('click', () => {
    weeks++;
    let datePlus = new Date();
    datePlus.add(7 * weeks).days();
    setDates(datePlus);
    console.log(weeks);
});

previousWeek.addEventListener('click', () => {
    weeks--;
    let dateMin = new Date();
    dateMin.add(7 * weeks).days();
    setDates(dateMin);
    console.log(weeks);
});

logo.addEventListener('click', () => {
    setDates(new Date());
    weeks = 0;
});