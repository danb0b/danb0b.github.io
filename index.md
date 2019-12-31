---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---

{% capture all_tags %}{% for item in site.recipes %}{% for tag in item.tags %}{{ tag }},{% endfor %}{% endfor %}{%endcapture%}
{% assign tag_words = all_tags | split:',' | sort | uniq %}

## Recipes

{% for word in tag_words %}[{{word}}](#{{word | strip | lower | replace: " ", "-"}}), {% endfor %}

{% for word in tag_words %}
### {{word}}

{% for recipe in site.recipes %}{% if recipe.tags contains word %} * [{{ recipe.title }}]({{ recipe.url }})
{% endif%}{% endfor %}{% endfor %}

### Untagged

{% for recipe in site.recipes %}{% if recipe.tags.size == 0 %} * [{{ recipe.title }}]({{ recipe.url }})
{% endif %}{% endfor %}

### All Recipes
{% for recipe in site.recipes %}* [{{ recipe.title }}]({{ recipe.url }})
{%endfor%}