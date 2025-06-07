%% Cleaners

clc, clearvars, close all;

%% Anonimus functions to use latter

% Sigmoid activation:
% x     : neural input;
% slope : Steepness of the curve;
% thresh : Threshold of activation.

% x = linspace(-10, 10) %
% slope = 0.5; %
% thresh = 0.0; %

sigmoid = @(x, slope, thresh)  1./(1 + exp(- slope * (x - thresh)));

% plot(x, sigmoid)%

% Normal Distribution:
% x : Neural Space;
% mu : Center;
% sigma : Standart Deviation.


% x = linspace(-10, 10); 
% mu = 0; 
% sigma = 2;

gauss = @(x, mu, sigma)  exp(-0.5*(x - mu).^2/ sigma^2);

% plot(x, gauss, "LineWidth",4)

%% Spatial discretisation

% Limits
L = 10;
dx = 0.1;
N = round(2*L/dx) + 1;
% n of Neurons
x = linspace(-L, L, N);

%% Temporal Discretization

% Range [0, 20s]
T = 20;
dt = 0.01;
M = round(T/dt);

t = linspace(0, T, M);

%% Parameters

% Sigmoid:
slope = 100;
thresh = 0;

% Neural Field(parameters for the equation):
% Time constant;
tau = 1;

% Resting state;
h = 0.5;

%% Dynamic Neural Fiel
u_field = -h * ones(1, N);

%% Coupeling Funtion

% Parameters:
ampl = 2;
width = 0.85;
inhib = 0.5;

% Synaptic weights:
w = ampl * gauss(x, 0.0, width) - inhib;
    % w1 = gauss(x, 0.0, width) - inhib;

% FFT Transform
w_hat = fft(w);

%% external stimuli
bump1 = gauss(x, -5, width);

bump2 = gauss(x, +5, width);

stimuli = zeros(M, N);
for idx = 1 : round(M * 0.5)
    stimuli(idx, :) = bump1 + bump2;

end

%% external stimuli (training)
%bump1 = [1,2,3,4 ,5, 0, 0, 0, 0, 0];
%bump2 = [0,0,0,0,0, 1, 2, 3, 4, 5];

 %stim = zeros(10, 10);

%for idx = 1 : (10/2) 
    %stim(idx, :) = bump1 + bump2;
 %end

 %%