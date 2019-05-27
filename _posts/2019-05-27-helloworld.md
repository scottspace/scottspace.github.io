---
layout: post
title: Hello world!
---
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">
Hi there!  We're importing a notebook in the div below:
<br>
<div class="my_import"></div>
<script type="module">

import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/@tmcw/hello-world.js?v=3";

const runtime = new Runtime();
const main = runtime.module(define, name => {
  if (name === "hello") {
    return new Inspector(document.querySelector("#my_import"));
  }
});

</script>
