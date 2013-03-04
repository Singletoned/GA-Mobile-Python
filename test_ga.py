# -*- coding: utf-8 -*-

import ga


def test_track_page_view():
    ga.UTM_GIF_LOCATION = "http://www.example.com"
    url_args = dict(
        utmn="1234567890",
        utmhn="www.picturehouses.co.uk",
        utmhid="1234567890",
        utmr="-",
        utmp="newsletter-bath-20130227",
        utmac="UA-12345678-3")
    environ = dict(
        HTTP_USER_AGENT="blah")
    res = ga.track_page_view(
        url_args=url_args,
        cookies=dict(),
        environ=environ)
