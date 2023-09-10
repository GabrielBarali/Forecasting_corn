import pandas as pd
import scipy.stats as stats
import statsmodels.tsa.stattools as stattools
import statsmodels.api as sm

import src.tera_project_charts as charts


def load_timeseries_csv(csv_path,
                        date_column):

    series = pd.read_csv(csv_path)
    series[date_column] = pd.to_datetime(series[date_column], dayfirst=True)
    series.set_index(date_column, inplace=True)

    return series


def test_normality(data, method='shapiro-wilk'):
    if method == 'shapiro-wilk':
        p_value = stats.shapiro(data)[1]
    if method == 'dagostino-pearson':
        p_value = stats.normaltest(data)[1]
    return p_value


def test_stacionarity(data):
    kpss = stattools.adfuller(data)
    return kpss[1]


def acf_info(data,
             alpha=None,
             title_value=False,
             lags=None,
             figsize_value=(20, 5),
             grid=True):

    charts.get_acf_plot(data, alpha, title_value, lags, figsize_value, grid)
    acf = sm.tsa.acf(data, alpha=alpha)
    return acf[0]


def pacf_info(data,
              alpha=None,
              title_value=False,
              lags=None,
              figsize_value=(20, 5),
              grid=True):

    charts.get_pacf_plot(data, alpha, title_value, lags, figsize_value, grid)
    pacf = sm.tsa.pacf(data, alpha=alpha)
    return pacf[0]
