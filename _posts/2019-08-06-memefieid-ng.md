---
layout: post
title: Machine Learning Yearning, Memeified.
thumb: /img/ng/chap_1.png
---

Welcome to the first edition of Memeified AI!  This edition translates
Andrew Ng's wonderful, free, online book of
["Machine Learning Yearning"](https://www.deeplearning.ai/machine-learning-yearning/) into
fun memes, tweets, and isms.  Whatever an ism, is.

Memefieid AI summarizes important works in the AI field as
memes and tweets, so that busy people can get a sense of what's
inside. 

I also provide a 20-minute talk with Q&A if you'd like me to
speak at your event.  I can extend it to 45 minutes if you're really
into that sort of thing (and can sit that long). I also have a professional
"immersion" version that lasts an entire day, including hands-on
workshops.  Stay tuned for updates
this Fall from the universities where I'm an adjunct faculty.

I thought I'd share a personal story about how these came about.

I've long been a fan of Carl Sagan, Richard Feynamnn, and Neil de
Grasse Tyson.  They're superb communicators who transform the most
complex mathematics, physics and science into fun, approachable
lectures, speeches, and quips.  I grew up with Carl's Cosmos on PBS,
studied Richard in college, and am in awe of Neil.

A few weeks ago I sat down with my friend Paul Magnone, who've I've
known for quite a long time. He asked me what Feynmann might have done
today, were he to rebuild his famous lectures on science.  How might
apply his infamous wit and sense of humor to heady, complex subjects?
Surely he'd give lectures on YouTube.  But what else?

We had the benefit (or impairment) of a nice bottle of wine, and one
of us blurted out "Memes and Tweets."  At first we laughed.  How
absurd would that be?  These subjects are complex, far more than can
fit in a small form factor.

Then we got to talking.  How much do we really retain from a lecture,
weeks or months after we've participated?  Even professional PR leaders
drive us to focus on sound-bites.  Could we actually extract something
fun, lighthearted but meaningful from such dense material?  The wine
and friendship bravado gave us (over) confidence.

"OK, you first," said Paul.  So that's how I spent an August vacation
back East.  You're seeing the inaugural launch of Memeified AI.
They'll get better.  Maybe.  I hope you like it, and have as much fun
viewing it as I did putting it together.

### 1. Why Machine Learning Strategy

This book will help you spot clues in your machine learning system, saving you months 
to years of development time. 

<img alt="Meme 1" width="200" src="https://scott.ai/img/ng/chap_1.png">

### 2. How to use this book to help your team

Like a tip?  Share the 1-2 pages of text with your colleagues to spread the word.

<img alt="Meme 2" width="200" src="https://scott.ai/img/ng/chap_2.png">

### 3. Prerequisites and Notation

You need to know a little about machine learning (ML),
supervised learning,  and deep learning to get
the most out of this book.

<img alt="Meme 3" width="200" src="https://scott.ai/img/ng/chap_3.png">

### 4 Scale drives machine learning progress

You obtain the best performance from neural network ML systems when
you train a very large network and have a huge amount of data.

<img alt="Meme 4" width="200" src="https://scott.ai/img/ng/chap_4.png">

### 5 Your development and test sets

The "training set" of data trains your network, the "dev set" of data is
then used to tune parameters, and the "test set" evaluates performance.
The dev and test sets direct your team toward important changes in the ML system.

<img alt="Meme 51" width="200" src="https://scott.ai/img/ng/chap_5.png">

### 6 Your dev and test sets should come from the same distribution

Don't train your network on one set of data and expect it to work
well on other types of data.  Be realistic.

<img alt="Meme 6" width="200" src="https://scott.ai/img/ng/chap_6.png">

### 7 How large do the dev/test sets need to be?

The more accuracy you need, the more data you need.  I derived
a handy calculation for you.

<img alt="Meme 7" width="200" src="https://scott.ai/img/ng/chap_7.png">

### 8 Establish a single-number evaluation metric for your team to optimize

Too many cooks spoil the broth.  If you have several, assign weights in an ensemble
or use a geometric mean (e.g. the F1 scores).  Lower values must be better.

<img alt="Meme 8" width="200" src="https://scott.ai/img/ng/chap_8.png">

### 9 Optimizing and satisficing metrics

If you must, you can use two metrics.  One specifies a minimal criteria that
satisfies the business need.  A second allows you to optimize performance.

<img alt="Meme 9" width="200" src="https://scott.ai/img/ng/chap_9.png">

### 10 Having a dev set and metric speeds up iterations

A dev set and a single metric let you iterate faster, keeping your team 
focused.

<img alt="Meme 10" width="200" src="https://scott.ai/img/ng/chap_10.png">

### 11 When to change dev/test sets and metrics

If you realize your initial dev set and metrics weren't right,
change them, ensuring they reflect realistic scenarios.

<img alt="Meme 11" width="200" src="https://scott.ai/img/ng/chap_11.png">

### 12 Takeaways: Setting up development and test sets

The ML iteration cycle involves selecting an idea, writing some code,
evaluating the dev set with your metric, and repeating.  Most initial ideas
flounder, so don't be discouraged. Its all part of the ritual.

<img alt="Meme 12" width="200" src="https://scott.ai/img/ng/chap_12.png">

### 13 Build your first system quickly, then iterate

Don't over-engineer your ML system.  Get something started, quickly.  Iteration
wins over deliberation.

<img alt="Meme 13" width="200" src="https://scott.ai/img/ng/chap_13.png">

### 14 Error analysis: Look at dev set examples to evaluate ideas

Be analytical and systematic in ML.  Look at your data failures, categorize them in a spreadsheet,
see what you have, and evaluate objectively.

<img alt="Meme 14" width="200" src="https://scott.ai/img/ng/chap_14.png">

### 15 Evaluating multiple ideas in parallel during error analysis

Turn your ideas for improving the ML system into columns of a spreadsheet,
then check off which of the failures the idea will address.  Evaluate
objectively.

<img alt="Meme 15" width="200" src="https://scott.ai/img/ng/chap_15.png">

### 16 Cleaning up mislabeled dev and test set examples

Only fix mislabeled data when this "flaw" is larger than other 
flaws you've seen in your data.  For example, if its just a 1% problem, and you've got
a 20% error, focus elsewhere.

<img alt="Meme 16" width="200" src="https://scott.ai/img/ng/chap_16.png">

### 17 If you have a large dev set, split it into two subsets, only one of which you look at

Create an "eyeball" subset of your large dev set which you'll review manually,
applying human intuition to guide ML development.  The rest is called the "blackbox"
dev set.

<img alt="Meme 17" width="200" src="https://scott.ai/img/ng/chap_17.png">

### 18 How big should the Eyeball and Blackbox dev sets be?

Eyeballs tire out after about 1,000 examples.  Blackbox should be big.

<img alt="Meme 18" width="200" src="https://scott.ai/img/ng/chap_18.png">

### 19 Takeaways: Basic error analysis

Use spreadsheets and be analytical when tuning ML systems.

<img alt="Meme 1" width="200" src="https://scott.ai/img/ng/chap_19.png">

### 20 Bias and Variance: The two big sources of error

An easy way to remember these terms is that bias errors occur 
with your training set, variance errors occur with your dev and test
set.

<img alt="Meme 20" width="200" src="https://scott.ai/img/ng/chap_20.png">

### 21 Examples of Bias and Variance

Variance is the *additional* error in your dev and test sets, above and
beyond the error in your training set.

<img alt="Meme 21" width="200" src="https://scott.ai/img/ng/chap_21.png">

### 22 Comparing to the optimal error rate

Sometimes its impossible to get error below a threshold, such as in 
speech recognition problems with very noisy backgrounds where humans struggle
to hear.  This is called the "unavoidable bias" error in your data set.

<img alt="Meme 1" width="200" src="https://scott.ai/img/ng/chap_22.png">

### 23 Addressing Bias and Variance

When you have high training error rates, increase the size of your model to 
capture more information.  When variance is high, add more data to your training
set to fix those errors.

<img alt="Meme 23" width="200" src="https://scott.ai/img/ng/chap_23.png">

### 24 Bias vs. Variance tradeoff

Bigger models improve bias, screw up variance.  Regularization 
can improve variance, but screw up bias.  Ah, life.

<img alt="Meme 24" width="200" src="https://scott.ai/img/ng/chap_24.png">

### 25 Techniques for reducing avoidable bias

Futz with your model architecture and input features to improve bias.

<img alt="Meme 25" width="200" src="https://scott.ai/img/ng/chap_25.png">

### 26 Error analysis on the training set

Classify your training errors as columns in a spreadsheet,
then check off each column for each data element your ML 
system failed to analyze.  

<img alt="Meme 26" width="200" src="https://scott.ai/img/ng/chap_26.png">

### 27 Techniques for reducing variance

Add more training data, introduce regularization (smoothing out weight distributions), 
stop your training earlier, reduce input features, or use a smaller model
to reduce variance.

<img alt="Meme 27" width="200" src="https://scott.ai/img/ng/chap_27.png">

### 28 Diagnosing bias and variance: Learning curves

Train your model on training sets of increasing size while ensuring they each
are a representative sample of the real world.  Evaluate metric on the dev set.
Plot results.

<img alt="Meme 28" width="200" src="https://scott.ai/img/ng/chap_28.png">

### 29 Plotting training error

Add another curve showing metric performance on the test set, as you increase
training set size.

<img alt="Meme 29" width="200" src="https://scott.ai/img/ng/chap_29.png">

### 30 Interpreting learning curves: High bias

If your dev metric plateaus above ideal performance, you have 
high bias.

<img alt="Meme 30" width="200" src="https://scott.ai/img/ng/chap_30.png">

### 31 Interpreting learning curves: Other cases

If your test metric is worse than ideal performance, you have high bias.

<img alt="Meme 31" width="200" src="https://scott.ai/img/ng/chap_31.png">

### 32 Plotting learning curves

If your test metric is good but dev metric is worse and hasn't plateaued, 
you have high variance.

<img alt="Meme 32" width="200" src="https://scott.ai/img/ng/chap_32.png">

### 33 Why we compare to human-level performance

Tasks that humans do well enable us to specify
human-level performance, which gives us a clear goal and insights into
failure along the way.

<img alt="Meme 1" width="200" src="https://scott.ai/img/ng/chap_33.png">

### 34 How to define human-level performance

Be like Andrej, take the test yourself if nobody's done it before.  For all
other cases, aim for the stars and use the human record performance.

<img alt="Meme 34" width="200" src="https://scott.ai/img/ng/chap_34.png">

### 35 Surpassing human-level performance

Use error analysis and introduce data to train your model, just like they
do at Tesla.

<img alt="Meme 35" width="200" src="https://scott.ai/img/ng/chap_35.png">

### 36 When you should train and test on different distributions

Um, never. That's an old school thought.

<img alt="Meme 36" width="200" src="https://scott.ai/img/ng/chap_36.png">

### 37 How to decide whether to use all your data

Never use irrelevant data, or data you won't encounter in practice.

<img alt="Meme 37" width="200" src="https://scott.ai/img/ng/chap_37.png">

### 38 How to decide whether to include inconsistent data

Never use data with irrelevant context.  For example, when predicting NYC real estate values,
don't train on real estate from Detroit.

<img alt="Meme 38" width="200" src="https://scott.ai/img/ng/chap_38.png">

### 39 Weighting data

Apply a weighting factor to errors from synthetic data, so that errors
from real data count more.

<img alt="Meme 39" width="200" src="https://scott.ai/img/ng/chap_39.png">

### 40 Generalizing from the training set to the dev set

If your dev set errors are high, but errors on unseen distributions drawn from your test
set are low, you have data mismatch.

<img alt="Meme 40" width="200" src="https://scott.ai/img/ng/chap_40.png">

### 41 Identifying Bias, Variance, and Data Mismatch Errors

"Avoidable bias" means your model is making mistakes when humans would not.  Your sources
of error are (1) unavoidable bias, (2) avoidable bias, (3) variance, and (4) data mismatch.

<img alt="Meme 41" width="200" src="https://scott.ai/img/ng/chap_41.png">

### 42 Addressing data mismatch

Try to understand why your dev set doesn't represent the same distribution as your
training set.  Once you do, realign the data sets and add more data where needed to
better represent the real world.

<img alt="Meme 42" width="200" src="https://scott.ai/img/ng/chap_42.png">

### 43 Artificial data synthesis

Synthetic data may contain hidden patterns not visible to humans, but that can create
models with artificially good performance.  Be careful, blend synthetic data with real data.

<img alt="Meme 43" width="200" src="https://scott.ai/img/ng/chap_43.png">

### 44 The Optimization Verification test

Many models output a sequence of values. Search is the task of finding this sequence
that maximizes model performance.  Scoring is the task of evaluating a single sequence.

<img alt="Meme 44" width="200" src="https://scott.ai/img/ng/chap_44.png">

### 45 General form of Optimization Verification test

Test the score of the correct output you expect from sequence models.
If this is worse than the output
of your model, you have a search problem.  Otherwise its a scoring problem.

<img alt="Meme 45" width="200" src="https://scott.ai/img/ng/chap_45.png">

### 46 Reinforcement learning example

Always ensure that your reward function in RL actually prefers optimal paths, tested
by evaluating an optimal human performance.

<img alt="Meme 46" width="200" src="https://scott.ai/img/ng/chap_46.png">

### 47 The rise of end-to-end learning

In lieu of end-to-end deep learning with a giant model, try pipelines
of simpler, understandable, explainable tasks.

<img alt="Meme 47" width="200" src="https://scott.ai/img/ng/chap_47.png">

### 48 More end-to-end learning examples

Self-driving cars and speech translation are recent examples of (people trying to use)
end-to-end deep learning systems.

<img alt="Meme 48" width="200" src="https://scott.ai/img/ng/chap_48.png">

### 49 Pros and cons of end-to-end learning

End-to-end systems work best with lots of labeled data, from input to output.  Without
it, data pipelines and features are your friend.

<img alt="Meme 49" width="200" src="https://scott.ai/img/ng/chap_49.png">

### 50 Choosing pipeline components: Data availability

Design your pipeline components around available data, e.g., one to detect cars,
another to detect pedestrians, and a third to plan a path forward.

<img alt="Meme 50" width="200" src="https://scott.ai/img/ng/chap_50.png">

### 51 Choosing pipeline components: Task simplicity

Simple is as simple does.  Don't over-think things,
divide and conquer ML pipelines, keep parts simple, then iterate.

<img alt="Meme 51" width="200" src="https://scott.ai/img/ng/chap_51.png">

### 52 Directly learning rich outputs

With the right input and output pairs, deep learning can produce many
exciting, rich output sequences.  Examples include
image captioning, speech recognition, text to human-like speech, and
question answering systems.

<img alt="Meme 52" width="200" src="https://scott.ai/img/ng/chap_52.png">

### 53 Error analysis by parts

Apply error analysis (error category vs. data spreadsheets) to each 
part of an ML pipeline.

<img alt="Meme 53" width="200" src="https://scott.ai/img/ng/chap_53.png">

### 54 Attributing error to one part

Correct erroneous inputs before testing
an ML pipeline component.  This avoids cascading errors and
helps isolate root causes of failure.

<img alt="Meme 54" width="200" src="https://scott.ai/img/ng/chap_54.png">

### 55 General case of error attribution

Walk your ML pipeline into a directed acyclic graph, then walk it once
to get a linear order of pipeline parts for error analysis. 

<img alt="Meme 55" width="200" src="https://scott.ai/img/ng/chap_55.png">

### 56 Error analysis by parts and comparison to human-level performance

Focus first on pipeline components that haven't reached human-level performance.
Premature optimization is the root of all evil (or, at least some frustration).

<img alt="Meme 56" width="200" src="https://scott.ai/img/ng/chap_56.png">

### 57 Spotting a flawed ML pipeline

When all your parts are working at a human level or above, and the model
is still failing, your pipeline design is flawed.  Change it.

<img alt="Meme 57" width="200" src="https://scott.ai/img/ng/chap_57.png">

### 58 Building a superhero team - Get your teammates to read this

Share Andrew Ng's document and this blog post to help
build your own, superhero ML team!  Thanks for your time today.

<img alt="Meme 58" width="200" src="https://scott.ai/img/ng/chap_58.png">
