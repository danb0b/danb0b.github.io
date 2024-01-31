---
title: Incredible Feats of Productivity
summary: Or, how I twiddle my setup constantly to maximize feelings of success
date: 2024-01-31
draft: true
---

## Introduction

The purpose of this article is to document some of my best practices in my work setup.  I will try to detail how they are all connected together in this blog, and connect it to specific tutorials and how-to's located elsewhere, if necessary.

Keep in mind that many of the projects I've listed here have been 5+ years in the making; I have slowly, glacially, changed as my needs have gotten more pressing.  First one thing, then the other.

## Software Stack

### Ubuntu

I finally switched over to Ubuntu full time about 2 years ago, though te love affair goes back decades.  My original Linux installation was dapper drake, some time in the 2005-2007 time frame, on a home-built pc I put together.  It was great, and I didn't just try it out briefly but had it installed for a while.  I even got RAID working with my built in motherboard controller, which was impressive for me at the time, but ultimately it didn't work, because some of my favorite software from work and school, including Matlab, Solidworks, Visual Studio, etc, were not released for Linux, requiring me to have a second computer.

Moving forward to grad school, I was doing my PhD when ROS first came on the market.  It was inextricably tied to Ubuntu at the time, which gave me a reason to revisit it.  I got into linux again for the second time.  It was usable, but again, I was still tied to Solidworks.

It was also during this time that I made the migration from Matlab to Python, because I was sick of the Matlab license server failing when my wifi got bad.  This removed one tether from my Windows dependency.

I finally made the plunge, not so much because I was no longer using Solidworks (which I hadn't used consistently in a long time), but because I was no longer in control of my Windows experience at work.  So many things had been locked down that it was harder to manage my own networking needs, install my own software, or remove "required" bloatware that was bogging down my system.  Linux was still the wild west for my IT department, which gave me the freedom to self manage my own networking and security.

So I re-installed Ubuntu (20.04) and started solving the problems associated with disconnecting from Windows, Office, and the like.  I stick with LTS releases of Ubuntu to minimize any stability issues, and to hone in on best practices for each major release than to constantly be missing a moving target.

### Writing

I moved away from MS Office before I ever left Windows.  My least favorite part of office was the lack of collaborative editing even though the world was moving toward it.  Today, even with the Office365 web tools much better than before, I have left that style of writing as much as I can.  I now rely on three major tools, with one as my favorite for personal writing projects.

* Overleaf: I use overleaf for collaborative paper editing in latex with other researchers
* Google Docs: I use google docs for editing collaboratively with teams that don't need to use latex.
* Markdown with git: I use this almost exclusively for personal writing projects, courses, websites, presentations, and anthing else.

### Presentations

One of the big issues I had with how I developed and edited presentations was due to my use of Powerpoint.  Powerpoint files are really .zip files with all the media files included in separate folders, and some meta-data tying it all together with slide components like text boxes and graphics.  The problem though, is that even if you make a small change to the file and save it, the whole file gets re-zipped.  This is a bear to transfer to the cloud, is difficult to edit when files get larger than one or two Gbs, and creates a version-control headache, in that small changes are not recognized and thus pptx files become incompatible with git or github.  Even migrating to powerpoint's xml format did not work as the .xml file they use still uses large blobs of binary information in the xml to store data.  So instead I decided to go in the opposite direction that powerpoint headed in the early 2000's: strip the media out of the pptx, put it in a central place on my computer, strip out the text and put it somewhere else, and version-control the text so that small changes resulted in small diffs in a git repository somewhere.  

So, I made a VSBasic project for converting powerpoint slides to markdown.  I extracted all the media from each powerpoint by renaming it to a .zip and extracting the image and movie data, and then merged the two back together.

I now use pandoc to create my slides using revealjs.  I made a script to automate this process.

Managing my media, though, has become more difficult, because it's hard to tell whether any of the videos I've stored are actually used by any presentations.  Additionally, I still store the media on the cloud, but when I'm on the road I need a local copy of all images and videos.  This folder itself has grown quite large over the years -- but just imagine if I had stayed with multiple copies of the same embedded videos!  So instead, I have made a python script that compresses all the original video and pictures and dumps it locally, using ffmpeg along with some Python packages.  Encoding can be performed periodically as new videos are put in my cloud folder, and on my local machine now only stores a fraction of what the original-size videos would take up.  This is a good compromise between maintaining a high-quality original, as I need to do for maintaining continuity in my lab, and for portability and speed, which I need on my laptop.

### Cloud Storage

With the move to Ubuntu, native support for cloud services is much worse than Windows.  While dropbox supports linux, many other cloud storage providers don't, or only allow you to use the web client.  

I now use rclone to mount my cloud drives into my local filesystem, so they appear just as a normal folder in my filesystem.  Rclone is quite a handy tool for this and works across almost every cloud storage system pretty transparently

There is one exception: onedrive.  Microsoft onedrive modifies common files by re-creating the preview image and tacking it onto the original file, changing the file (and file size) whenever it syncs.  This means that normal ways of comparing two files -- hashing or file-size comparisons -- don't permit rclone to compare files.  Instead, when syncing or backing up, I have to take a two-step approach toward syncing files.  First sync all the odd files using traditional file comparison methods, then sync all the common files -- media files, office files, and the like -- ignoring the checksum and file size.

These are the file types I've found that you have to treat specially: doc,xls,docx,xlsx,pptx,jpg,html,JPG,ppt,aspx,htm,MASTER,xlsm

### git and github

I have multiple accounts in github

### VSCode
