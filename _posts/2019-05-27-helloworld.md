---
layout: post
title: ObervableHQ Breakout
thumb: /img/o_breakout.png
---
This is a simple demonstration of

<a href="https://beta.observablehq.com/@jashkenas/downloading-and-embedding-notebooks">embedding
Observable notebooks</a>.
It pulls the game code live from the <a href="https://observablehq.com/@scottp/breakout">original
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
