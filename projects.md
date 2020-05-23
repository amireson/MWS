---
layout: page
title: Project Archive
---

{% for i in (2019..2020) %}

# {{ i }}
{% for proj in site.projects %}
{%if proj.year == i %}
[{{ proj.author }}:]({{site.baseurl}}{{ proj.url }})
{{ proj.title }}
{% endif %}
{% endfor %}

{% endfor %}

