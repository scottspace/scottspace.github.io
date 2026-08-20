# Check the Numbers

*A machine took Katherine Johnson's job title in 1962. John Glenn bet his life on what she still had. The same question is now on every desk.*

**Scott Penberthy** · August 2026 · 1,350 words

Canonical: https://scott.ai/essays/check-the-numbers/

---

On February 20, 1962, John Glenn sat strapped inside a capsule the size of a phone booth, on top of an Atlas rocket like one he had watched explode three years earlier. Reentry was a corridor a few degrees wide. Too shallow meant skipping off the atmosphere into space. Too steep meant burning. The most advanced computer on Earth had calculated his trajectory. He would not go.

He asked for a person instead. "Get the girl to check the numbers." Her name was Katherine Johnson. The title printed on her badge was Computer. The machine had already taken her title. What did she still have, that a man would bet his life on?

Hold that question. It is now everyone's question.

## The Unsolvable

The reentry equations could not be solved exactly. Most of nature's equations cannot. The universe gives us its rules. It does not give us the answers. So Katherine stepped them. Take a tiny step. Ask the rule where things are heading. Step again. Every step is slightly wrong, yet the full path brought Glenn home. She fought to put her name on that trajectory report, at a laboratory where women rarely received credit. Remember the name.

## Reading History Backward

Here is the strange privilege of writing this in 2026. We already know the answer. Knowing the answer changes what we can see in the beginning. History is a trail walked in fog. You only see the trail from the summit.

![A switchback mountain trail at dawn descending into a valley of fog, the upper stretches catching golden light](https://scott.ai/images/essays/check-the-numbers/summit.jpg)

*History is a trail walked in fog. The whole path is visible only from the summit.*

From the summit, 250 years of mathematics collapse into a single move, taken six times.

In 1687, Newton and Leibniz wrote the laws of nature as differential equations. A law became a local rule of change. Then came the catch. Almost none of these equations can be solved in closed form.

In 1768, Euler answered them anyway. His method gives up the exact solution and approximates the trajectory. The next state equals this state, plus a small step in the direction the rule points. Each step carries a small error that stays bounded when the steps stay small. This is the equation Katherine used.

> xₜ₊₁ = xₜ + ε f(xₜ)
>
> *Six formulations · 250 years · one move*

In 1847, Cauchy turned the same step on optimization. To find the bottom of a valley you cannot see, measure the slope where you stand and step downhill. Gradient descent is Euler's method applied to an error surface. Every neural network alive today is trained by this rule.

In 1948, Shannon turned the step on language. He treated English as a stochastic process and asked how well a machine could approximate the distribution of the next symbol, given the symbols before it. His instruments were novels and coin flips. The modern language model is his estimator, scaled beyond anything Bell Labs could have powered.

In 2021, Song and colleagues turned the step around. Their diffusion models learn the local structure of a data distribution, then integrate backward from pure noise toward the data, removing a little noise at each step. The sampler that takes those steps is named for Euler. This is the mathematics inside image generators and AlphaFold 3.

And now a sixth rung. Vision-language-action models put the world's state and the machine's action into one formulation. The next state equals this state, plus a small step, given the action taken. One new term. The step becomes a policy. The machine no longer approximates only what the world is doing. It approximates what the world will do if it acts.

> xₜ₊₁ = xₜ + ε f(xₜ, aₜ)
>
> *The same move · one new term · the action*

Six formulations. One move. Watch what is being approximated as the ladder rises. A trajectory. A minimum. A sequence. A distribution. A consequence. Every rung makes the same bargain. Give up the exact answer no one can compute. Take a small step anyone can. None of the six knew they were building the same machine. Only from here, after the answer is in hand, does the ladder look like one ladder. I call the time we live in the Approximation Era.

Readers of this periodical know the climb in their bones. In 1901, Marconi pushed a signal across the Atlantic before physics said it could arrive. The waves should have flown straight off the curve of the Earth. The ionosphere caught them, though no one could yet say why. He climbed in the fog. The trail appeared later.

## From Theorem to Machine

The mathematics waited on hardware. In 1989, Cybenko proved that a large enough neural network can approximate any continuous function. The theorem was a map with no ship. In 2012, three researchers in Toronto entered a photo contest with a network that ran on two gaming cards. It nearly halved the error rate overnight. The theorem had become cheap. Anything you can observe, it can learn to understand.

In 2022 the public met the generator, which is approximation run in reverse. Anything it understands, it can create. Now the actor closes the loop. Anything it can create, it can act on. A robot hand pours coffee. A surgical tool holds steady. The samplers stepping the motors still carry Euler's name. Observe, understand, generate, act, then observe again. This community wrote the theory of that loop and called it feedback.

![A robotic hand holding a piece of chalk up to a vast dark blackboard lit by a warm desk lamp](https://scott.ai/images/essays/check-the-numbers/chalk-hand.jpg)

*After 250 years, the step learned to take itself. Now it is learning to act.*

One honest limit remains. Chaos is real. Lorenz showed in 1963 that some systems amplify any error in the last digit until the forecast is worthless. No approximator will ever step a single true path through a month of weather. The era's answer is to change the object of approximation once more. Where one future cannot be known, the distribution of futures can. GenCast learned that distribution and now beats the best physical ensemble forecast on Earth. Chaos does not end the era. It tells the era what to approximate.

A wrong sentence costs a blush. A wrong motion can cost a hand. We are all back on the pad.

## What She Still Had

So return to the question. Glenn's machine was hundreds of thousands of times faster than Katherine Johnson. He asked for her anyway.

Her check took a day and a half at a desk calculator. She recomputed the entire flight, digit against digit, until her numbers matched the machine's.

Now look closely at the era's promise. Anything you can observe. Anything, not everything. A machine this capable still cannot choose what is worth doing. What should these machines do for us? Which problems deserve them? Will the answer leave our lives better? The machine never asks. Choosing is judgment, and judgment is taste.

And every choice needs someone to answer for it. The machine risks nothing. It has no family, no career, no aspirations, no reputation. A person who signs puts all of those on the table. That is a great deal to stake, and it is exactly why the signature means something. Trust is granted to someone who can be wrong at a cost. Katherine's name on that report became the one thing no machine could produce.

**Judgment. Accountability. Trust.** That is what she still had. That is what we still have.

## Your Katherine Johnson Moment

Every idea you set aside because it needed fifty people and ten years has quietly come back within reach. I watched one person, in two days, draft regulatory submissions for sixty-three countries in seven languages. Notice what was missing. It was not code. Code has become cheap. What was missing was a signature.

That is where you come in. Somewhere in your work there is a launch that will not happen until someone the crew trusts says the numbers are right. Not the fastest mind in the room. The one who signs.

So I leave you with the question I ask every room. When anything is possible, what will you say is worth doing? When the answer has to be right, what will they turn to you for? What is your Katherine Johnson moment?

Katherine kept working for thirty-three years after the machine took her title, helped put men on the Moon, and lived to one hundred and one. The man who refused to launch without her went back to space at seventy-seven, still the oldest human ever to orbit the Earth. The machine took her title. It never touched her.

John Glenn knew his answer. He made it an order.

**Be the one they won't launch without.**

---

*Written for the Marconi Association's periodical. Adapted from "Check the Numbers," a talk in the Google Greyglers Legends series, built on the Approximation Era thesis at https://scott.ai/era.*
