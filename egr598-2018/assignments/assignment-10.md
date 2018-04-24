---
title: GROUP Assignment 10
subtitle: Design & Manufacturing Workflow
class_name: EGR598
bibliography: ../bibliography.bib
csl: ../ieee.csl
figure_alignment: H
---

## Overview

The purpose of this exercise is for your team to execute a full design workflow to compute the cut files for each layer of your device. The input should be a dxf file.  The output should be a set of dxf files, one for each layer of your laminate

## Detailed Procedure

1. Create a dxf file, with a separate layer for each design element, such as mountain hinges, valley hinges, body material, holes(if you want to separate these from the outer body), cut lines, etc.  If you have a multi-laminate design (more than 5 layers), you may need more layers.
1. Create a script which extracts each of these elements and creates a laminate object for each set of design elements.  for example, plot all the hinges, all the cuts, all the bodies, all the holes with separate plot commands.
1. Justify your design decisions.
    * Why have you selected your particular hinge design?
    * Why are hinges the width you have selected?  
    * other project specific decisions you made
1. Compute the manufacturing geometry including web and support, ensuring that all scrap is cuttable and/or removable
1. Test your manufacturing to ensure that:
    * no floating parts of your design exist after the first cut
    * your design is completely separated from your web.
    * the result of your manufacturing process equals your laminate robot.
<!--## Alternate method
If you choose to use popupCAD, that is fine.  Please indicate input dxf(s), along with-->
