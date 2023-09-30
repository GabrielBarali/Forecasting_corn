# Carregue a biblioteca readr para leitura do CSV
library(readr)

# Leia os dados do CSV (substitua 'seu_arquivo.csv' pelo caminho real do arquivo)
dados <- read_csv('C:\\Tera\\Projeto\\data\\milho-cepea_RS_2.csv', col_types = cols(date = col_date(format = "%d-%m-%Y")))

# Crie uma série temporal com frequência de 252
serie_temporal <- ts(dados$RS, frequency = 252)

# Carregue a biblioteca forecast para usar auto.arima
library(forecast)

model_sarima = auto.arima(serie_temporal,
                          stepwise=FALSE,
                          approximation=FALSE,
                          seasonal=TRUE, # This will extent to SARIMA
                          allowdrift=FALSE, 
                          parallel = FALSE,  # speeds up computation, but tracing not available
                          trace=TRUE)

summary(model_sarima)