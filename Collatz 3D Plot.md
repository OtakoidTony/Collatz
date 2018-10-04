
# Wolfram Mathematica 11.0
## Collatz Conjecture 3D Plotting
```Mathematica
ListPlot3D[
  Table[
    NestList[
      If[# == 1, 
        1, 
        If[EvenQ[#],
          #/2,
          (3 # + 1)/2
        ]
      ]
      &, i, 100],
    {i, 200}],
  Mesh -> All,
  DataRange -> All,
  PlotRange -> All
]
```
