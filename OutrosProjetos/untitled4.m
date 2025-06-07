%% section 1 | Questions
% ? quantos 3 existem?
% if there are more than 3 numbers that are a 3 print "wow!"

%% sec 2 | cleaners
% cleaners


clc, clearvars;
%% sec 3 | logic operations
% radom genaration

a = randi(5, 1, 10);

% actions

num_of_3s = sum(a == 3);

num_of_3s

if num_of_3s >= 3
    display("Wow!")
else
    display("Ana Rita linda")
end

%% sec 4 | foor loop

 a = randi(5, 1, 10^7);
 count = 0;
tic
for i = 1:length(a)
    if a(i) == 3
    count = count + 1;
    end
end
toc
count
if count >= 0.2 * length(a)
    display("Ai papy chulo!")
end