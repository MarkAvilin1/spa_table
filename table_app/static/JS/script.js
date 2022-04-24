function ajax(page_no) {
    let sorting = document.getElementById("id_sorting");
    let categories = document.getElementById("id_categories");
    let condition = document.getElementById("id_condition");
    let choose = document.getElementById("id_choose");
    $.ajax({
        url: '/httpResponse',
        type: "get",
        data: {
            'pageNumber': page_no,
            'sorting': sorting.value,
            'categories': categories.value,
            'condition': condition.value,
            'choose': choose.value
        },
        dataType: 'json'
    }).done(function (data) {
        let dataTable = data.map(function (data) {
            return data.fields;
        })
        $('#table tbody').empty();
        for (let i = 0; i < dataTable.length; i++) {
            const element = dataTable[i];
            $('#testTmpl').tmpl(element).appendTo('#table tbody');
        }
    })
}

function ajax2() {
    let sorting = document.getElementById("id_sorting");
    let categories = document.getElementById("id_categories");
    let condition = document.getElementById("id_condition");
    let choose = document.getElementById("id_choose");
    $.ajax({
        url: '/httpResponse',
        type: "get",
        data: {
            'sorting': sorting.value,
            'categories': categories.value,
            'condition': condition.value,
            'choose': choose.value
        },
        dataType: 'json'
    }).done(function (data) {
        let dataTable = data.map(function (data) {
            return data.fields;
        })
        $('#table tbody').empty();
        for (let i = 0; i < dataTable.length; i++) {
            const element = dataTable[i];
            $('#testTmpl').tmpl(element).appendTo('#table tbody');
        }
    })
}
