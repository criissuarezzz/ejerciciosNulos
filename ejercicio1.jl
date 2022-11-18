# calcular determinante nxn

function det(A)
    n = size(A,1)
    if n == 1
        return A[1,1]
    else
        det = 0
        for i = 1:n
            det += (-1)^(i+1)*A[1,i]*det(A[2:n, [1:i-1; i+1:n]])
        end
        return det
    end
end
