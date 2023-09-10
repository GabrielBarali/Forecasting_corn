import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import scipy.stats as stats
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def plot_series_line(data,
                     figsize_value=(20, 5),
                     linewidth_value=1,
                     fontsize_value=10,
                     grid=True,
                     legend_value=True,
                     title_value=False,
                     xlabel_value=False,
                     ylabel_value=False):
    """
    Plot the time series in a line graph

    Parameters:
    data:

    """
    data.plot(figsize=figsize_value,
              linewidth=linewidth_value,
              fontsize=fontsize_value,
              legend=legend_value)

    plt.grid(grid)

    if title_value:
        plt.title(title_value)
    if xlabel_value:
        plt.xlabel(xlabel_value, fontsize=fontsize_value)
    if ylabel_value:
        plt.ylabel(ylabel_value, fontsize=fontsize_value)
    plt.show()


def get_plot_seasonality(data,
                         model='additive',
                         period=None,
                         figsize_value=(20, 5)):

    seasonal = seasonal_decompose(data, model=model, period=period)
    fig = seasonal.plot()
    fig.set_size_inches(figsize_value)
    fig.tight_layout()
    plt.show()

    return seasonal


def get_QQ_plot(data):
    stats.probplot(data, dist='norm', plot=plt)
    plt.title('Normal QQ plot')
    plt.show


def get_density_plot(data,
                     title_value=False,
                     bins='auto'):
    sns.histplot(data, kde=True, stat="density", bins=bins)
    if title_value:
        plt.title(title_value)


def get_acf_plot(data,
                 alpha=None,
                 title_value=False,
                 lags=None,
                 figsize_value=(20, 5),
                 grid=True):

    fig = plot_acf(data, alpha=alpha, lags=lags)
    if title_value:
        plt.title(title_value)

    plt.ylabel('Autocorrelation value')
    plt.xlabel('Lags')
    fig.set_size_inches(figsize_value)
    plt.grid(grid)
    plt.show()


def get_pacf_plot(data,
                  alpha=None,
                  title_value=False,
                  lags=None,
                  figsize_value=(20, 5),
                  grid=True):

    fig = plot_pacf(data, alpha=alpha, lags=lags)
    if title_value:
        plt.title(title_value)

    plt.ylabel('Autocorrelation value')
    plt.xlabel('Lags')
    fig.set_size_inches(figsize_value)
    plt.grid(grid)
    plt.show()
