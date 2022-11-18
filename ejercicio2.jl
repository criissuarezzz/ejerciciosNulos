#resolver un ecuaciones diferencias finitas
#usando el metodo de Euler
#
#dy/dt = f(t,y)
#y(t0) = y0
#

using Plots
gr()

function f(t,y)
    return -y
end

function euler(f,t0,y0,tf,h)
    t = t0:h:tf
    y = zeros(length(t))
    y[1] = y0
    for i in 1:length(t)-1
        y[i+1] = y[i] + h*f(t[i],y[i])
    end
    return t,y
end

t,y = euler(f,0,1,10,0.1)
plot(t,y)

savefig("ejercicio2.png")

# Path: ejercicio3.jl

#dibuja una gráfica de la función f(x) = x^2

using Plots
gr()

function f(x)
    return x^2
end


#resolver un ecuaciones diferencias finitas
#usando el metodo de Euler
