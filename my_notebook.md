---
---
{% for item in site.notebook %}
* [{{item.title}}]({{site.baseurl}}{{item.url}}){% endfor %}