function nextPage(page) {
    window.location.href=page;
}

function changePeriod(){
    var d = new Date();
    hour = d.getHours();
    minute = d.getMinutes();
    // oh hell no I am not coding A day B day
    // or steam 
    if((hour == 8 && 30 <= minute) || (hour == 9 && min < 45)){
        window.location.href="../P1";
    }else if((hour == 9 && 45 <= minute) || (hour == 11 && min < 25)){
        window.location.href="../P2";   
    }else if((hour == 11 && 25 <= minute) || (hour == 1 && min < 30)){
        window.location.href="../P3";   
    }else if((hour == 1 && 30 <= minute) || (hour == 3 && min < 10)){
        window.location.href="../P4";   
    }else if((hour == 3 && 10 <= minute) || (hour == 4 && min < 10)){
        window.location.href="../P8";  
    }else{
        window.location.href="/"
    }
}    