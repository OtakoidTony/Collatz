
# Mathematica를 이용하여 콜라츠 수열을 입체적으로 시각화하는 
```Mathematica
ListPlot3D[Table[ NestList[ If[# == 1, 1, If[EvenQ[#], #/2, (3 # + 1)/2]] &, i, 100], {i, 200}], Mesh -> All, DataRange -> All, PlotRange -> All]
```
