from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.refdata.instruments import InstrumentData
nubra = InitNubraSdk(NubraEnv.UAT)
instruments = InstrumentData(nubra)

df = instruments.get_instruments_dataframe()

nifty_options = df[(df['asset'] == 'NIFTY') & (df['exchange'] == 'NSE')]
print(nifty_options[['ref_id', 'stock_name', 'strike_price', 'option_type']].head())


