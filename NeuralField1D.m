%% Cleaning

close all;
clearvars;
clc;

%% Utilities

% Sigmoid Activation:
% x     : Neural Input.
% slope : Steepness.
% thresh: Threshold.
sigmoid = @(x, slope, thresh)   1 ./ (1 + exp(-slope * (x - thresh)));

% Normal Distribution:
% x     : Neural Space.
% mu    : Centre.
% sigma : Standard Deviation.
gauss   = @(x, mu, sigma)       exp(-0.5 * (x - mu).^2 / sigma^2);

%% Spatial Discretisation

% Field spawns [-L, L].
L       = 10.0;
% Spatial step.
dx      = 0.1;
% Number (odd) of neurons. 
N       = round(2*L/dx) + 1;
% Neural Population.
x       = linspace(-L, L, N);

%% Temporal Discretisation

% Simulation spawns [0, T].
T       = 20.0;
% Temporal step.
dt      = 0.01;
% Number of time steps.
M       = round(T/dt);
% Time vector.
t       = linspace(0, T, M);

%% Parameters

% Sigmoid:
slope   = 100.0;
thresh  = 0.0;

% Neural Field:
% Time constant.
tau     = 1.0;
% Resting state.
h       = 0.5;

%% Dynamic Neural Field

u_field = -h * ones(1, N);

%% Coupling Function

% Parameters.
ampl    = 2.00;
width   = 0.85;
inhib   = 0.5;

% Synaptic weights.
w       = ampl * gauss(x, 0.0, width)- inhib;

% FFT Transform.
w_hat   = fft(w);

%% External Stimuli

% Bump 1 (stronger).
bump1   = 1.0 * gauss(x, -5.0, 1.0);
% Bump 2 (weaker).
bump2   = 1.0 * gauss(x, +5.0, 1.0);

stimuli = zeros(M, N);
for idx = 1 : round(M * 0.5)
    stimuli(idx, :) = bump1 + bump2;
end

%% Simulation

% Iterate through time.
for i = 1 : M
    % Firing rate.
    f       = sigmoid(u_field, slope, thresh);
    f_hat   = fft(f);
    % Convolution.
    conv    = dx * ifftshift(real(ifft(f_hat .* w_hat)));
    % Field Update.
    u_field = u_field + dt/tau * (-u_field + conv + stimuli(i, :) - h);
    % Visualisation.
    if mod(i, 5) == 0
        plot(x, u_field, "k", "LineWidth", 2.0);
        hold on;
        plot(x, stimuli(i, :), "b", "LineWidth", 2.0);
        hold off; drawnow;
    end
end

% Close the Figure.
close all; 

%% Results

figure;
plot(x, u_field, "k", "LineWidth", 2.0);
hold on;
plot(x, zeros(1, N), "--k", "LineWidth", 2.0);
xlabel("Feature Dimension", "FontSize", 16);
ylabel("Neural Activation", "FontSize", 16);
title("Neural Field Simulation", "FontSize", 20);