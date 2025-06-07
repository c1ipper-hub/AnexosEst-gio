%% Cleans variables, comand line & plots

close all;
clc;
clearvars;

%% Setting the utilitie for the sigmoid function and normal distribution

% Sigmoid Activation:
    % Variables:
    % x     : Neural Input.
    % slope : Steepness of the function.
    % thres : Threshold of activation.

    sigmoid = @(x, slope, thresh)  1./(1 + exp(-slope *(x - thresh)));

% Normal Distribution
    % Variables:
    % x     : Neural Space.
    % mu    : Center Value.
    % sigma : Standart Diviation.

    gauss = @(x, mu, sigma) exp(-0.5 * (x - mu).^2 / sigma^2);

%% Space

    L   = 10;
    dx  = 0.1;
    N   = round(2*L/dx) + 1;
    x   = linspace(-L, L, N);