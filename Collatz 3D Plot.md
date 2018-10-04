
# Wolfram Mathematica 11.0
## Collatz Conjecture 3D Plotting
```Mathematica
Collatz[i_]:=If[# == 1, 1, If[EvenQ[#], #/2, (3 # + 1)/2] (*This is Collatz Conjecture Algorithm.*)
CollatzList[i_]:=NestList[Collatz[i]] &, i, 100] (*This is a list for plotting.*)

ListPlot3D[
    Table[CollatzList[i], {i, 200}],
        Mesh -> All,
        DataRange -> All,
        PlotRange -> All
]
```
