---
layout: post
title: How to Build an AI
thumb: /img/build_an_ai/ai_1a.jpg
excerpt_separator: <!--more-->
share-img: https://scott.ai/img/astrodock.png
---

Mental models help us conquer complexity.  But there's complexity, 
then there's the face-melting, mind-blowing complexity in 
mathematically intense AI.  Diff eq and quantum physics, anyone?

I have a mental model for AI.  I find this
immensely useful for sleeping peacefully in the
AI revolution.  I disagree with 
naysayers who slam analogies with mammalian brain function. I personally
find the analogy _very_ helpful.  

Time to walk through it.

<img alt="i1" width="500" src="https://scott.ai/img/build_an_ai/ai_1a.jpg">

Let's look inside Bert's head, shall we?

The top, gray layer of Bert's brain is about the size and thickness of a
large dinner napkin,
crammed and crunched into a skull.  The nooks and crannies are filled
with tiny neurons, whose cells look roughly like the figure here on the right
(not drawn to scale).

<img alt="i2" width="500" src="https://scott.ai/img/build_an_ai/ai_2a.jpg">

Inside Bert's head you'll see many layers of these neurons.  If we
separated them like in 7th grade biology class, we'd see a rich fabric
of layers, with sinews of white connecting them together.

Tracing these threads in his nervous system, we'd see them 
connect directly to Bert's eyes for seeing, ears for hearing,
and so forth.  Bert thinks or "computes" by detecting subtle chemical charges
from his senses, propagating charges through his vast, intricate
network of neurons.

At some point, the visuals from Bert's eyes will fire enough neurons, 
they fire others, and so on.  Then Bert feels a certain
tickle in his brain, bellowing

"Cat!"

Google's first true AI found cat's in YouTube, too, after months
and millions.  The board was not, um, "pleased."  I talk about that
on stage a lot. 

Now for some science.  

Let's
draw a map of Bert's neurons, kinda like how we'd
draw a map of airplane flights.   The bodies of the neurons
are our "cities," and the long tubes that connect them are our "flights."   In AI we call 
this a "computational graph."   

Let's _graph_ 9 of Bert's neurons. 

<img alt="i3" width="500" src="https://scott.ai/img/build_an_ai/ai_3a.jpg">

Time for a new science word...  "Tensor."

Neurons in Bert's head carry a little electrical charge.  Imagine if we could see
this charge as a battery level. We can write down the battery
levels for all 9 Neurons.  We'll use 0.0 to mean a dead battery, 1.0 to mean a full
battery.  0.50 is half-charged, 0.25 is a quarter charge, and so on.  You get the idea.

<img alt="i4" width="500" src="https://scott.ai/img/build_an_ai/ai_4a.jpg">

The list of battery levels is called a "tensor."  

We can be super fancy here.  We can list them in a column in Excel, 
and call it a "1-dimensional"
or "1-d" tensor.  1-d is just a vertical list.

We can list a bunch in a spreadsheet, making sure
to fill every row and column in a nice rectangle, without missing a spot. 
That's a "2-d" tensor.   2-d is like a stock plot, with two dimensions "time" and "price."

We can copy that sheet to another, and another.  Mess the
numbers up a bunch, but still keep them between 0.0 and 1.0.  Then
we'd have _sheets_ of tensors, or a "3-d" tensor.  A common 3-d tensor
is a digital image, one sheet each for the pixel values of red, green and blue.

Now you know what a Tensor is.  Not so scary is it?

Know what's cool?  Bert represents _everything_ as a tensor.  So
do you.  

Look at all
the amazing things Bert can hold in his head as a tensor.  Instructions
for driving a car, the taste of his martini from last night, a picture
of a bunny, or words he's reading are just... tensors.

<img alt="i5" width="500" src="https://scott.ai/img/build_an_ai/ai_5a.jpg">

Bert's brain is a _tensor processor_.  Tensors in, tensors out.  Tensors flow
to think. Tensors
flow through the graph sitting in the napkin folded in his skull.   
Indeed, the most popular tool among AI nerds today is... _Tensorflow_.

We can reframe a lot of what humans do as tensor activity.  We can map
sensory experience into tensors.  We flow
those tensors through our brain's computational graph.  Out come other tensors, which
our bodies interpret by moving, speaking, writing, drawing or doing burpees.

Bert can hear someone speak (a tensor of
frequencies over time) and write down words he's heard (a tensor representing
words in a sequence).  That's called _automated speech recognition_.

Bert can watch (image tensors over time) and listen (sound tensors over tiem), then figure out
how to turn the steering wheel (a "control" tensor telling us the angle of turn
and how fast), press the brake (another control tensor), or play with the 
turn signal (a logical on/off tensor).  That's called _autonomous driving_.

