---
layout: post
title: How to Build an AI
thumb: /img/build_an_ai/ai_1a.jpg
excerpt_separator: <!--more-->
share-img: https://scott.ai/img/build_an_ai/ai_1a.jpg
---
I have a mental model for AI. I find the model
useful for understanding deeply complex,
mathematical techniques as well as abstract, high-level
coding in AI programs.  The analogy helps me work
with clients to build massive data pipelines that drive
billion-dollar businesses.  If you've never really understood
what a "tensor" was, or how "TensorFlow" got its name,
this post is for you.  To me, "tensors" in AI are as important
as "records" in the database world.
<!--more-->

I disagree with 
naysayers who dismiss analogies to brain function. I personally
find these analogies _very_ helpful.  After all, they inspired original research
into AI back in the 1940s.  Further, today's deep learning systems borrow a lot from
_biological architectures_ of the brain.  But your mileage may vary, and that's 
cool.

<img alt="i1" width="500" src="https://scott.ai/img/build_an_ai/ai_1a.jpg">

Let's look inside Bert's head, shall we?

The top, gray layer of Bert's brain is about the size and thickness of a
large dinner napkin,
crammed and crunched into a skull.  The nooks and crannies are filled
with tiny neurons, whose cells look roughly like the figure below
(not drawn to scale).

<img alt="i2" width="500" src="https://scott.ai/img/build_an_ai/ai_2a.jpg">

Inside Bert's head you'll see layers of neurons.  If we
separated them like we did in 7th grade biology class, we'd see a rich Baklava
of gray layers all connected by sinews of neurons.

Tracing these threads in Bert's nervous system, we'd see the neurons
connecting directly to Bert's eyes for seeing, ears for hearing,
and so forth.  Bert thinks or "computes" by detecting subtle chemical charges
from his senses, propagating charges through his vast, intricate
network of neurons.

At some point, the visuals from Bert's eyes will fire enough neurons, 
they fire others, and so on.  Then Bert feels a certain
tickle in his brain, bellowing

"Cat!"

Now for some science.  

Let's
draw a map of Bert's neurons, similar to how we'd
draw a map of airplane flights.   The bodies of the neurons
are our "cities," and the long tubes that connect them are our "flights."   In AI we call 
this a "computational graph."  Let's _graph_ 9 of Bert's neurons. 

<img alt="i3" width="500" src="https://scott.ai/img/build_an_ai/ai_3a.jpg">

Neurons in Bert's head carry a tiny electrical charge.  Imagine if we could see
this charge as a battery level. We can write down the battery
levels for all 9 neurons in the graph.  We'll use 0.0 to mean a dead battery, 1.0 to mean a full
battery.  0.50 is half-charged, 0.25 is a quarter charge, and so on.  You get the idea.

<img alt="i4" width="500" src="https://scott.ai/img/build_an_ai/ai_4a.jpg">

The list of battery levels is called a "tensor."  We can be super fancy here, and
use "higher order" math:

 - We can list battery levels in a column in Excel, 
and call it a "1-dimensional"
or "1-d" tensor.  1-d is just a vertical list.

- We can put battery levels in a spreadsheet, making sure
to fill every row and column in a nice rectangle, without missing a spot. 
That's a "2-d" tensor.   2-d is like a stock chart, with two dimensions "time" and "stock price."

- We can copy that sheet to another, and another.  Mess the
numbers up a bunch, but still keep them between 0.0 and 1.0.  Then
we'd have _sheets_ of tensors, or a "3-d" tensor.  A common 3-d tensor
is a digital image, one sheet each for the pixel values of red, green and blue.

Bert represents _everything_ as a tensor.  Imagine all
the amazing things Bert holds in his head as tensors.  Instructions
for driving a car, the taste of his martini from last night, a picture
of a bunny, or words he's reading are all... tensors.

<img alt="i5" width="500" src="https://scott.ai/img/build_an_ai/ai_5a.jpg">

Bert's brain is a _tensor processor_.  Tensors in, tensors out.  Tensors flow
to think.  Interestingly enough, the
most popular tool among AI nerds today is... _Tensorflow_.

We can reframe human thinking as tensor activity.  We map
sensory experience into tensors.  We flow
those tensors through the brain's graph, producing more
tensors.  Our bodies interpret those tensors by moving, speaking, writing, 
drawing or doing burpees. 

Here are some examples:

 - Bert can hear someone speak (a tensor of
frequencies over time) and write down words he's heard (a tensor representing
words in a sequence).  That's called _automated speech recognition_.

 - Bert can watch (image tensors over time) and listen (sound tensors over time), then figure out
how to turn the steering wheel (a "control" tensor telling us the angle of turn
and how fast), press the brake (another control tensor), or play with the 
turn signal (a logical on/off tensor).  That's called _autonomous driving_.

 - Bert can see a description of a bunny (a sequence of word tensors) and then
