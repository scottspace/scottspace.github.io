# The Approximation Era

*Compute is replacing calculus. 1,200-word cut, 2026-09-10.*
<!-- equation-diff.png doubles as the og:image / social card -->
![Euler 1768 beside the vision language action equation, one added term in gold](/images/era/equation-diff.png)
*One added letter, 258 years apart.*

---

Take the equation Euler published in 1768.

*y₁ = y₀ + h f(y₀)*

Add one letter.

*y₁ = y₀ + h f(y₀, a₀)*

The first line brought John Glenn home from orbit. The second drives every robot now learning to work in the physical world. One added letter, 258 years apart. That edit is the story of our time.

Here is my claim. We live in the Approximation Era. When we cannot solve nature's equations, we step them. Compute keeps getting cheaper, so the step is becoming nearly free. Soon we can build anything, digital or physical. We cannot build everything. This essay lives between those two sentences. First the ladder that makes the first sentence true. Then the two walls that make the second one true.

## One move, six equations

In 1687, Newton and Leibniz found that one kind of sentence describes how anything changes. Here is how the next instant depends on this one.

*dy/dt = f(y)*

That sentence is a differential equation, and it runs the universe. The catch is that writing the rule is not solving it. Almost none of these equations have exact answers. The universe made a promise it would not keep.

In 1768, Euler stopped waiting. Obey the rule in small steps. Ask which way things are heading. Step a little that way. Ask again. Every step is slightly wrong. The walk still gets you home. In 1962, Katherine Johnson stepped John Glenn's trajectory at a desk calculator, and he flew because she signed. I tell that story in [Check the Numbers](/essays/check-the-numbers/).

![A coarse gold Euler polyline drifting off a smooth pale curve while a finer one hugs it](/images/era/step-curve.jpg)
*The move itself. Big steps miss. Small steps hug the truth. Compute buys smaller steps.*

In 1847, Cauchy aimed the step downhill.

*w₁ = w₀ − η ∇L*

That is gradient descent, and it is how every neural network on Earth learns. Start very wrong. Step downhill on your errors a few million times. Become a little less wrong each time.

In 1948, Shannon stepped through language. Guess the next word from the words so far. He played the game with a shelf of novels and coin flips. ChatGPT is the same game with the whole internet, and it passes the bar exam.

In 2021, diffusion ran the walk backward. Start with static. Remove a little noise. Step again until a picture appears, or a protein. AlphaFold 3 turned a five-year thesis into a two-day compute job and ran it two hundred thousand times. The sampler inside is named for Euler.

The sixth rung is the diff at the top. Add the action taken, and the step becomes a policy. The machine no longer just predicts what the world will do. It learns what the world will do if it acts. That equation now drives real arms and real tools.

Six equations. One move. A trajectory, a minimum, a sentence, a picture, a consequence. Six strangers, 250 years, one move.

## Why the step works

Approximation should be impossible. Learning a rule with a billion moving parts should take more examples than there are atoms. It works because the universe cooperates three ways. The rules are low dimensional. Energy is mass times c squared, not mass to the hundredth power. The rules are local. You can reason about Palo Alto without consulting a butterfly in Japan. And the rules compose. Nucleotides stack into DNA, cells into organs, parts into cars. A galaxy, a hurricane, and a seashell draw the same spiral. Katherine was not cheating. She was collecting on a promise the cosmos had already made. So is every model in production today.

![A galaxy, a hurricane, and a nautilus joined by one golden spiral line](/images/era/three-spirals.jpg)
*A galaxy, a hurricane, a seashell. One spiral. The universe reuses its functions.*

## Two walls

A capability this general needs its edges drawn before you trust it. This one has exactly two.

Chaos caps prediction. Lorenz proved that no model can step one true path through a month of weather. Error compounds until the forecast is fiction. So the era changed its product. It does not predict the future. It predicts the futures. Step a thousand walks from the same present and keep them all. We predict a set of paths, not one. Stepping distributions this way now beats the best physical weather ensembles on Earth. Chaos did not stop the era. It told the era what to sell.

![A fan of gold paths spreading from a single bright point, one silver path running through them](/images/era/chaos-fan.jpg)
*From one present, a fan of futures. We predict the set, not the path.*

Quantum ends observation. Every rung on the ladder assumes looking is free. We observe the world, and the world does not notice. At the bottom of physics that assumption dies. You cannot copy an unknown quantum state. Measuring it changes the answer. There is no dataset behind that veil. Machines that learn behind it are just now being built, and one with quantum memory already learns some things exponentially faster than any classical observer. That is not this era. The era ends at that wall, and the next one starts behind it.

![A gold dilution refrigerator glowing in a dark lab](/images/era/quantum-chandelier.jpg)
*The machine behind the veil.*

## Anything, not everything

Inside those walls, the recipe is now general. A model, capital, and watts.

An AI engineer in Australia proved it when his dog was dying of cancer. He sequenced the dog. He sequenced the tumor. A model designed the molecule that teaches an immune system that exact face, and he had it made. The dog is in remission. The same play is in human trials for HER2 positive cancer right now. My scanner counts the pattern at market scale: more than 9,000 verified AI deployments across 3,586 public companies, concentrated where atoms and consequences live.

![A golden retriever standing on a dock at sunrise](/images/era/dog-morning.jpg)
*In remission. The ladder reaches all the way to the dog.*

Notice what the recipe no longer includes. Expertise. Expert-level work in any domain is becoming a commodity you rent by the token. Knowledge stopped being the bottleneck. Energy is the bottleneck now. Run the arithmetic. Serve an AGI on an eight-way GPU box. Give one to every person and every working robot. Two billion boxes draw about ten terawatts. The planet generates about ten. Soon, anyone with access to capital and watts can build anything, digital or physical. The planet has the watts for anything. It does not have the watts for everything.

![Transmission towers at dusk above a valley with a glowing data center](/images/era/grid-night.jpg)
*Tokens and watts, the currency of the next twenty years.*

## Choosing

So the last scarce thing is the choice. A machine this capable still cannot choose what is worth building, and it cannot answer for the choice. It has no family, no career, no reputation to stake. Judgment, accountability, and trust stay with people. Glenn had the fastest computer on Earth and still asked for Katherine. Choosing is the one step the machine will never take for us.

Here is where I signed. My mother died of cancer at 57. Before she went, she made my brother and me promise to find a better way. He became an oncologist. I became the AI guy. Our watts go to cancer. And the next choice is already made. The quantum dark, where the next era waits.

![A hand signing a document with a fountain pen in warm lamplight](/images/era/signature.jpg)
*The one thing the machine cannot produce.*

Katherine Johnson did the math by hand because there was no other way. We have other ways now. The work is the same. Show up. Take the next step. Keep stepping until John gets home.
