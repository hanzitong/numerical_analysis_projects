
set terminal png
set output 'plot.png'
set xlabel "x"
set ylabel "y"
plot "output.dat" using 1:2 with lines title "Obj Function"

