x = linspace(-10, 10);
y = x.^2;

z = fft(y)
plot(x, z, "LineWidth", 4)