from pytrends.request import TrendReq
import itertools

tzBR='-180'
pytrend = TrendReq(hl='en-US', tz=tzBR, timeout=(10,25))

df = pytrend.trending_searches(pn='brazil')
trends = list(itertools.chain.from_iterable(df.values.tolist()))
print(trends)
