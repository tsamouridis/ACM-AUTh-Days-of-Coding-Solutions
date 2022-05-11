function maxNumOfPastries = pastry(N, E, A, B)
    maxNumOfPastries = 0;
    
    % this loop checks if there is at least one pastry that can be bought
    % with E. Typically it is the base case of the recursion
    for i = 1:N
        if canBuyIt(A(i), E)
            break;
        else
            return
        end
    end

    %real price holds the price of each pastry after the discount
    realPrice = zeros(1, N); % preallocation
    for i = 1:N
        realPrice(i) = A(i) - B(i);
    end

    [~, index] = min(realPrice); %index of the cheapest pastry

    while canBuyIt(A(index), E)
        E = E - A(index) + B(index); %money left after the discount
        maxNumOfPastries = maxNumOfPastries + 1;
    end
    
    A(index) = Inf; %since the cheapest pastry cannot be bought, we assign infinity to its price
    
    maxNumOfPastries = maxNumOfPastries + pastry(N, E, A, B); % recursion
    
end