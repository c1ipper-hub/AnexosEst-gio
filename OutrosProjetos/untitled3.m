clc, clearvars, close all,

x = linspace(0, 10,100000);
y = sin(x);

% plot(x, y, "."), hold on, plot([0, 10],[0.8, 0.8])
result1 = sum(y > 0.8);
 
result2 =  sqrt((sum(y <= 0.8) - 100000).^2);

 result1
 result2

 