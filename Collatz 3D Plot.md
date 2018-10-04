
# Wolfram Mathematica 11.0
```Mathematica
ListPlot3D[Table[ NestList[ If[# == 1, 1, If[EvenQ[#], #/2, (3 # + 1)/2]] &, i, 100], {i, 200}], Mesh -> All, DataRange -> All, PlotRange -> All]
```
