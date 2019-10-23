
## Collatz Conjecture 3D Plotting

### Wolfram Mathematica 11.0
```Mathematica
CollatzList[i_]:=NestList[If[# == 1, 1, If[EvenQ[#], #/2, (3 # + 1)/2]] &, i, 100] (*This is a list for plotting.*)
ListPlot3D[
    Table[CollatzList[i], {i, 200}],
        Mesh -> All,
        DataRange -> All,
        PlotRange -> All,
        PlotTheme -> "Detailed"
]

ListPlot[CollatzList[30]]

ListContourPlot[Table[CollatzList[i],{i,2,100}],DataRange -> All,
        PlotRange -> All,
        PlotTheme -> "Detailed"]
        
        
Collatz[base_][n_]:=CollatzList[base][[n]]

OneWorkCollatz[base_,x_]:=If[Collatz[base][x]-Collatz[base][x-1]<0,-1,If[Collatz[base][x]-Collatz[base][x-1]>0,1,0]]

Plot[OneWorkCollatz[111,Floor[x]],{x,3,70},PlotRange -> All,
        PlotTheme -> "Detailed"
]
 ```
