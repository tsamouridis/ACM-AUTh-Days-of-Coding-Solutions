function maxCapacity = findMaxCapacity(height)
	maxCapacity = 0;
    n = length(height);
    for ii = 1:n-1
        for jj = ii+1:n
                side1 = min(height(ii), height(jj));
                side2 = jj-ii;
                value = side1*side2;
            if value > maxCapacity
                maxCapacity = value; 
            end
        end
    end
end