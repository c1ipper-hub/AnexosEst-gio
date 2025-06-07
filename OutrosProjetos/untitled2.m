clc, clearvars, close all,

x   = linspace(-10, 10);

y1  = -(x-3).^2 + 10;

y2  = -(x-3).^2 + 15;

y3  = -(x-5).^2 + 10;

figure(1)

subplot(1,3,1)
plot(x,y1, "m-", "LineWidth", 2)
xlabel("x"), ylabel("y"), title("y vs x Problem")
legend("y1")

subplot(1, 3,2)
plot(x,y2, "b-", "LineWidth", 2)
xlabel("x"), ylabel("y"), title("y vs x Problem")
legend("y2")

subplot(1,3,3)
plot(x,y3, "g-", "LineWidth", 2)
xlabel("x"), ylabel("y"), title("y vs x Problem")
legend("y3")

xlabel("x"), ylabel("y"), title("y vs x Problem")
grid on


