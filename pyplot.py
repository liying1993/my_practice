import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y%m%d')})

    plt.plot_date(date, closep,'-', label='Price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


graph_data('TSLA')


# data = {
#     'a': np.arange(50),
#     'b': np.random.randint(0, 50, 50),
#     'd': np.random.randn(50)
# }
# data['b'] = data['a'] + 10*np.random.randn(50)
# data['d'] = np.abs(data['d'])*100
# plt.scatter('a','b',c='c',s='d',data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

# t = np.arange(0., 5., 0.2)#就是以0.为起点，以5.为末点，但是不包括5.，两个数之间的间距是0.2
# print(t)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.plot([1, 2, 3, 4],[1, 4, 9, 16], "ro")
# plt.axis([0,6,0,20])
# plt.ylabel("some numbers")
#
# plt.show()
