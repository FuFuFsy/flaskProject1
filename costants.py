"""
This module contains costants that are been used inside the all repository
"""

# import datetime
# import os

# # COMPANY
# AAPL = "AAPL"


# # PATHS
# PROJECT_PATH = os.path.abspath(".")
# PLOTS_FOLDER = os.path.join(PROJECT_PATH, "plots")
# DATA_FOLDER = os.path.join(PROJECT_PATH, "data")


# STOCK_DATA_CSV = os.path.join(
#     DATA_FOLDER, "stock_data.csv")
# COVID_DATA_CSV = os.path.join(
#     DATA_FOLDER, "covid_data.csv")
# TECHNICAL_INDICATORS_CSV = os.path.join(
#     DATA_FOLDER, "technical_indicators.csv")
# ECONOMIC_INDICATORS_CSV = os.path.join(
#     DATA_FOLDER, "economic_indicators.csv")

# STOCK_DATA_CSV = "stock_data.csv"
# COVID_DATA_CSV = "covid_data.csv"
# TECHNICAL_INDICATORS_CSV = "technical_indicators.csv"
# ECONOMIC_INDICATORS_CSV = "economic_indicators.csv"


# # DATES
# START_DATE = datetime.date(2017, 4, 1)
# END_DATE = datetime.date(2022, 4, 30)

# TEST_START_DATE = datetime.date(2022, 4, 30)
# TEST_END_DATE = datetime.date(2022, 6, 1)


# DATABASE
CLUSTER_NAME = "Cluster0"


DATABASE_NAME = "security"


# COLLECTION_STOCK_DATA = "stock_data"
# COLLECTION_COVID_DATA = "covid_data"
# COLLECTION_TECHNICAL_INDICATORS = "technical_indicators"
# COLLECTION_ECONOMIC_INDICATORS = "economic_indicators"
# COLLECTION_TEST_DATA = "test_data"
#COLLECTION_ARDUINO_TEST = "test-arduino"
# COLLECTION_ORDER="orders"
# COLLECTION_STOCKPREDICT_HSI="Share_HSI"
# COLLECTION_STOCKPREDICT_A="share_predict_000547"
COLLECTION_MESSAGE="message"

# COLLECTIONORDER = [COLLECTION_STOCKPREDICT_HSI]
# COLLECTIONA=[COLLECTION_STOCKPREDICT_A]
COLLECTIONMESS = [COLLECTION_MESSAGE]

# LOCAL_STORING_FILE_NAMES = {
#     COLLECTION_STOCK_DATA: STOCK_DATA_CSV,
#     COLLECTION_COVID_DATA: COVID_DATA_CSV,
#     COLLECTION_TECHNICAL_INDICATORS: TECHNICAL_INDICATORS_CSV,
#     COLLECTION_ECONOMIC_INDICATORS: ECONOMIC_INDICATORS_CSV
# }


# # SCRAPING
# DICT_SCRAPING_DATA = {
#     # FUNDAMENTAL INDICATORS
#     'pe_ratio': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=id%3Ape_ratio%2Cinclude%3Atrue%2C%2C&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AAAPL%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",  # &maxPoints=515
#     'market_cap': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=id%3Amarket_cap%2Cinclude%3Atrue%2C%2C&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AAAPL%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'ps_ratio': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=id%3Aps_ratio%2Cinclude%3Atrue%2C%2C&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AAAPL%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     # EXCHANGE RATES
#     'usd_can': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSDCDENK%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'usd_gbp': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSDPSER%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'usd_japan': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSDJYENK%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'usd_china': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSDCYENK%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     # GENERAL MACROECONOMIC INDICATORS
#     'usd_euro': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSDEER%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'csi': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSCS%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'usd_exports': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSEGS%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'industrial_production': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSIPI%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     # COMMODITIES
#     'gold': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AGPUSD%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator=",
#     'oil': "https://ycharts.com/charts/fund_data.json?annotations=&annualizedReturns=false&calcs=&chartType=interactive&chartView=&correlations=&dateSelection=range&displayDateRange=false&displayTicker=false&endDate=&format=real&legendOnChart=false&note=&partner=basic_2000&quoteLegend=false&recessions=false&scaleType=linear&securities=id%3AI%3AUSCOFPP%2Cinclude%3Atrue%2C%2C&securityGroup=&securitylistName=&securitylistSecurityId=&source=false&splitType=single&startDate=&title=&units=false&useCustomColors=false&useEstimates=false&zoom=max&redesign=true&chartCreator="
# }


# # OTHER COSTANTS
# COVID_VARIABLES = ['id', 'date', 'vaccines', 'tests', 'confirmed', 'recovered', 'deaths',
#                   'hosp', 'vent', 'icu']

# SEPARATOR = "\t"


# # COLUMNS TO REMOVE
# COLUMNS_TO_REMOVE = {
#     "covid_data": ["Recovered", "Confirmed"],
#     "stock_data": ["Open", "High", "Low", "Close"],
#     "technical_indicators": ["ema", "macd"],
#     "economic_indicators": ["ps_ratio"]
# }


# # OUTLIERS
# COVID_OUTLIERS = {
#     "New": ["2020-12-10"],
#     "Daily Deaths": ["2021-06-01",
#                      "2021-06-10",
#                      "2021-07-20",
#                      "2022-03-21",
#                      "2022-04-06"]
# }
