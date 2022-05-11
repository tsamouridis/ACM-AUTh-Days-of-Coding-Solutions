%this function checks whether or not we can afford the price of a pastry
function res = canBuyIt(priceOfPastry, E)
    if priceOfPastry <= E
        res = true;
    else
        res = false;
    end
end