Bert can see a description of a bunny (a sequence of word tensors) and then
draw that bunny (generating an image tensor). That's often done
by _generative adversarial networks_ that specialize in creating
big tensors out of smaller ones.

Bert can see a picture of a bunny (an image tensor) and label it with
the word "b u n n y," (a label tensor).  
That's called _logistical regression_. 

A modern, _artificial_ intelligence captures this approach in
software.  Tensors come into our machine,
they flow through a graph, then other tensors flow out.  We use computers
to turn normal everyday things into tensors, hand them to an AI, then interpet
output tensors just like our bodies do.

<img alt="i6" width="500" src="https://scott.ai/img/build_an_ai/ai_6a.jpg">

Shockingly, this works.  Not only does it work, it works _extremely_ well when
run billions of operations per second (the speed of your phone).  The performance
is often super human. This major breakthrough in 2012 led to the world's Nobel prize in
computing.

The _computational graphs_ consiste of _artificial_ neurons, which are simple
math equations of tensor values.  The most popular equation
multiplies input values
by constants called _weights_, then adds constants called _biases_ to yield
outputs.  You may vaguely recall this from 8th grade,

y = m * x  + b

The input tensor is "x." The output tensor is "y." The value "m" is a _weight_.  
The value "b" is a _bias_.  

You may do this (or have teams who do this) with stock prices and inventory levels,
often using single numbers (0-d tensors).  Computers do the same thing, except they
can use 500,000-d tensors.  Half a million D.  That's insane.  But its still
the same math in the end.  Computers are good at numbers.

A major advance in AI added a "fire" macro, like you'd use on a spreadsheet,
to mimic neurons.  Instead of just
using the output tensor Y, we can send the result of "firing" an artificail
neuron like this:

y = fire(m * x + b)

The graph plus all of its constant valus -- m, b, and fire -- are 
collectively called an AI "model."  The "model"
tells a computer how to give us an output tensor, y, when given an input 
tensor "x."

Figuring out what to use for "m" and "b" is the process 
called _machine learning_.  The computer is learning the values
that cause it behave correctly, turning input tensors into the outputs
we expect.

Computers do it by guessing.  If they guess
too low, they tweak "m" and "b" a bit so the answer is higher.  If the guess
is too high, they do the reverse.

The first way a machine learns was inspired by teaching and parenting. 
We give the AI concrete examples.  We show an input tensor,
the output tensor we expect, then ask the AI to guess.

<img alt="i7" width="500" src="https://scott.ai/img/build_an_ai/ai_7a.jpg">

The next major way machines learn reminds me of "Marco, Polo!" we played
on the swim team. If a AI guesses close to the answer, we say they're "warmer" 
and the AI keeps moving forward.  If the AI guesses farther from the answer, 
we say they're "colder" and the 
AI switches direction.

<img alt="i8" width="500" src="https://scott.ai/img/build_an_ai/ai_8a.jpg">

What?  Were you expecting something more exotic?  
Elementary school teaching, Hide n Seek, and tensors?  Is that all there is?

Yes.

Don't forget, we're basically
a bag of water with a worm in the middle for energy, plus some gray jelly up top
to avoid being eaten.  We have some stiff carbon things holding us together,
letting us move a bit better
than a jellyfish.  Humans have a long way to go, evolution-wise.

The tensor mental model is powerful.  We can classify the research from 10,000 brilliant
minds and 100s of thousands of papers into four easy buckets: 

1. Some researchers invent clever ways
to represent our world with tensors.

2. Other scientists invent graphs, or ways to create graphs,
for turning big tensors into small ones, or small ones into
big ones.

3. Others invent neat ways to learn "w," "b" and "fire."  More
recently they've begun to learn the graph itself, too.

4. The last batch use tensors and graphs to do cool things.

Of course, there's always the brave Python-esque researchers 
donig a fifth,
which doesn't fit my model.  Perhaps you're the lone genius who 
will figure out what comes next after tensors!  Your path bucket
is thus:

5. And now for something completely different.

## Conclusion

The tensor model of tensors in, tensors out, flowing through graphs, is a simple
yet powerful technique to understand and build AI systems.  You're probably wondering
how exactly we can represent business, web sites, mobile apps, voice assistants,
and driverless cars with this approach.  I'll be sharing future posts to help
you through that.  I'll also be using techniques that will feel just as easy
as spreadsheet macro's, leveraging the most popular language of the Web -- javascript.

Thanks for tuning in.  If you enjoy this, please follow me on twitter,
connect on LinkedIn, or give me a shout out.  That way we can stay in touch
through humanity's incredible journey forward.


