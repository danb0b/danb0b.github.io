---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---

## Recipes

{% for recipe in site.recipes %}* [{{ recipe.title }}]({{ recipe.url }})
{%endfor%}