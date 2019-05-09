# breakout
# originally from 
# https://gist.github.com/Milhound/67f59113ab3ac6b21421cb799df4a5ce#file-breakout-coffee

paused = false

# Canvas
cW = 400
cH = 400
#cW = 850
#cH = 600

# Player
pW = 60
pH = 10
pSpeed = 15
pScore = 0
pLives = 3
pX = cW / 2 - pW / 2
pY = cH - pH - 7

# Ball
bD = 3
bSpeed = 7
bIncrease = 0.8
bX = cW / 2 - bD / 2
bY = cH - pH - bD / 2 - 10
if Math.round(Math.random()) == 0
    bVX = -Math.random() * 7
else
    bVX = Math.random() * 7
bVY = -7

# Enemy
eW = cW / 10
eH = eW / 2
enemies = {}
saturation = 200
rowCount = 6

generateEnemy = (rows) ->
    x = 0
    i = 0
    while x < rows
        while i < 10 + x * 10
            enemies[i] = {
                "location": [],
                "living": true,
                "color": []
            }
            enemies[i].location[0] = (i - x * 10) * eW
            enemies[i].location[1] = cH / 2 - x * eH
            r = Math.floor(Math.random() * 256)
            g = Math.floor(Math.random() * 256)
            b = Math.floor(Math.random() * 256)
            enemies[i].color[0] = r
            enemies[i].color[1] = g
            enemies[i].color[2] = b
            enemies[i].color[3] = saturation
            i++
        x++

setup = ->
    generateEnemy(rowCount)
    const canvas = createCanvas(cW, cH)
    canvas.parent('breakout-canvas')
    frameRate(30)
    
draw = ->
    background(80)
    player()
    score()
    enemy()
    ball()
    collision()
    if pLives == 0
        reset()
    if pScore == Object.keys(enemies).length
        win()

player = ->
    fill(255)
    rect(pX, pY, pW, pH)
    if keyIsDown(LEFT_ARROW)
        pX = max(pX - pSpeed, 0)
    if keyIsDown(RIGHT_ARROW)
        pX = min(pX + pSpeed, cW - pW - 1)
score = ->
    textSize(30)
    text("Score: " + pScore, cW - cW * 0.20, cH * 0.1)
    text("Lives: " + pLives, cW * 0.05, cH * 0.1)

enemy = ->
    for key of enemies
        if enemies[key].living == true
            fill(enemies[key].color[0], enemies[key].color[1], enemies[key].color[2], enemies[key].color[3])
            rect(enemies[key].location[0], enemies[key].location[1], eW, eH)

ball = ->
    fill(255)
    ellipse(bX, bY, bD, bD)
    bX = constrain(bX + bVX, bD / 2, cW - bD / 2)
    bY = constrain(bY + bVY, bD / 2, cH - bD / 2)
    
collision = ->
    # Bottom Contact
    if bY == cH - bD / 2
        bX = pX + pW / 2 - bD / 2
        bY = cH - pH - bD / 2 - 10
        bVY = -7
        pLives--
    # Canvas Top Contact
    if bY == bD / 2
        bVY = -bVY
    # Canvas Side Contact
    if bX == bD / 2 or bX == cW - bD / 2
        bVX = -bVX
    # Contact with Enemy box
    for key of enemies
        if enemies[key].living
            # Side of eBox
            if bY < enemies[key].location[1] + eH and bY > enemies[key].location[1]
                if bX > enemies[key].location[0] and bX < enemies[key].location[0] + eW
                    bVX = -bVX
                    enemies[key].living = false
                    pScore++
            # Bottom of Box
            if bY < enemies[key].location[1] + eH + bD / 2 and bY > enemies[key].location[1] + eH
                if bX > enemies[key].location[0] and bX < enemies[key].location[0] + eW
                    bVY = -bVY
                    enemies[key].living = false
                    pScore++
            # Top of Box
            if bY > enemies[key].location[1] - bD / 2 && bY < enemies[key].location[1]
                if bX > enemies[key].location[0] and bX < enemies[key].location[0] + eW
                    bVY = -bVY
                    enemies[key].living = false
                    pScore++
                                    

    # Contact with Player
    if bX > pX and bX < pX + pW
        if bY > pY - bD / 2 - 2
            bY = cH - pH - bD - 2
            bVY = -abs(bVY + bIncrease)
            # Right Half
            if bX > pX + pW / 2
                if bX > pX + pW * 0.9
                    bVX = 7
                else if bX > pX + pW * 0.8
                    bVX = 6
                else if bX > pX + pW * 0.7
                    bVX = 4
                else if bX > pX + pW * 0.6
                    bVX = 3
                else
                    bVX = 2
            # Left Half
            if bX < pX + pW / 2
                if bX < pX + pW * 0.1
                    bVX = -7
                else if bX < pX + pW * 0.2
                    bVX = -6
                else if bX < pX + pW * 0.3
                    bVX = -4
                else if bX < pX + pW * 0.4
                    bVX = -3
                else
                    bVX = -2
                

keyTyped = ->
    if key == 'p'
        paused = !paused
        if paused
            console.log('Paused the game')
            noLoop()
        else
            console.log('Unpaused the game')
            `loop()`
    if key == ' ' && pScore == Object.keys(enemies).length
        reset()
        `loop()`
reset = ->
    # Player
    pScore = 0
    pLives = 3
    pX = cW / 2 - pW / 2
    pY = cH - pH - 7

    # Ball
    bX = cW / 2 - bD / 2
    bY = cH - pH - bD / 2 - 10
    if Math.round(Math.random()) == 0
        bVX = -Math.random() * 7
    else
        bVX = Math.random() * 7
    bVY = -7
    generateEnemy(rowCount)
win = ->
    noLoop()
    background(255)
    fill(0)
    text("YOU WIN!", cW / 2, cH / 2)
