---
title: Reimagining Today's Electronics Handbook
date: 2025-06-05
summary: " "
---

> Last year I was asked to contribute to an introductory electronics handbook.  The publisher wanted my thoughts on how to refresh it, improve it, and make it current, since the original authors had moved on and didn't have time to make the necessary improvements.  Even though I didn't have time to work on it, I put together a writeup on what I thought needed to change, with a justification for why.  I thought that writeup might have some utility on its own, so here it is, adjusted for a general audience.  Consider my perspective, as someone who teaches introductory courses on mechatronics and embedded systems --  I don't have time to teach everything, so I have to pick and choose, based on what I think will serve my students best as they approach the workforce.  These thoughts are therefore already  running through my head as I consider how to update and curate my courses.

---

Back when I was in school, it was still manageable to attempt to cram everything introductory about electronics, mechatronics or embedded systems into a single handbook or textbook, running in parallel with the courses I once took, and these days teach.  The problem with these topics today is that 1) so many devices, products, and concepts have come and gone, that your materials need to be overhauled top to bottom every few years.  Additionally, the number of things to know about introductory electronics has both grown and shifted as well. I will give you a brief rundown:

## The work you have to do to enter electronics has changed

Electonics theory doesn't really change, because it's  fundamental to how more advanced electronic concepts work. You still need to know Ohm's law, Kirchoff's voltage and current rules, and your basic passive circuit elements. However, what I have observed in the past few years of teaching is that basic thru-hole components (the kind that are easy to put on a breadboard and start playing with) are getting harder to find, and that many companies have "productized" or "modularized" basic surface mount parts (ala Adafruit, Sparkfun, Mikroe) to provide easier access to more intricate systems on a chip. This is exemplified by Mikroe's "click" boards, for example. Thus, when you can fly, do you need to learn how to walk? Though I believe at the heart of a good education you must learn and practice the basics, most of us don't tear down our calculators before using them. I don't believe most students -- let alone hobbyists -- want or need to start at the beginning; they want to make their systems work *now*.

When I was learning electronics, we also used to learn about digital circuits from the bottom up, because we still needed to develop our own circuits from scratch.  Microprocessors and microcontrollers were not advanced enough to include many of the processing and mapping capabilites they do today. We thus composed logical elements from their base constituents (and,or,not,nand, etc) and used that to augment simple processing architectures. Today, though, microcontrollers and single-board-computers include much of the hardware (or offer expansion boards) that we used to have to build. This means that the focus and tone of a book written today about electronics would be about selecting a chip or chip family (or product ecosystem) that has the right features baked in, rather than designing and selecting 10 discrete parts to form your own analog signal processing circuit or digital system. The best (fastest and easiest) way to craft a system these days is in software, and to do it on whatever \$2 chip that has the right blend of on-board features.

While speaking about software, I first learned assembly language in my mechatronics courses, in order to better understand the connection between computer architectures and the software that runs on top of it.  We did because of our systems' *constraints*. The limits of memory and program space were such that we had to be innovative in how we coded our systems -- our programs had to be efficient! We sometimes sacrificed program clarity for program efficiency. These days, because the limits of memory and program space are virtually non-existent, we are able to use a variety of higher-level languages without seeing the performance hit they extract on our systems (for good and for ill). Because we are writing simple systems in higher-level languages, and because many of those low-level decisions are made for us by increasingly integrated design tools or high-quality software libraries, our focus in development these days has shifted towards paradigms that are transferrable, safe/secure, and easy to understand, rather than efficient.

The landscape of products, and ways to combine them, has also exploded. New programming languages(rust, micropython), new computing platforms (raspberry pi, esp32, psoc, etc), new components (cameras, sensors, motors, and their interfacing components) -- it is too much for one person to catalogue any more in a single "Gutenberg library" of electronics knowledge. You have to pick and choose.

Therefore, I think if you were to write a handbook or textbook today, you must be more strategic in what you spend time on. Keep the theory, but get much faster to the parts you need to know **today**.

## PCB Design and Manufacturing

Developing your own circuits has also advanced quite a bit. To affordably make your own PCBs, you once started by designing your own circuits by hand, literally drawing your own circuit on a copper-clad board and then etching away the copper. These days, you can get a \$10 board sent from overseas in a week. Thus, the discussion of tools we use to make our own boards needs to be overhauled.

* Eliminate a discussion of wire-wrap technology, the "transparency" method of designing PCBs
* Update the tools in today's electronics workbench with an eye toward affordability.  There are a lot of tools that makes yesterday's lab bench, filled with expensive meters, drivers, and tools -- less essential for those on a budget.
* Eliminate analog multimeters and oscilloscopes.  This is great for historical context, but not what we use any more!

You should introduce the dominant free and open source PCB design tools, the idea of how they work, and include a practical walkthrough.  KiCAD is my open-source tool of choice, though we have also used Altium and Cadence successfully on the industry-grade side.  It would also be useful to discuss simpler tools that exist between a full electronics design and something more hobbyist oriented, such as Fritzing or tinkercad.

