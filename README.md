django-basic-stats
==================

django-basic-stats is a simple traffic statistics application. It show latest referrer, google queried terms or overall hits count.

It also provides optional logging and statistics for mobile devices (user agent, screen and window width/height, device pixel ratio).


Installation
------------
- Add 'stats', to INSTALLED_APPS
- Add 'stats.statsMiddleware.statsMiddleware' to MIDDLEWARE_CLASSES
- Run "syncdb" or "migrate" if you are using South


Enabling mobile device logging
------------------------------
Mobile devices are logged via JavaScript code sending AJAX requests if browser USER AGENT matches one of mobile devices.

Assuming you have jQuery available you will have to add such JavaScript code to you site:

    var ismobile = (/iphone|ipod|android|blackberry|mini|palm|smartphone|ipad|xoom|playbook|tablet|mobile|kindle/i.test(navigator.userAgent.toLowerCase()));
    if (ismobile) {
        $(document).ready(function(){
            $.ajax({
            url: '/stats/mobile/',
            cache: false,
            type: "GET",
            data: {"window_width": window.innerWidth,
            "window_height": window.innerHeight,
            "screen_width": screen.width,
            "screen_height": screen.height,
            "device_pixel_ratio": window.devicePixelRatio},
            });
        });
    }

If you are using other JavaScript library you will have to redo the AJAX sending part. Note that /stats/mobile/ is a hardcoded URL.


Usage
-----
Statistics are visible for site staff. Login to you site as such user and go to /stats/

In Django admin panel you will also get "Mobile" model with all logged mobile devices.