draw that bunny (generating an image tensor). That's often done
by _generative adversarial networks_ that specialize in creating
big tensors out of smaller ones.

 - Bert can see a picture of a bunny (an image tensor) and label it with
the word "b u n n y," (a label tensor).  That's called _logistical regression_. 

A modern, _artificial_ intelligence captures this approach in
software.  Tensors come into our machine,
they flow through a graph, then other tensors flow out.  We use computers
to turn normal everyday things into tensors, hand them to an AI, then interpet
output tensors just like our bodies do.

<img alt="i6" width="500" src="https://scott.ai/img/build_an_ai/ai_6a.jpg">

Shockingly, this works.  Not only does it work, it works _extremely_ well at 
billions of operations per second (e.g., at the speed of your phone).  The performance
is super human. This major breakthrough in 2012 led to the world's Nobel prize in
computing!

The _computational graphs_ consist of _artificial_ neurons, another name for
math equations with tensor values.  The most popular neuron
multiplies input values
by constants called _weights_, then adds constants called _biases_, to yield
outputs.  You may recall this equation of a line,

y = m * x  + b

The input tensor is "x." The output tensor is "y." The value "m" is a _weight_.  The value "b" is a _bias_.  You may have used this math with stock prices and inventory levels,
often using single numbers.  Computers do the same thing.  They just use
use more dimensions.  A lot more.

A major advance in AI introduced a radically simple "fire" macro, 
like the @macro's you've  used
on a spreadsheet, 
to mimic neurons.  Instead of 
using the output tensor Y, we can send the result of "firing" an artificial
neuron like this:

y = @fire(m * x + b)

The graph plus all of its constant valus -- m, b, and @fire -- are 
collectively called an AI "model."  The "model"
tells a computer how to give us an output tensor, y, when given an input 
tensor "x."

Figuring out what to use for "m" and "b" is the process 
called _machine learning_.  The computer is learning the values
that cause it to behave correctly, turning input tensors into the outputs
we expect.

Computers do this by guessing.  If they guess
too low, they tweak "m" and "b" a bit so the answer nudges higher.  If their guess
is too high, they do the reverse, nudging lower.

The first way a machine learns was inspired by teaching from a supervisor. 
We give the AI concrete examples.  We show an input tensor,
the output tensor we expect, then ask the AI to guess.  This is called
_supervised_ learning.

<img alt="i7" width="500" src="https://scott.ai/img/build_an_ai/ai_7a.jpg">

The next major way machines learn reminds me of "Marco, Polo!" we played
on the swim team. If an AI guesses close to the answer, we say they're "warmer" 
and the AI keeps moving forward.  If the AI guesses farther from the answer, 
we say they're "colder" and the 
AI switches direction.  This is called _reinforcement_ learning.

<img alt="i8" width="500" src="https://scott.ai/img/build_an_ai/ai_8a.jpg">

What?  Were you expecting something more exotic?   Elementary school teaching,
Hide n Seek, and tensors?  Is that all there is?

Yes.

Don't forget, we're basically
a bag of water with a worm in the middle for energy, plus some gray jelly up top
to avoid being eaten.  We have some stiff carbon things holding us together,
letting us move a bit better
than a jellyfish.  Humans have a long way to go, evolution-wise.

The tensor mental model is useful for understanding
the latest research as four basic ideas: 

1. Some researchers invent clever ways
to represent the world with tensors.

2. Other scientists invent graphs, or ways to create graphs,
for turning big tensors into small ones, or small ones into
big ones.

3. Others invent neat ways to learn "w," "b" and "fire."  More
recently they've begun to learn the graph itself, too.

4. The last batch use tensors and graphs to do cool things.

Of course, there's always the brave Monty Python-ish researcher
pulling a fifth,
which doesn't fit my tensor model.  Perhaps you're the lone genius who 
will figure out what comes next after tensors!  Your bucket
is thus:

5. "And now for something completely different."

## Conclusion

The tensor model of tensors in, tensors out, flowing through graphs, is a simple
yet powerful technique to understand and build AI systems.  

You're probably wondering
how exactly we can represent business, documents, web sites, mobile apps, voice assistants,
customers, inventory, risk, driverless cars and more with this approach.
How do we protect against hidden biases
in our tensors?  How do we make tensors that protects our privacy, in areas
like medicine and finance?

I'll be sharing future posts to help
you through all that.  I'll also be using techniques that will feel just as easy
as spreadsheet @macro's, leveraging the most popular scripting languages of the Web.

Thanks for tuning in!  If you enjoy this, please follow me on twitter,
connect on LinkedIn, or give me a shout out.  That way we can stay in touch
through humanity's incredible journey forward.