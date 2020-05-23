---
---

# MWS ENVS992 Project Report

This package contains a template for the MWS 992 project reports. These reports are required as the main deliverable for your project.

## Instructions

Your final project report is to be written in the Markdown language. This is a modern, simple type-setting language that can be used to generate documents in a variety of formats. This is superior to Word Processor software for a number of reasons:

1. The reports are lightweight (smaller files) and more stable that typically is the case with large Word documents

2. The reports can easily be reformatted into websites or Word Documents or PDFs, without you having to do any extra work.

3. The output is more consistent and higher quality than typical Word processor software is able to produce. 

You must install the software, following the directions below. Then you must download the repository where the template is stored. The template also contains instructions of what is required in the various different files. Please read this carefully, and talking to your partner/advisor or the Program Director if it is not clear. Finally you must edit the `.md` files to add your content. You will also add figures in the folder `figures`.

Read the sections below for more detailed instructions.


## Markdown

The reports are to be written in markdown language. This is a relatively simple language for creating html files, but can also be used to create a number of different document formats, including docx and pdf. To learn the language, [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is a cheat sheet, and [here](https://www.markdowntutorial.com) is a 10 minute tutorial. In case you want to add equations, these are added in LaTeX format, in between `$$` symbols, e.g. `$$\pi=3.14159$$` appears as

$$\pi=314159$$

[Here](https://davidhamann.de/2017/06/12/latex-cheat-sheet/) is a cheat sheet of LaTeX symbols and equations.

You should not need anything more than these resources above to produce all the content you will need on your website.

## The atom editor

To edit Markdown, we will use the [atom](http://atom.io) text edtior. Download and install this free software. Open atom and find preferences, find "install packages" and then you will need to add two packages: `language-markdown` and `markdown-preview-plus`. [Here is a video](https://youtu.be/djkes2a_rxI) demonstrating how to do this.

**Figures**: One quirk to pay attention to is adding figures. You can include a figure in your document with the command `![](FigureName.png)`. This works for png and jpg files and you should be able to save any figure you create (e.g. a graph, diagram or photo) into one of those formats. If you have control over the resolution, 300 dpi is recommended, and try to keep photos to < 1 Mb. The problem with this, is that the size of the figure in the final document is unpredictable. To fix the size of the figure you should add figures with the following syntax: `![](FigureName.md){ width=100% }`. You can adjust the width by changing 100% (100% fills the page width). This will not display correctly in atom, but it will work when I compile your documents for your website.

## Downloading the template and creating your report

The procedure is described in these two vidoes: [Part 1](https://youtu.be/2QEhr2t_8DU) and [Part 2](https://youtu.be/5mDQG37GFc4).

Step one is to obtain the template from the repository here: [https://git.cs.usask.ca/ani378/mws_992_report](https://git.cs.usask.ca/ani378/mws_992_report). Download as a zip file, extract this and move the folder to somewhere sensible on your computer. 

The next step is to edit the home page, whihc is called `home.md`. Here you will add your project details. You will also edit here the contents of your website, removing (and possibly adding) particular pages. Note, you include all the non-optional pages, and perhaps 1 - 3 of the optional pages, depending on your project.

You will add figures to the folder figures, and edit all the `.md` files. You will not be able to compile your entire website (unless you do the advanced steps below, but not recommended). For your information, the basic website will look like [this](http://homepage.usask.ca/~ani378/MWS_demo/home.html). If you send me your zipped folder, I can compile this for your and let you see your compiled website. 

## Pandoc: Advanced optional software

To convert the Markdown files into html, docx and pdf requires the installation of a somewhat more complicated piece of software called "pandoc". This will be run automatically for you when youre report is submitted, and your website will be automatically created, so you don't need to worry about this. However, if you are curious, you are welcome to install this if you wish to. To convert a Markdown file to html using pandoc you must install pandoc on your computer, navigate to your working folder on the commandline, and then issue the command

```bash
pandoc -s --mathjax -o doc.html doc.md
```

where `doc.md` is the name of your markdown file and `doc.html` is the name of the html file that is produced. If you run that for every Markdown file in the folder, you will have created your entire website.
