# The Approximation Era

*Compute is replacing calculus. Draft rewrite v2 with imagery, 2026-08-23.*
<!-- equation-diff.png doubles as the og:image / social card -->
![Euler 1768 beside the vision language action equation, one added term in gold](/images/era/equation-diff.png)
*One added letter, 258 years apart.*


---

Take the equation Euler published in 1768.

*y₁ = y₀ + h f(y₀)*

Add one letter.

*y₁ = y₀ + h f(y₀, a₀)*

The first line brought John Glenn home from orbit. The second is the equation behind every robot now learning to work in the physical world. One added letter, 258 years apart. That edit is the story of our time.

Here is my claim. We live in the Approximation Era. When we cannot solve nature's equations, we step them. That move is 250 years old, and we have now written it six ways. The first five let machines understand and create anything we can observe. The sixth lets them act. Because compute keeps getting cheaper, the step is becoming nearly free, and every discipline that once waited on a derivation is becoming computable through observation instead. This is not a tech trend. It is a phase change, and it has visible edges. Climb the ladder with me and make up your own mind.

## One move, six equations

In 1687, Newton and Leibniz found that you can describe how anything changes with one kind of sentence. Here is how the next instant depends on this one.

*dy/dt = f(y)*

That sentence is a differential equation, and it runs the universe. The catch is that writing the rule is not the same as solving it. Almost none of these equations have exact answers. The universe made a promise it would not keep.

In 1768, Euler stopped waiting for the answer and started obeying the rule in small steps. Stand where you are. Ask the rule which way things are heading. Step a tiny bit that way. Ask again. Every step is slightly wrong. The walk still gets you home. In 1962 a woman named Katherine Johnson used exactly this line to bring John Glenn down from orbit. Glenn would not fly on the computer's word alone, so during the preflight checklist he asked the engineers to get the girl to check the numbers. She reran the machine's trajectory at her desk calculator for a day and a half, and he made his condition plain. If she says they're good, I'm ready to go. I wrote that story in Check the Numbers. Hold the image. Small wrong steps, a path that lands, a person who signs.

![A mechanical desk calculator under a single warm lamp](/images/era/desk-calculator.jpg)
*A day and a half at a desk calculator, checking the fastest computer on Earth.*

In 1847, Cauchy aimed the step downhill. Feel which way is down. Step. Repeat.

*w₁ = w₀ − η ∇L*

That is gradient descent, and it is how every neural network on Earth learns today. Start out very wrong. Step downhill on your errors a few million times. Become a little less wrong each time. The 2024 Nobel Prize in physics went to work built on this line.

In 1948, Shannon stepped through language. Guess the next word from the words that came before.

*p(next word | the words so far)*

He played the game by hand with a shelf of novels and coin flips. ChatGPT is the same parlor game with the whole internet, and it passes the bar exam.

In 2021, Song and colleagues ran the step backward. Start with pure static. Remove a little noise. Step again, and again, until a picture appears, or a protein. That is diffusion, the engine inside image generators and AlphaFold 3, which turned a five year PhD thesis into a two day compute job and ran it for two hundred thousand proteins. Roughly a million years of human work, published and given away. The sampler inside these tools is literally named for Euler.

And now the sixth rung, the diff you saw at the top. Vision language action models add one term to Euler's line, the action taken, and the step becomes a policy. The machine no longer just predicts what the world will do. It learns what the world will do if it acts. Watch the seed of it. A team at Google took a video model and wired in a joystick. Up, down, left, right, fire. Three bits per second of human intent. The model learned to guess the next frame and the next button press together, and a playable world appeared, imagined frame by frame, consistent with the physics it had absorbed. Three bits of control conjured a world. Today's robot models are that seed grown into a tree, perception, instruction, and motion in one network, driving real arms and real tools.

Six equations. One move. A trajectory, a minimum, a sentence, a picture, a consequence. None of the six authors knew they were building the same machine. You can object that this is hindsight, six strangers pattern matched into one story. Fair. The test of a retrofit is whether it predicts anything. So I count.

![A coarse gold Euler polyline drifting off a smooth pale curve while a finer one hugs it](/images/era/step-curve.jpg)
*The move itself. Big steps miss. Small steps hug the truth. Compute buys smaller steps.*

## The evidence

