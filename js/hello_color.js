function setup() {
    createCanvas(400,400);
    canvas.parent("hello-color-canvas")
    noCursor();
  
    colorMode(HSB, 200, 100, 100);
    rectMode(CENTER);
    noStroke();
}

function draw() {
    background(mouseY/2, 100, 100);
    fill(200-mouseY/2, 100, 100);
    rect(200, 200, mouseX+1, mouseX+1);
}