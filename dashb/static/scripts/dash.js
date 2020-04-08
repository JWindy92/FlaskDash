desk_light = document.querySelector('#desk-light input');
table_lamp = document.querySelector('#table-lamp input');
desk_strip = document.querySelector('#desk_strip input');
bed_lamp = document.querySelector('#bed-lamp input');
movie_button = document.querySelector('#bed-lamp button')

desk_light.addEventListener('change', function() {
    toggle_power('desk-light')
})

table_lamp.addEventListener('change', function() {
    toggle_power('table-lamp')
})

bed_lamp.addEventListener('change', function() {
    toggle_power('bed-lamp', service="yeelight")
})

movie_button.addEventListener('click', function() {
    var data_obj = {
        "service": "yeelight",
        "command": "movie"
    }
    
    $.ajax({
        type:"POST",
        url:`/lights/bed-lamp`,
        contentType: 'application/json',
        dataType: "json",
        data : JSON.stringify(data_obj)
    })
})

desk_strip.addEventListener('change', function() {
    var message = {
        "brightness": 255,
        "effect": "solid",
        "color": {"r": 132, "g": 3, "b": 252},
    }
    if ($(`#desk_strip input[type=checkbox]`).prop('checked')) {
        message["state"] = 'ON';
    } else {
        message["state"] = 'OFF';
    }
    toggle_power('desk_strip', service="custom", custom_object=message, custom_topic='johnw/desk_strip/set')
})



function toggle_power(device_name, service='mqtt', custom_object={}, custom_topic="") {
    {
        if ($(`#${device_name} input[type=checkbox]`).prop('checked')) {
            var command = 'ON';
        } else {
            var command = 'OFF'
        }
        if (service == 'custom') {
            var data_obj = {
                'payload': custom_object
            }
            if (custom_topic) {
                data_obj['topic'] = custom_topic
            }
        } else {
            var data_obj = {
                'service': service,
                'command': command
            };
        }
    
        $.ajax({
            type:"POST",
            url:`/lights/${device_name}`,
            contentType: 'application/json',
            dataType: "json",
            data : JSON.stringify(data_obj)
        })
    }
}

// if ($('input[type=checkbox]').prop('checked')) {
//     var command = 'ON';
// } else {
//     var command = 'OFF'
// }
// var data_obj = {
//     'service': 'mqtt',
//     'command': command
// };

// $.ajax({
//     type:"POST",
//     url:"/lights/desk-light",
//     contentType: 'application/json',
//     dataType: "json",
//     data : JSON.stringify(data_obj)
// })