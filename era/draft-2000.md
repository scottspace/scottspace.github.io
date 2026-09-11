# The Approximation Era

*Compute is replacing calculus. Tightened cut, 2026-09-10.*
<!-- hero-dawn-canyon.jpg doubles as the og:image / social card -->
![First sunlight breaking over a vast canyon rim and lighting ancient rock strata](/images/era/hero-dawn-canyon.jpg)
*First light on the oldest rock. The crust is learning to think.*

---

We are teaching rock to think.

Dig sand from the ground, melt it into silicon, etch a few billion switches into it, and pour sunlight through them. Do this at scale and the rock begins to finish your sentences. Keep going and it folds proteins, drives cars, designs medicine, and works a lathe. Nothing in the recipe is new physics. At the bottom of it sits one equation, 250 years old.

*y₁ = y₀ + h f(y₀)*

Euler published that line in 1768. Katherine Johnson used it to bring men home from the Moon. An engineer in Australia used it last year to cure his dog's cancer. And right now it is quietly turning the mantle of our planet into an intelligence smarter than any human who has ever lived, powered by the light that falls on it for free.

World class expertise, in any field, is becoming something you rent with two things, capital and watts. We live in the Approximation Era. In this era anyone can truly build anything, digital or physical. But we cannot build everything. This essay walks both halves of that sentence, up the ladder that makes the first half true, then out to the two walls that make the second half true. Climb with me.

## One move, six equations

In 1687, Newton and Leibniz found that one kind of sentence can describe how anything changes. Here is how the next instant depends on this one.

*dy/dt = f(y)*

That sentence is a differential equation, and it runs the universe. Drop a ball, dose a patient, price an option, spin a hurricane, and somewhere underneath, a rule of this shape is doing the work. The catch is that writing the rule is not solving it. Almost none of these equations have exact answers. The universe made a promise it would not keep.

In 1768, Euler stopped waiting and obeyed the rule in small steps. Ask which way things are heading. Step a little. Ask again. Every step is slightly wrong, yet the walk gets you home. In 1962 this line carried John Glenn around the Earth. Glenn would not fly on the computer's word alone. During the preflight checklist he asked the engineers to get the girl to check the numbers. Katherine Johnson spent a day and a half at a desk calculator re-stepping the trajectory by hand. When she said the numbers were good, he flew. Her math later helped bring Apollo home from the Moon. I tell her story in [Check the Numbers](/essays/check-the-numbers/). Hold the image. Small wrong steps, a path that lands, a person who signs.

![A coarse gold Euler polyline drifting off a smooth pale curve while a finer one hugs it](/images/era/step-curve.jpg)
*The move itself. Big steps miss. Small steps hug the truth. Compute buys smaller steps.*

In 1847, Cauchy aimed the step downhill. Feel which way is down. Step. Repeat.

*w₁ = w₀ − η ∇L*

That is gradient descent, how every neural network on Earth learns. Start out very wrong. Step downhill on your errors a few million times. The 2024 Nobel Prize in physics went to work built on this line.

In 1948, Shannon stepped through language. Guess the next word from the words that came before. He played the game by hand with a shelf of novels and coin flips. ChatGPT is the same parlor game with the whole internet, and it passes the bar exam.

In 2021, diffusion ran the walk backward. Start with pure static. Remove a little noise. Step again, and again, until a picture appears, or a protein. That is the engine inside every image generator and inside AlphaFold 3, which turned a five year thesis into a two day compute job and ran it two hundred thousand times. A million years of human work, given away. The sampler is named for Euler.

And then, in our decade, someone added one letter.

*y₁ = y₀ + h f(y₀, a₀)*

The a is the action taken. With it the step becomes a policy. The machine no longer predicts what the world will do. It learns what the world will do if it acts. Watch the seed. A team at Google wired a joystick into a video model. Up, down, left, right, fire. Three bits per second of human intent. The model learned to guess the next frame and the next button press together, and a playable world appeared, frame by frame, obeying physics it had absorbed. Today's robot models are that seed grown into a tree. Perception, instruction and motion in one network, driving real arms and real tools. One added letter, 258 years apart.

![Euler 1768 beside the vision language action equation, one added term in gold](/images/era/equation-diff.png)
*One added letter, 258 years apart.*

Six equations. One move. A trajectory, a minimum, a sentence, a picture, a consequence. None of the six authors knew they were building the same machine.

## Why the step works

