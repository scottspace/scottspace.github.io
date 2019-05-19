// breakout
// originally from 
// https://gist.github.com/Milhound/67f59113ab3ac6b21421cb799df4a5ce#file-breakout-coffee
// y, g, o, r

var paused = false;

// Canvas
var cW = 400;
var cH = 400;

// Player
var pW = 40;
var pH = 10; 
var pSpeed = 15;
var pScore = 0;
var pLives = 3;
var pX = cW / 2 - pW / 2;
var pY = cH - pH - 7;

// Ball
var bD = 10;
var bSpeed = 7;
var bIncrease = 0.8;
var bX = cW / 2 - bD / 2;
var bY = cH - pH - bD / 2 - 10;
var bvX;
if (Math.round(Math.random()) == 0) {
    bVX = -Math.random() * 7; 
}
else {
    (bVX = Math.random() * 7);
}
var bVY = -7;

// Enemy
var eW = cW / 10;
var eH = eW / 2;
var enemies = {};
var saturation = 200;
var rowCount = 6;
var bBlue = [51, 153, 255];
var bGreen = [51, 255, 51];
var bYellow = [255, 255, 51];
var bOrange = [255, 178, 102];
var bOrange2 = [255, 128, 0];
var bRed = [255, 102, 102];
var bSounds = ['1C','16','12','10','0C','0A'];
var bFreq = [2093, 1046, 698, 523, 415, 349, 293,
             261, 233, 207, 185, 174, 164, 146, 138, 
             130, 123, 116, 110, 103, 98, 98, 93, 
             87, 82, 82, 77, 73, 73, 69, 69, 65];
             
var bColors = [bBlue, bGreen, bYellow, bOrange, bOrange2, bRed];

function generateEnemy(rows) {
    var x = 0;
    var i = 0;
    while (x < rows) {
	var xSound = bFreq[parseInt(bSounds[x],16)];
        while (i < 10 + x * 10) {
            enemies[i] = {
                "location": [],
                "living": true,
                "color": []
            };
            enemies[i].location[0] = (i - x * 10) * eW;
            enemies[i].location[1] = cH / 2 - x * eH;
            colr = bColors[x];
            r = colr[0];
            g = colr[1];
            b = colr[2];
            enemies[i].color[0] = r;
            enemies[i].color[1] = g;
            enemies[i].color[2] = b;
            enemies[i].sound = xSound;
            enemies[i].color[3] = 220; //saturation;
            i++;
	}
        x++;
    }
}

function setup() {
    generateEnemy(rowCount);
    var canvas = createCanvas(cW, cH);
    canvas.parent('breakout-canvas');
    frameRate(30);
}
    
function draw() {
    background(80);
    player();
    score();
    enemy();
    ball();
    collision();
    if (pLives == 0) {
        reset();
    }
    if (pScore == Object.keys(enemies).length) {
        win();
    }
}
    
function player() {
    fill(bOrange2);
    rect(pX, pY, pW, pH);
    if (keyIsDown(LEFT_ARROW)) {
        pX = max(pX - pSpeed, 0);
    }
    if (keyIsDown(RIGHT_ARROW)) {
        pX = min(pX + pSpeed, cW - pW - 1);
    }
}

function score() {
    textSize(16);
    fill(255);
    text("Score: " + pScore, cW - cW * 0.20, cH * 0.1);
    text("Lives: " + pLives, cW * 0.05, cH * 0.1);
}

function enemy() {
    for (var key in enemies) {
        if (enemies[key].living == true) {
            var ecol = enemies[key].color;
            fill(ecol[0], ecol[1], ecol[2]);
	    stroke(ecol[0], ecol[1], ecol[2]);
            rect(enemies[key].location[0], enemies[key].location[1], eW, eH);
	    stroke(0);
	}
    }
}

function ball() {
    fill(bOrange);
    rect(bX,bY, bD, bD);
    // ellipse(bX, bY, bD, bD);
    bX = constrain(bX + bVX, bD / 2, cW - bD / 2);
    bY = constrain(bY + bVY, bD / 2, cH - bD / 2);
}
    
function collision() {
    // Bottom Contact
    var sX = 1;
    var sY = 1;
    if (bY == cH - bD / 2) {
        bX = pX + pW / 2 - bD / 2;
	bY = cH - pH - bD / 2 - 10;
        bVY = -7;
        pLives--;
    }

    // Canvas Top Contact
    if (bY == bD / 2) {
        sY = -1;
    }

    // Canvas Side Contact
    if (bX == bD / 2 || bX == cW - bD / 2) {
        sX = -1;
    }
    
    // Contact with Enemy box
    for (var key in enemies) {
        if (enemies[key].living) {
            // Side of eBox
            if (bY < enemies[key].location[1] + eH && bY > enemies[key].location[1]) {
                if (bX > enemies[key].location[0] && bX < enemies[key].location[0] + eW) {
                    sX = -1;
		    sY = -1;
                    enemies[key].living = false;
                    pScore++;
		}
	    }
            // Bottom of Box
            if (bY < enemies[key].location[1] + eH + bD / 2 && bY > enemies[key].location[1] + eH) {
                if (bX > enemies[key].location[0] && bX < enemies[key].location[0] + eW) {
                    sY = -1;
                    enemies[key].living = false;
                    pScore++;
		}
	    }
            // Top of Box
            if (bY > enemies[key].location[1] - bD / 2 && bY < enemies[key].location[1]) {
                if (bX > enemies[key].location[0] && bX < enemies[key].location[0] + eW) {
		    console.log("Top collision! ",key);
                    sY = -1;
		    sX = -1;
                    enemies[key].living = false;
                    pScore++;
		}
	    }
	}
    }   
  
    if (sY != 1 || sX != 1) {
	bVY = sY*bVY;
	bVX = sX*bVX;
    }

