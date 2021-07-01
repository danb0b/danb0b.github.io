---
layout: home
title: Dan Aukes, Ph.D.
---

![Dan Aukes]({{site.baseurl}}/assets/danaukes.jpg){:width="300px"}

I am a Robotics Researcher, director of the [IDEAlab](http://idealab.asu.edu), and Assistant Professor in the Ira A. Fulton Schools of Engineering, Arizona State University.  This is my personal website 


## Personal Code Projects

{% for post in site.code %}* [{{ post.title }}]({{ post.url }})
{%endfor%}

## Course Pages and Tutorials

* [Foldable Robotics Spring 2021 Course Page](https://egr557.github.io)
* [ROS Tutorial Pages](project_ros_tutorial/)

## Recipes

[Recipes]({{site.baseurl}}/recipes)

## Websites

* [IDEAlab](https://idealab.asu.edu)

## Other Websites

* [ASU Robotics](http://robotics.asu.edu)
* [SCRAMbots](https://www.scrambots.com)
* [Technical Committee on Mechanisms and Design](https://www.robotmechanisms.org)
* [popupCAD](http://www.popupcad.org)

## Slack Workspaces

* [IDEAlab](https://idealab-asu.slack.com)
* [SCRAMbots](https://scram-workspace.slack.com)
* [kaiteki](https://kaiteki-asu.slack.com)
<!--* [New Faculty](https://newfacultyatasu.slack.com)-->
<!--* [EGR314](https://asu-2211-egr314-15063.slack.com)-->
<!--* [EGR304](https://asu-2207-egr304-76246.slack.com)-->
<!--* [EGR557](https://asu-2211-egr557-30967.slack.com)-->

<!--
-->
## Twitter
* [danaukes](https://twitter.com/danaukes)
* [popupCAD](https://twitter.com/popupcad)
* [idealab](https://twitter.com/idealabasu)
* [dave the kangaroo](https://twitter.com/davethekangaroo)
* [scrambots](https://twitter.com/scrambots)

## Bookmarks

<!--
see the [bookmarks]({{site.baseurl}}/bookmarks) page.
-->

{% assign bookmark_pages = site.pages | where: "type", "bookmarks" | sort: "title" %}

{% for item in bookmark_pages %}* [{%if item.title%}{{item.title}}{%else%}{{item.url}}{%endif%}]({{site.baseurl}}{{item.url}}) 
{% endfor %}


## Calendar

<div class="embed-responsive embed-responsive-16by9">
<iframe src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FPhoenix&amp;src=ZGFuYXVrZXNAZ21haWwuY29t&amp;src=bTBmaGZicTkxZmpsYjdwMHBkZGQ2bjFnc2NAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;src=YXN1LmVkdV9iaTV0MDVvbTg0amx0NDN1cGhmc2RscHRwMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&amp;src=OGkxM2k1ZnZmNGVsaGR2Z3U5dDA5Y2piZzBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;src=dGpqYXRwMWJsZTVoMzk3Y2VjY3JnYW1jYjRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;src=czZscDYyZmp2cHR1Nm45YzhuN3Zlc2djMjhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;src=ZGF1a2VzQGFzdS5lZHU&amp;color=%23F09300&amp;color=%234285F4&amp;color=%23795548&amp;color=%23D50000&amp;color=%23C0CA33&amp;color=%239E69AF&amp;color=%23F09300&amp;showTitle=0" style="border-width:0" width="100%" height="600" frameborder="0" scrolling="no"></iframe></div>

