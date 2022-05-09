box = ["X" "X" "X"; "X" "O" "X";"O" "#" "X"; "O" "X" "#"]
[m,n] = size(box);
rotateBox(box,m, n,'R')
rotateBox(box,m, n,'L')