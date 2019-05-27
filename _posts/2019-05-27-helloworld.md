---
layout: post
title: Hello world!
---
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">
Hi there!  We're importing a notebook in the div below:
<br>
<div id="clip" style="border:1px solid #ccc; margin: 20px;"></div>
<script type="module">

import notebook from "https://api.observablehq.com/@jashkenas/breakout.js?v=3"
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
/* import notebook from "https://api.observablehq.com/@tmcw/hello-world.js?v=3"; */

new Runtime().module(notebook, Inspector.into(document.querySelector("#clip")));

</script>
