var Cal = function (divId) {

    //Сохраняем идентификатор div
    this.divId = divId;

    // Дни недели с понедельника
    this.DaysOfWeek = [
        'Пн',
        'Вт',
        'Ср',
        'Чтв',
        'Птн',
        'Суб',
        'Вск'
    ];

    // Месяцы начиная с января
    this.Months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];

    //Устанавливаем текущий месяц, год
    var d = new Date();

    this.currMonth = d.getMonth();
    this.currYear = d.getFullYear();
    this.currDay = d.getDate();
};

// Переход к следующему месяцу
Cal.prototype.nextMonth = function () {
    if (this.currMonth == 11) {
        this.currMonth = 0;
        this.currYear = this.currYear + 1;
    } else {
        this.currMonth = this.currMonth + 1;
    }
    this.showcurr();
};

// Переход к предыдущему месяцу
Cal.prototype.previousMonth = function () {
    if (this.currMonth == 0) {
        this.currMonth = 11;
        this.currYear = this.currYear - 1;
    } else {
        this.currMonth = this.currMonth - 1;
    }
    this.showcurr();
};


Cal.prototype.showall = function () {
    for (var i = 0; i <= 11; i++) {
        this.showMonth(this.currYear, i);
    }
};

var full_html = ''

// Показать месяц (год, месяц)
Cal.prototype.showMonth = function (y, m) {
    var html = '<table>';
    var d = new Date()
        // Первый день недели в выбранном месяце
        , firstDayOfMonth = new Date(y, m, 7).getDay()
        // Последний день выбранного месяца
        , lastDateOfMonth = new Date(y, m + 1, 0).getDate()
        // Последний день предыдущего месяца
        , lastDayOfLastMonth = m == 0 ? new Date(y - 1, 11, 0).getDate() : new Date(y, m, 0).getDate();

    // Запись выбранного месяца и года
    html += '<tr>';
    html += '<td colspan="7">' + this.Months[m] + ' ' + y + '</td>';
    html += '</tr>';


    // заголовок дней недели
    html += '<tr class="days">';
    for (var i = 0; i < this.DaysOfWeek.length; i++) {
        html += '<td>' + this.DaysOfWeek[i] + '</td>';
    }
    html += '</tr>';

    // Записываем дни
    var i = 1;
    do {
        var dow = new Date(y, m, i).getDay();

        // Начать новую строку в понедельник
        if (dow == 1) {
            html += '<tr>';
        }

        // Если первый день недели не понедельник показать последние дни предыдущего месяца
        else if (i == 1) {
            html += '<tr>';
            var k = lastDayOfLastMonth - firstDayOfMonth + 1;
            for (var j = 0; j < firstDayOfMonth; j++) {
                html += '<td class="not-current">' + k + '</td>';
                k++;
            }
        }

        // Записываем текущий день в цикл
        var chk = new Date();
        var chkY = chk.getFullYear();
        var chkM = m + 1;
        var month_to_id = chkM
        id_name = 'date_' + chkY + '_' + chkM + '_' + i;
        html += '<td class="normal" id="' + id_name + '">' + i + '</td>';

        // закрыть строку в воскресенье
        if (dow == 0) {
            html += '</tr>';
        }
        // Если последний день месяца не воскресенье, показать первые дни следующего месяца
        else if (i == lastDateOfMonth) {
            var k = 1;
            for (dow; dow < 7; dow++) {
                html += '<td class="not-current">' + k + '</td>';
                k++;
            }
        }

        i++;
    } while (i <= lastDateOfMonth);

    // Конец таблицы

    html += '</table>';
    // Записываем HTML в div
    full_html += html
    //document.getElementById(this.divId).innerHTML = html;
    document.getElementById("calendar").innerHTML = full_html

};


function testPrint() {
    var json_data = JSON.parse(document.getElementById("json_data").innerText)
    json_data.forEach((item) => {

        var item_id = 'date_' + item[1] + '_' + item[2] + '_' + item[3];
        try {
            if (document.getElementById(item_id).style.color === 'red') {
                document.getElementById(item_id).style.background = 'orange'
            } else {
                document.getElementById(item_id).style.color = 'red'
            }
        } catch (e) {
            console.log(e)
        }

    })
}

// При загрузке окна
window.onload = function () {
    // Начать календарь
    var c = new Cal("calendar");
    c.showall();
    testPrint()


}

// Получить элемент по id
function getId(id) {
    return document.getElementById(id);
}
