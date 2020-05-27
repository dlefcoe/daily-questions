
# imports
from trading_ig import IGService
from trading_ig.config import config


ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig_service.create_session()

account_info = ig_service.switch_account(config.acc_number, False) # not necessary
print(account_info)

open_positions = ig_service.fetch_open_positions()
print("open_positions:\n%s" % open_positions)

print("")

epic = 'CS.D.EURUSD.MINI.IP'
resolution = 'D'
num_points = 10
response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, resolution, num_points)
df_ask = response['prices']['ask']
print("ask prices:\n%s" % df_ask)



