# Random-walk model with unequal latencies between response classes
nreps <- 1000
nsamples <- 2000
# Model parameters
drift <- 0.0
sdrw <- 0.3
criterion <- 3
t2tsd <- c(0.8, 0.0) # Variability in starting point and drift
# Preallocate memory
latencies <- rep(0, nreps)
responses <- rep(0, nreps)
evidence <- matrix(0, nreps, nsamples + 1)
# Simulation loop
for (i in 1:nreps) {
  sp <- rnorm(1, 0, t2tsd[1]) # Starting point variability
  dr <- rnorm(1, drift, t2tsd[2]) # Drift variability
  evidence[i, ] <- cumsum(c(sp, rnorm(nsamples, dr, sdrw)))
  p <- which( abs( evidence[i, ]) > criterion) [1]
  responses [ i ] <- sign( evidence[i ,p ])
  latencies [ i ] <- p
}
# p l o t up t o 5 random-walk p a t h s
tbpn <- min(nreps, 5)
plot(1 : max(latencies[ 1 : tbpn ]) + 10, type = 'n' , las = 1,
     ylim = c(- criterion - .5, criterion + .5) ,
     ylab = 'evidence' , xlab = 'decision time')
for (i in c(1:tbpn)) {
  lines(evidence[i, 1:(latencies[i]-1)])
}

abline(h=c(criterion, - criterion), lty = 'dashed')
"""
# Set up the plotting area to have two rows and one column
par(mfrow = c(2, 1))

# Top responses: latencies for positive responses
toprt <- latencies[responses > 0]
topprop <- length(toprt) / nreps

# Histogram for top responses
hist(toprt, 
     col = "gray",
     xlab = "Decision time", 
     xlim = c(0, max(latencies)), 
     main = paste(
       "Top responses (", as.numeric(topprop),") m = ", as.character(signif(mean(toprt), 4)),
       sep = ""), las = 1)

# Bottom responses: latencies for negative responses
botrt <- latencies[responses < 0]
botprop <- length(botrt) / nreps

# Histogram for bottom responses
hist(botrt, 
     col = "gray",
     xlab = "Decision time", 
     xlim = c(0, max(latencies)), 
     main = paste(
       "Bottom responses (", 
       as.numeric(botprop), 
       ") m = ", 
       as.character(signif(mean(botrt), 4)), 
       sep = ""
     ), 
     las = 1)
     