# You complete me

The idea here is to create phases from a seed (this is made up code at this point):

## Background

```
import you_complete_me
MAX_PHRASE_WORDS = 10
completer = YouCompleteMe('some_pregenerated_db.sqllite', MAX_PHRASE_WORDS)
completer.complete("mary had a") => "mary had a little closer to you soon love to"
```

Ultimately, I hope to use this with the Google AIY voice kit to make google say funny things.  It's
not meant for serious consumption, but if you want to use this as a base for something more
powerful, that's what open source is all about right?

## Getting started

* clone this project:

```
git clone ...
cd YouCompleteMe
```
* make a data driector

```
mkdir data
cd data
```

* Download and create a corpus:

(note that the OANC is the biggest corpus I've used. I'm sure if you used a bigger corpus this thing
would break)

```
wget http://www.anc.org/OANC/OANC_GrAF.tgz
tar xvfz OANC_GrAF.tgz
find OANC-GrAF -name "*.txt" -exec cat {} \; > oanc.txt
```

* Create a database of 4-grams:

```
python3 count_ngrams.py 4 < data/oanc.txt > data/oanc_4gram_counts.txt
```

* ???
* Profit!!

## MVP TODO

* Modify `count_ngrams.py` create a database instead of a text file
* Make the code under "Background" above actually work
* Just use the most frequent trigram to generate the next word
* Super basic Google AIY integration

## Nice to haves

* scrub data for repeated words. For some reason the OANC corpus has a bunch of repeated "a"'s which
  might cause kind of an infinite serins of "a"s in the output. Or something
* make this probabalistic where the next word is taken not from just the most frequent matching
  n-gram, but from a random one from the top matches weighted by the frequency
* make a youtube video of google voice hilariously completing my sentences

## Trobleshooting/FAQ

Q: Hey, these directions create a text file, not a database like in the example. What gives?  A: You
expected something that works? Not yet bud

Q: I tried to import your library and it doesn't work A: Yeah... that's because it doesn't exist yet

Q: This repo was last updated a **long** time ago and none of what's outlined here works, what
gives?  A: Maybe I lost interest? Maybe you're impatient?
