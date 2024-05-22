---
title: Incredible Feats of Productivity
date: 2024-05-22
---

## Intro

I don’t know if it’s the ever-increasing volume of bad news I’m getting from my tech podcasts, the impending AI apocalypse, or perhaps myself atrophying a bit and sticking with what I know, but if I hadn’t already switched to Linux, the news that operating systems were baking in surveillance [^1] certainly would have accelerated my shift.  So I thought I’d discuss how I switched to Linux and why, but start with the tools I use to get things done in Linux, such as tools for writing, and how I de-linked myself from any one productivity suite.

## Office / Productivity

Let's get one thing straight.  I get distracted by editing tools.  Instead of _writing_, I tweak, I bold, I fix my style sheets, I twiddle photos around.  Thus, for me, markdown is a great alternative that keeps me focused.  Why?  Because markdown permits me to focus more on writing and less on presentation.  For an academic, it's similar to what latex is supposed to be like _in theory_, but _in practice_ it gets me even closer.  With the right tools, though, markdown is portable across different domains -- html, latex/pdf, docx, pptx -- I can use markdown as my base and output it to whatever I want.

There are a couple critical markdown tools that make this possible.  The first is [pandoc](https://pandoc.org/).  Pandoc is a file converter that allows me to convert any document to any document type like powerpoint, pdf, latex, and markdown.

I wrote a couple pieces of software to make using pandoc easier.  First, I wrote a [script in Visual Basic](https://www.danaukes.com/code/powerpoint-to-markdown/) that extracts all the images and converts all my powerpoints to markdown, and allows me to unlink all my embedded videos.  I have also created a package for applying pre-made templates for course syllabi, letters, and plain documents styled the way I like them, called [pandoc-plus](https://www.danaukes.com/code/pandoc-plus/).  It theoretically works across windows and linux, and I started this path much earlier than my switch to Linux.

For slides I use pandoc with the revealjs library to generate simple, styled html pages that click through just like a powerpoint file.  I tweaked my pandoc-plus script for slides and put it in the [same project.](https://www.danaukes.com/code/pandoc-plus/)

Extracting videos from my powerpoints was a tricky step; I have since collected all the previously embedded videos into a single folder and make a compressed copy of each one that I store locally on my machine.  This permits me to take all my media with me, but retain the higher quality original in fewer places.  I now just embed ```<video>``` elements in my markdown as needed.  Critical to this step was a couple of command-line scripts added to cut and compress segments of videos for embedding into my powerpoints a little easier than FFMPEG alone.  I grouped all these tools [here](https://github.com/danb0b/code_media_tools/tree/master/python/media_tools), alongside tools for extracting images from pdf, generating image/video galleries, etc...all in service of enhancing my ability to work with my own media outside of any one productivity suite.

### But what about collaboration?

I still use overleaf, google docs, libre office or office365 online when I need to.  I also have a [windows virtual machine](https://www.danaukes.com/tags/virtualbox) with office loaded so I can ensure the formatting matches what I need it to catch the trickiest corner cases.

### What about CAD?

I don't use Solidworks or Autodesk Fusion360 daily, weekly, or monthly.  If I did, it would be much harder.  As it is, I just use them in a [virtual machine](https://www.danaukes.com/tags/virtualbox) as needed.

## You make a lot of websites.  How do you code those up?

Again, I use [markdown](https://www.danaukes.com/tags/markdown/), with two strategies for generating static html.  Why static site generators?  Because I don't need interactivity, and interactivity requires more from a hosting provider.  Without host-side interactivity, I can use github to serve my html pages.  

For cases where I want/need to control the styling or theme of the page completely, I use [Hugo](https://www.danaukes.com/tags/hugo/) alongside heavily-edited themes I've found in the community.  Hugo is much faster than Jekyll, a more-well-known alternative, which I used to use, and also, helps keep your content separate from your code.  This is better for text portability across different domains, and the markdown requires little editing in the transition.

Alternatively, I also am a big fan of [mkdocs](https://www.danaukes.com/tags/mkdocs) with the material theme.  This is for cases, like classes, where I don't care about the style as about the ease of managing the site.  This approach has saved me weeks of time over Hugo

## WHY, WHY MARKDOWN?

Because, at the end of my day, mixing text, images, and video together created an unmanageable mess that kept growing in scope and size.  By linking images, video, and text back to their source, I have been able to move towards _fewer files_ that I edit iteratively, and store the text in git repositories.  Thus, I get the benefit of seeing the entire history of my files, without the reliance on the cloud or the bloat of keeping every old version of my files.

> What about the unmanageable mess of having file links decay and have to be maintained?

Well, at least I can search across all my markdown files in a fraction of the time and fix links globally using simple find/replace.

### What editor do you use to write markdown in?

VSCode with a number of additional extensions.  Why? Because I can also use VSCode for Python, latex, Jupyter, and other text-based editing tasks. It's a good-enough one stop shop.  I really liked obsidian, too, but that would be better for me if I only was working with markdown.

## How did you get your files out of the cloud?

TL/DR: It was easy since google made me do it anyways[^2].  

I used [Rclone](https://rclone.org/) to download and convert google docs to .docx, .pptx, and other office files.  Then I used my ppt converter and/or pandoc-plus to do an initial pass at converting them to markdown.

Rclone is a great tool for syncing files across cloud providers.  It's great for syncing files locally at the command line, and it also has a "mount" option that permits it to behave like a new drive or mounted folder in your filesystem, as an alternative to using each cloud provider's native app.  

## Conclusion

This is an incredibly short summary of _**YEARS**_ of development work that permitted me to extricate my own files and simplify my approach towards writing.  While the tools I developed helped me, they are not written for _you_, and are not general purpose, with little documentation in some cases.  

It would also have been better to start with this approach.  Half of the tools I wrote were to facilitate a one-time conversion, and don't really have a purpose in my day-to-day any more.

[^1]: [ARS Technica: New Windows AI feature records everything you’ve done on your PC](https://arstechnica.com/gadgets/2024/05/microsofts-new-recall-feature-will-record-everything-you-do-on-your-pc/)

[^2]: [The Register: The end of free Google storage for education](https://www.theregister.com/2022/02/14/google_free_storage_plan_ends_opinion_column/)
