---
layout: post
title: ObervableHQ Breakout
thumb: /img/o_breakout.png
---
Here's a demonstration of what Mike Bostock calls
<a href="https://beta.observablehq.com/@jashkenas/downloading-and-embedding-notebooks">embeddable
Observable notebooks</a>. Game code is pulled live from a larger, more comprehensive notebook
seen here with the <a href="https://observablehq.com/@scottp/breakout">original
notebook source</a>.

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="/css/helloworld.css">
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">

<div class="outer">
<div class="wrapper">
 <div class="score">
 <div class="left">Score: <span id="score"></span></div>
 <div class="right">High Score: <span id="highscore"></span></div>
</div>
<div id="game"></div>
<div id="newgame"></div>
</div>
</div>
 <script type="module">
      import {Runtime} from "https://unpkg.com/@observablehq/runtime@4/dist/runtime.js";
      import notebook from "https://api.observablehq.com/@scottp/breakout.js?v=3";
      const renders = {
        "viewof c": "#game",
        "score": "#score",
        "highscore": "#highscore",
        "viewof newgame": "#newgame"
      };
      function render(_node, value) {
        if (!(value instanceof Element)) {
          const el = document.createElement("span");
          el.innerHTML = value;
          value = el;
        }
        if (_node.firstChild !== value) {
          if (_node.firstChild) {
            while (_node.lastChild !== _node.firstChild) _node.removeChild(_node.lastChild);
            _node.replaceChild(value, _node.firstChild);
          } else {
            _node.appendChild(value);
          }
        }
      }
      const runtime = new Runtime();
      const main = runtime.module(notebook, name => {
        const selector = renders[name];
        if (selector) {
          return {fulfilled: (value) => render(document.querySelector(selector), value)}
        } else {
          return true;
        }
      });
      
      // work on mobile, too
      main.redefine("w", 400);
      main.redefine("paddleLength", 60);
</script>

Wait. That's so random, Scott, why is a game stuck on your site about AI?

Well, I've been toying with the idea of putting live code on this website of mine, so that
people can not only watch videos, but perhaps play with AIs as they mature.

Mike ([@bostock](https://twitter.com/mbostock))
created a beautiful library in [D3](https://d3js.org/) for visualizing data with javascript.  He
later built a community for sharing these visualizations as code [blocks](https://bl.ocks.org/),
which has since matured into entire
JavaScript notebooks.

What I particularly like about Mike's latest work is that he's addressed two of the screwy
problems with notebooks today.

First, we have the "broken state" problem.  Notebook users
can change the value of data variables in one cell, which are not shown in other cells.  Spreadsheets
don't do that, as they propagate changes in one cell to another.  Mike's "Observerable" notebooks
actually create dataflow graphs (common in compiled languages).  From there, his notebooks use
these dataflow graphs to propagate changes from one cell to all others.  I think that's so cool!

A second problem is sharing individual cells of a notebook.  In Observable, every cell can be exported
as a standalone, reactive javascript application for inclusion inside websites.  I wanted to give
that a go.

Given that my interest in deep learning was first spawned by Demis' work on Atari, I thought it'd be
fun to try and include an Atari simulator from an Observable notebook as a cell on my own feed.  After
a bit of tinkering I got it to work.

Now... what will I do with his newfound magic?  Thinking a lot about that these days.
