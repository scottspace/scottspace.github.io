---
layout: post
title: Observable Breakout!
---
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">
  <style>
       .outer {
        margin: 0;
        font-family: 'Press Start 2P', cursive;
        line-height: 1.8;
        align-items: center;
        top: 0; left: 0; right: 0; bottom: 0;
      }
      .wrapper {
        text-align: center;
        margin:  auto;
      }
      #game {
        min-height: 350px;
        margin: 10px auto 40px;
      }
      .left {
        float: left;
      }
      .right {
        float: right;
      }
      .score {
        overflow: hidden;
        margin: 15px auto 0;
        font-size: 14px;
        max-width: 700px;
      }
      #newgame input {
        color: #fff;
        background: #000;
        cursor: pointer;
        border: 2px solid #fff;
        border-radius: 10px;
        padding: 10px 15px;
        font: 15px 'Press Start 2P', cursive;
        outline: none;
      }
      .explanation {
        margin: 40px auto;
        font-size: 12px;
        text-align: left;
        max-width: 550px;
      }
    </style>
<br>
<div class="outer">
<div class="wrapper">
 <div class="score">
 <div class="left">Score: <span id="score"></span></div>
 <div class="right">High Score: <span id="highscore"></span></div>
</div>
<div id="game"></div>
<div id="newgame"></div>
<div class="explanation">
 This is a simple demonstration of <a href="https://beta.observablehq.com/@jashkenas/downloading-and-embedding-notebooks">embedding
 Observable notebooks</a>. It pulls the game code live from the <a href="https://beta.observablehq.com/@jashkenas/breakout">original
 notebook source</a>.
 </div>
</div>
</div>
 <script type="module">
      import {Runtime} from "https://unpkg.com/@observablehq/runtime@4/dist/runtime.js";
      import notebook from "https://api.observablehq.com/@jashkenas/breakout.js?v=3";
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
</script>
