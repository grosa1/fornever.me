﻿# -*- coding: utf-8 -*-

from django.http import HttpResponse

def sitemap_robocode_xml(request):
    return HttpResponse('''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://fornever.no-ip.org/robocode/sniper/</loc>
   </url>
</urlset>''')