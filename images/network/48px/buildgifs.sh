#!/bin/bash

duration=0.2

#python makegif.py "sample1/time*_x.png" x.gif -d $duration

mkdir -p anim
mkdir -p anim/x
python makegif.py "sample1/time*_x.png" anim/x.gif -d $duration

# function gifbuild {
#     echo python makegif.py $1 $2 -d $duration
#     echo mkdir -p $2
#     echo convert $2 -coalesce $2/x.png
# }

for dim in 3 22 47; do
    mkdir -p anim/f
    mkdir -p anim/i
    mkdir -p anim/j
    mkdir -p anim/o
    mkdir -p anim/state

    python makegif.py "sample1/time*/"$dim"_fGate.png" anim/$dim"f.gif" -d $duration
    convert anim/x.gif -coalesce anim/x/x.png

    python makegif.py "sample1/time*/"$dim"_fGate.png" anim/$dim"f.gif" -d $duration
    convert anim/$dim"f.gif" -coalesce anim/f/$dim"f.png"

    python makegif.py "sample1/time*/"$dim"_iGate.png" anim/$dim"i.gif" -d $duration
    convert anim/$dim"i.gif" -coalesce anim/i/$dim"i.png"

    python makegif.py "sample1/time*/"$dim"_jGate.png" anim/$dim"j.gif" -d $duration
    convert anim/$dim"j.gif" -coalesce anim/j/$dim"j.png"

    python makegif.py "sample1/time*/"$dim"_oGate.png" anim/$dim"o.gif" -d $duration
    convert anim/$dim"o.gif" -coalesce anim/o/$dim"o.png"

    python makegif.py "sample1/time*/"$dim"_state.png" anim/$dim"state.gif" -d $duration
    convert anim/$dim"state.gif" -coalesce anim/state/$dim"state.png"
done
