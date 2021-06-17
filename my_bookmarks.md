---
title: Bookmarks
---
# Bookmarks

<!--
see the [bookmarks]({{site.baseurl}}/bookmarks) page.
-->

{% assign bookmark_pages = site.pages | where: "type", "bookmarks" | sort: "title" %}

{% for item in bookmark_pages %}* [{%if item.title%}{{item.title}}{%else%}{{item.url}}{%endif%}]({{site.baseurl}}{{item.url}}) 
{% endfor %}