Approximation should be impossible. Learning a rule with a billion moving parts should take more examples than there are atoms. It works because the universe cooperates in three ways. The rules are low dimensional. Energy is mass times c squared, not mass to the hundredth power. The rules are local. You can reason about Palo Alto without consulting a butterfly in Japan. And the rules compose. Nucleotides stack into DNA, cells into organs, parts into cars. A galaxy, a hurricane and a seashell draw the same spiral. The universe reuses its functions the way a good engineer reuses code. This is why a network trained on films learns physics nobody taught it, and why machinery that sorts cat memes from dog memes can be turned on tumors. Katherine was not cheating. She was collecting on a promise the cosmos had already made. So is every model in production today.

![A galaxy, a hurricane, and a nautilus joined by one golden spiral line](/images/era/three-spirals.jpg)
*A galaxy, a hurricane, a seashell. One spiral. The universe reuses its functions.*

## Two walls

You know a claim is an era and not a hype cycle when it has edges. This one has exactly two.

Chaos caps prediction. Lorenz proved in 1963 that no model, however perfect, can step one true path through a month of weather. Tiny errors compound until the forecast is fiction. The equations are fine. The universe simply refuses to hold still. So the era changed what it promises. Step a thousand walks from the same present and let them fan out. The shape of the fan holds more knowledge than any one line through it. Ensembles built this way now beat the best physical forecasts on Earth. We predict a set of paths, not one.

![A fan of gold paths spreading from a single bright point, one silver path running through them](/images/era/chaos-fan.jpg)
*From one present, a fan of futures. We predict the set, not the path.*

Quantum ends observation. Every rung on the ladder rests on one hidden assumption. Looking is free. We observe the world and the world does not notice. At the bottom of physics the assumption dies. You cannot copy an unknown quantum state. Measuring it changes the answer. There is no dataset behind that veil. Machines that learn behind it are just now being built, and one with quantum memory already learns some things exponentially faster than any classical observer. That is not this era. The era ends at that wall. The next one starts behind it, standing on this one the way Katherine stood on Euler.

![A gold dilution refrigerator glowing in a dark lab](/images/era/quantum-chandelier.jpg)
*The machine behind the veil.*

## Anything, not everything

Inside those walls, the recipe for building has gone general. It has three ingredients. A model, capital, and watts.

An AI engineer in Australia ran the recipe when his dog was dying of cancer. He sequenced the dog. He sequenced the tumor. A model designed the molecule that teaches an immune system that exact face, and he had it made. The dog is in remission. Sit with that. The same machinery that learned to tell cat from dog just designed medicine for the dog. The same play is in human trials for HER2 positive cancer right now.

![A golden retriever standing on a dock at sunrise](/images/era/dog-morning.jpg)
*In remission. The ladder reaches all the way to the dog.*

Notice what the recipe leaves out. Expertise. For all of history the limiting ingredient was a trained mind and the decades it took to make one. It now rents by the token. A dossier that took a team three months, a protein that took a thesis, a diagnosis that took a residency, each becoming a line item on a compute bill. I have counted more than 9,000 verified deployments across public markets, and they cluster where trained minds were scarcest. Knowledge stopped being the bottleneck.

Energy is. Run the arithmetic. Serve an AGI on an eight way GPU box and give one to every person and every working robot on Earth. Two billion boxes draw about ten terawatts. The planet generates about ten. The sun pours ten thousand times that onto our rooftops and deserts, so the ceiling is not physics, just collectors and wires. Tokens and watts are the currency of the next twenty years. Anyone holding both can build anything, digital or physical, and be world class doing it. The planet has the watts for anything. It does not have the watts for everything.

![Transmission towers at dusk above a valley with a glowing data center](/images/era/grid-night.jpg)
*Tokens and watts, the currency of the next twenty years.*

## Heart

So the last scarce thing is the choice.

A machine can weigh a thousand options and happily pick one. It cannot answer for the pick. No family, no name, nothing to lose. A choice that costs nothing carries no weight. Glenn had the fastest computer on Earth and still asked for Katherine.

When anyone can do anything, life is more about heart.

The machine hands out the trades and the titles at the door. What it cannot hand out is a reason. What expertise will you make your own? Where will you spend your capital, your effort, your watts?

![A parent and child holding hands at the rim of a sunlit canyon at dawn](/images/era/heart-rim.jpg)
*The reason.*

Katherine had a pencil, one old equation, and a reason. It carried men to the Moon and home again. You have the same equation running a trillion times faster, rock that thinks, and a sun that pays for it. For the first time in history, what you can build is not limited by what you know.

Only by what you love.

The light is already on the rock. Go build what your heart has been waiting for.
