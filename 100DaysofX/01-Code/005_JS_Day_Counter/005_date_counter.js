// #100DaysofCode - Day 5
// 005_date_counter.js
// display the current day # of current challenge

var date_diff_indays = function (date1, date2) {
    d1 = new Date(date1);
    d2 = new Date(date2);
    return Math.floor((Date.UTC(d2.getFullYear(), d2.getMonth(), d2.getDate()) - Date.UTC(d1.getFullYear(), d1.getMonth(), d1.getDate())) / (1000 * 60 * 60 * 24));
}

d1_begin = new Date(2019, 2, 4);
chal_num = 0;

document.getElementById("dButt").onclick = function () {
    document.getElementById("begin").innerHTML = document.getElementById("begin").innerHTML + d1_begin.toDateString();

    d_current = new Date();
    document.getElementById("current").innerHTML = document.getElementById("current").innerHTML + d_current.toDateString();

    day_count = document.getElementById("count").innerHTML + date_diff_indays(d1_begin, d_current);

    document.getElementById("count").innerHTML = day_count;

    if (0 < day_count <= 100) {
        chal_num = 1;
    } else if (100 < day_count <= 200) {
        chal_num = 2;
    } else if (200 < day_count <= 300) {
        chal_num = 3;
    }

    document.getElementById("chal").innerHTML = document.getElementById("chal").innerHTML + chal_num;

}