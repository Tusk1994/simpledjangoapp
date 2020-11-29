
function define_url(val) {
    return (val === 'l') ? '/line/' : '/column/';
};

function change_graph() {
    $('#bt_graph').attr('disabled', true);
    $.ajax({
        url:  define_url($('#bt_graph').attr('value')),
        success: function (data) {
            console.log(JSON.parse(data))
            // Take data from server
            make_graph(JSON.parse(data));
            change_url();
        },
        onerror: function (data) {
            console.log(data);
        }
    });
};


// Delay for button
$(document).ajaxComplete(function () {
    setTimeout(function(){
        $('#bt_graph').attr('disabled', false);
    }, 0)
});


function change_url() {
    let bt_graph = $('#bt_graph')
    if (define_url( bt_graph.attr('value')) === '/line/') {
        bt_graph.attr('value', 'c');
    } else {
        bt_graph.attr('value', 'l')
    };
};


function make_graph(context) {

    Highcharts.chart('container', {

        chart: context.chart,

        title: {
            text: context.title
        },

        credits: {
            enabled: false
        },

        yAxis: context.yAxis,

        xAxis: context.xAxis,

        legend: {
            enabled: false
        },

        series: context.series,

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                },
            }]
        }
    });
}