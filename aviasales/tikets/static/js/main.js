function press_dropdown(btn){

    select = document.getElementsByClassName('dropdown_select');
    faSortDown = document.getElementsByClassName('sort-down');
    faSortUp = document.getElementsByClassName('sort-up');


    if(btn.value == 'first'){

        for(var i=0; i<select.length; i++){

            document.getElementsByClassName('dropdown_select')[i].style.display = "none";
        }

        for(var i=0; i<faSortUp.length; i++){
            document.getElementsByClassName('sort-up')[0].style.display = "block";
        }

        for(var i=0; i<faSortDown.length; i++){
            document.getElementsByClassName('sort-down')[0].style.display = "none";
        }

        btn.setAttribute('value', 'second')
    }
    else if(btn.value == 'second'){

        for(var i=0; i<select.length; i++){

            document.getElementsByClassName('dropdown_select')[i].style.display = "flex";
        }

        for(var i=0; i<faSortUp.length; i++){
            document.getElementsByClassName('sort-up')[0].style.display = "none";
        }

        for(var i=0; i<faSortDown.length; i++){
            document.getElementsByClassName('sort-down')[0].style.display = "block";
        }

        btn.setAttribute('value', 'first')
    }
}

function press_dropdown2(btn){

    select = document.getElementsByClassName('dropdown_select2');
    faSortDown = document.getElementsByClassName('sort-down2');
    faSortUp = document.getElementsByClassName('sort-up2');


    if(btn.value == 'first'){

        for(var i=0; i<select.length; i++){

            document.getElementsByClassName('dropdown_select2')[i].style.display = "none";
        }

        for(var i=0; i<faSortUp.length; i++){
            document.getElementsByClassName('sort-up2')[0].style.display = "block";
        }

        for(var i=0; i<faSortDown.length; i++){
            document.getElementsByClassName('sort-down2')[0].style.display = "none";
        }

        btn.setAttribute('value', 'second')
    }
    else if(btn.value == 'second'){

        for(var i=0; i<select.length; i++){

            document.getElementsByClassName('dropdown_select2')[i].style.display = "flex";
        }

        for(var i=0; i<faSortUp.length; i++){
            document.getElementsByClassName('sort-up2')[0].style.display = "none";
        }

        for(var i=0; i<faSortDown.length; i++){
            document.getElementsByClassName('sort-down2')[0].style.display = "block";
        }

        btn.setAttribute('value', 'first')
    }
}