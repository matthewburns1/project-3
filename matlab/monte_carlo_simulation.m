% Monte Carlo Simulation - Stock Price Paths
% Using Geometric Brownian Motion

clc;
clear; 

% Parameters
S0 = 100;
mu = 0.08;
sigma = 0.20;
dt = 1/252;
N = 252;
M = 10000;

% Initialize
paths = zeros(N+1, M);
paths(1, :) = S0;

% Simulate
for i = 1:N
    z = randn(1, M);
    growth = exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*z);
    paths(i+1, :) = paths(i, :) .* growth;
end

% Check
fprintf('First path first 5 values:\n');
disp(paths(1:5, 1));

% Final prices
final_prices = paths(end, :);

% Results
fprintf('Monte Carlo Results (%d simulations):\n', M);
fprintf('Initialize Price: $%.2f\n', mean(final_prices));
fprintf('Mean Final Price: $%.2f\n', mean(final_prices));
fprintf('Median Final Price: $%.2f\n', median(final_prices));
fprintf('5th Percentile (VaR): $%.2f\n', prctile(final_prices, 5));
fprintf('95th Percentile: $%.2f\n', prctile(final_prices, 95));
fprintf('Probability of Loss: %.2f%%\n', sum(final_prices < S0)/M*100);

% Plot sample paths
figure;
plot(paths(:, 1:100), 'Color', [0.7 0.71 0.3]);
hold on;
plot(mean(paths, 2), 'r', 'LineWidth', 2);
title('Monte Carlo Simulation - 100 Stock Price Paths');
xlabel('Trading Days');
ylabel('Stock Price ($)');
legend('Simulated Paths', 'Mean Path');
grid on;

% Save Figure
saveas(gcf, 'outputs/monte_carlo_paths.png');
fprintf('Chart saved!\n'); 