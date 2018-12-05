var csrftoken = Cookies.get('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function addSpot(data) {
    if (data['spots'].length > 0) {
        var spotsElement = document.getElementById('spots');

        spotsElement.textContent = null;

        data['spots'].forEach(function (spot) {
            // console.log(spot);
            var elemLi = document.createElement('li');
            var elemPSpotAddress = document.createElement("p");
            elemPSpotAddress.textContent = '📍' + spot['address'];
            var elemPDistance = document.createElement("p");
            elemPDistance.textContent = '👣' + Math.round(spot['distance']) + 'm';

            if (spot['content_url']) {
                elemA = document.createElement('a');
                elemA.appendChild(elemPSpotAddress);
                elemA.appendChild(elemPDistance);
                elemA.href = spot['content_url'];
                elemA.target = '_blank';
                elemA.onclick = function(){
                    gtag('event', 'connect_wifi', {'event_category': 'conversion', 'event_label': spot['address'] })
                };
                // console.log(elemA.onclick);
                elemLi.appendChild(elemA);
            } else {
                elemLi.appendChild(elemPSpotAddress);
                elemLi.appendChild(elemPDistance);
                elemLi.classList.add('demo-no-swipe');
                elemLi.classList.add('demo-no-reorder');
            }
            spotsElement.appendChild(elemLi);
        });
    } else {
        console.log('Spots is empty.');
    }
}


function fetchSpot(latitude, longitude) {
    var url = '/spots';

    var payload = {
        latitude: latitude,
        longitude: longitude
    };

    // Ajax通信を開始
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: payload,
        timeout: 5000
    })
        .done(function (data) {
            // 通信成功時の処理を記述
            gtag('event', 'fetch_spot');
            addSpot(data);
        })
        .fail(function () {
            // 通信失敗時の処理を記述
            console.log('Connect Fail');
        });
}


function success(position) {
    gtag('event', 'watch_position', {'event_category': 'conversion'});
    fetchSpot(position.coords.latitude, position.coords.longitude);
}


function error(err) {
    console.warn('ERROR(' + err.code + '): ' + err.message);
    var statusElement = document.getElementById('status');
    statusElement.textContent = '本サイトを使用するには位置情報利用の許可が必要です。ページを再読込したり、ブラウザの設定を変えるなどして本サイトへの位置情報の利用を許可してください';
}


var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};

if ("geolocation" in navigator) {
    /* geolocation is available */
    navigator.geolocation.watchPosition(success, error, options);
} else {
    /* geolocation IS NOT available */
    console.log('geolocation IS NOT available');
}