An AI engineer in Australia ran the whole ladder when his dog was dying of cancer. He sequenced the dog's DNA. He sequenced the tumor. He found the difference, used a model to design the molecule that teaches an immune system that exact face, and had it made. The dog is in remission. Sit with that sentence. The same machinery that learns to tell cat from dog now designs medicine for the dog. The same play is in human trials for HER2 positive cancer right now.

![A golden retriever standing on a dock at sunrise](/images/era/dog-morning.jpg)
*In remission. The ladder reaches all the way to the dog.*

My scanner exists to count how often that kind of story is actually happening in the economy. It reads every earnings call and SEC filing across the S&P 500, the MidCap 400, the SmallCap 600, the Russell 2000, and the major international indexes. Every AI mention is extracted, validated against independent sources, and scored for how real it is. The count stands above 9,000 verified deployments across 3,586 public companies. The pattern in the data matches the pattern in the math. Vertical AI wins. Physical AI wins. The returns concentrate where atoms, regulation, time locked data, costly failure, and scarce expertise live, exactly where the thesis says approximators should bite first. The quarterly analysis is published at the Scanner.

## Why the step works at all

Approximation should be impossible. Learning a generic rule with a hundred moving parts should take more examples than there are atoms. It works because the universe cooperates in three ways. The rules are low dimensional. Energy is mass times c squared, not mass to the hundredth power. The rules are local. You can reason about Palo Alto without consulting a butterfly in Japan. And the rules compose. Nucleotides stack into DNA, cells into organs, parts into cars, cars into fleets. A galaxy, a hurricane, and a seashell draw the same spiral. Katherine was not cheating. She was collecting on a promise the cosmos had already made. So is every model in production today.

![A galaxy, a hurricane, and a nautilus joined by one golden spiral line](/images/era/three-spirals.jpg)
*A galaxy, a hurricane, a seashell. One spiral. The universe reuses its functions.*

## The edges

You know a claim is an era and not a hype cycle when it has edges. This one has three.

Chaos bends it. Lorenz proved that no model can step a single true path through a month of weather, because error compounds. So the era changed what it approximates. Not the one future but the distribution of futures, and stepping distributions now beats the best physical weather ensembles on Earth. Chaos tells the era what to approximate. It does not tell it to stop.

Power prices it. Serve an AGI on an eight way GPU box and give one to every person and every working robot, and two billion boxes draw about ten terawatts. The planet generates about ten. This is not theoretical. Working on a video project inside Google, I was out of compute by ten most mornings, bartering tokens with other teams to finish the day. Tokens and watts are the currency of the next twenty years, which is why the scanner now maps the grid itself, every plant, every battery farm, every data center, tied to the companies behind it.

![Transmission towers at dusk above a valley with a glowing data center](/images/era/grid-night.jpg)
*Tokens and watts, the currency of the next twenty years.*

Measurement ends it. Everything above rests on one hidden assumption. Looking is free. We observe the world and the world does not notice. At the quantum scale that assumption dies. You cannot copy an unknown quantum state, and measuring it changes the answer. There is no dataset at the bottom of physics. Machines that learn behind that veil are just now being built, and one with quantum memory already learns some things exponentially faster than any classical observer. That is not this era. That is the next one, and it will stand on this one the way Katherine stood on Euler.

## What the step cannot choose

Anything is not everything. A machine this capable still cannot choose what is worth doing, and it cannot answer for the choice. It has no family, no career, no reputation to stake. Judgment, accountability, and trust stay with people. Glenn had the fastest computer on Earth and still asked for Katherine. Behind every verified deployment in my scanner, someone signed.

![A hand signing a document with a fountain pen in warm lamplight](/images/era/signature.jpg)
*The one thing the machine cannot produce.*

Here is where I signed. My mother died of cancer at 57, and before she went she made my brother and me promise to find a better way. He became an oncologist. I became the AI guy. Cancer is a trajectory problem. The tumor's equations do not close, so medicine steps them, scan to scan, dose to dose, mid course corrections on the clock the disease sets. My brother checks the numbers at the bedside. I build the approximator that works while he sleeps. The engineer's dog is proof the ladder reaches. The arc bends from terminal to chronic to managed, and it is bending faster now, because the bench scientist works beside the engine.

Katherine Johnson did the math by hand because there was no other way. We have other ways now. The work is the same. Show up. Take the next step. Keep stepping until John gets home.
