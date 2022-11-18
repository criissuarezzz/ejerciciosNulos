#dibuja una gráfica de la función f(x) = x^2

using Plots
gr()

function f(x)
    return x^2
end


x = -10:0.1:10
y = f.(x)

plot(x,y)

savefig("ejercicio1.png")

# Path: ejercicio2.jl

#dibuja una gráfica de la función f(x) = x^2

using Plots
gr()

function f(x)
    return x^2
end