It is also now possible these days to sink a small amount of money into your own PCB mill in order to develop your own PCBs within the classroom or in your garage. For the serious hobbyist, they would want to know how to do this, what the dominant machines are, and what you need to know to get it working.  Because it is so accessible and affordable these days, a discussion of PCB manufacturing would help readers take their designs through to completion by themselves, which is a powerful selling point.

## Power and Voltage Regulation

While "linear" voltage regulators (the kind still used in introductory courses) are still prevalent, switching regulators are much more energy-efficient and are preferred in industry today. The focus on linear regulators should change, since so many more switching regulators are out there, and their setup and use is simpler now (now that they are more advanced and require fewer parts).

## Discrete Digital Circuit Design

While it's cool to learn about the way digital logic forms the basis for all computing, we just don't compose digital circuits like that any more -- by composing digital circuits from individual components (740X series, anyone?). I suggest trimming it down or eliminating it.

## Analog Circuitry

Analog signal conditioning, and its associated hardware (Op Amps) are are still a good topic to learn, but it is important to recognize that there are far fewer analog interfaces in use in modern electronics than digital. Thus, while you "have to know" how analog signals are conditioned and passed along, analog data is now often quickly digitized and then massaged via digital techniques.  This should be expanded upon in beginner textbooks and curricula for early learners.  Something about digital filters, "discrete" systems, and modern computing examples should be added to todays first courses and handbooks.

## Sensing

The theory of sensing is still great to know. In class, I still teach about capacitive sensing, inductive sensing, resistive sensing, and show how to connect these basic elements to custom-designed analog signal conditioning circuits.  This is great to learn, know, and understand, and I'm on the fence whether we should throw the baby out with the bathwater, but the reality is that most actual sensors on the market today are somewhat disconnected from this theory.  Many sensor chips are in fact complete systems in their own right, with logic, multiple individual sensors, sensor fusion algorithms, programmability, etc. Your basic electronics textbook doesn't really capture the complexity of setting up and working with even the most basic digital sensors, communicating with them, or reading them. Each of these complex sensors could be a chapter or more (their datasheets can be 50 pages!)

## Motors and Actuators

Motor theory hasn't changed, but driving electronics have. Furthermore, with the prevalence today of brushless motors in applications such as robots and drones, the complexities of driving brushless motors should be added. Also missing from many textbooks is how to integrate position sensing and drivers together within a motor controller. There are many exemplar chips and dev-boards today that do this out of the box, such as simpleFOC, openbldc, odrive, dynamixel, etc.

## Low and High-level Communication

Communication is no longer separated from low-level electronics projects.  In the past, you could design a circuit without necessarily needing to network it or communicate with the outside world, but when $2 microcontrollers these days include a WiFi module, you need to also prepare your reader for communicating with the world

An in-depth discussion of low-level protocols, such as SPI, I2C, EUSART, Onewire, I3C, I2S, as well as wiring standards (RS485, etc) would help the reader prepare for terminology they will encounter when selecting compatible parts.  A discussion of high level wired and wireless standards, such as Wi-Fi, Ethernet, TCP/IP, Zigbee, Bluetooth, LoRa, would also help the reader select the appropriate  You should provide concrete examples from datasheets, and code / software for interacting in C, as well as how to find existing libraries for arduino and micropython.

## Microcontrollers

The whole world of microcontrollers has changed, with new companies, whole families of products, updated architectures, etc.  Consider microcontrollers that can run MicroPython or similar, in addition to lower-level languages like C. This satisfies a similar goal: you want to move along quickly, without delving too deep into the guts of a particular architecture, since it is likely to change.

* Arduino is still a great, introductory architecture, because it is dominant at the hobbyist level. However, whole books are written on or about Arduino microcontrollers, and depending on your audience, many high-schoolers have already seen these.
* Discuss all the things microcontrollers can now do: connect to the internet, run a web page, run full operating systems
* Discuss the many new ways microcontrollers can be programmed these days.

Furthermore, small Single Board Computers (SBC's) that run full PC operating systems (raspberry pi, beagle bone, jetson nano, NUCs) should at least be introduced.  These are a dominant competitor to microcontrollers these days, because you can program them using all the same code that runs on Linux, accessing modern and better-maintained codebases, and then do even higher-level computing and communication. You can develop faster.  For this, students should be aware of Linux, as well as the major software packages and libraries you would want to consider if going this route.

## LLMs, Generative AI, and NLP

This is an active discussion with my colleagues -- how do you introduce and teach with these tools in the classroom?  You could consider adding a short discussion of this, because the tools are already here, and engineering students or hobbyists should be prepared to use them.  Examples could include:

* Using a coding assistant to increase productivity -- we already use VSCode in my courses, thus adding co-pilot or similar might be useful.
* consider AI-based PCB design tools.  There are a few out there already.  Are they mature enough to use?

The only caveat is that this section would be outdated quickly...

## 3D Printing

This may seem out of place, but so many people design and build their own enclosures for electronics, housings for motors, etc, that it should be introduced at least. You could add some concrete examples for how to print parts that minimize complexity, take into account manufacturability, assembly, and minimize part counts. You could talk about how to simplify attachments with self-tapping screws, capture nuts, etc.
