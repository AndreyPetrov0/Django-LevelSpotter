function updateIcon(val) {
    const icon = document.getElementById('status-icon');
    if (!icon) return;

    if (val === "" || val === "+" || val === "-") {
        icon.src = "{% static 'spotter/images/transparent_back.png' %}";
    } else if (val.startsWith('+')) {
        icon.src = "{% static 'spotter/images/up_arrow.png' %}";
    } else if (val.startsWith('-')) {
        icon.src = "{% static 'spotter/images/down_arrow.png' %}";
    }
}

function addDigit(input) {
    let form = document.forms['form_correct'];
    if (!form) return;
    
    let field = form.elements['correct_value'];
    let currentVal = field.value;
    let maxt = 4;


    if (input === '<') {
        field.value = currentVal.slice(0, -1);
        updateIcon(field.value);
        return;
    }

    if (input === '-') {
        if (currentVal.startsWith('-')) {
            field.value = '+' + currentVal.slice(1);
        } else if (currentVal.startsWith('+')) {
            field.value = '-' + currentVal.slice(1);
        } else {
            field.value = '-';
        }
        updateIcon(field.value);
        return;
    }

    if (currentVal.length < maxt) {
        if (input === '0') {
            if (currentVal === "" || currentVal === "+" || currentVal === "-") {
                return; 
            }
        }

        if (currentVal.startsWith('+') || currentVal.startsWith('-')) {
            field.value += input;
        } else {
            field.value = '+' + input;
        }
    }
    
    updateIcon(field.value);
}