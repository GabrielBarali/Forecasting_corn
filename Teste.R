# install.packages("forecast")
# install.packages("readr")
# install.packages("lubridate")

# Load the necessary libraries
library(forecast)
library(readr)      # For reading CSV data
library(lubridate)  # For date manipulation

# Set the path to your CSV file
data_path <- 'C:\\Tera\\Projeto\\data\\milho-cepea_RS.csv'  # Replace with your actual file path

# Read the CSV file into a data frame
data_frame <- read.csv(data_path, sep = ',', stringsAsFactors = FALSE)

# Convert the date column to Date class
data_frame$date <- dmy(data_frame$date)  # dmy() function for day-month-year format

# Create a time series object
time_series <- ts(data_frame$RS, start = min(data_frame$date), frequency = 252)

# Print the first few rows of the time series
head(time_series)


# Run the automatic SARIMA model selection
sarima_model <- auto.arima(time_series, seasonal = T)

# Print the selected SARIMA model details
print(summary(sarima_model))