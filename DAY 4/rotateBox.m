function rotatedArray = rotateBox(box, m, n, rotation)
    if(rotation == 'L')
        rotatedArray = rot90(box);
    elseif (rotation == 'R')
        rotatedArray = rot90(box, 3);
    end

    for ii = n-1:-1:1
        for jj = 1:m
            if rotatedArray(ii, jj) == "O"
                for kk = (ii+1):n
                    if rotatedArray(kk, jj) == "X"
                        rotatedArray(kk, jj) = "O";
                        rotatedArray(kk-1, jj) = "X";
                    elseif rotatedArray(kk, jj) == "#" || rotatedArray(kk, jj) == "O"
                        break;
                    end
                end
            end
        end
    end 
end