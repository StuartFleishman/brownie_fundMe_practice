from brownie import accounts, FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account

def deploy_simple_storage():
  account = get_account()

  if network.show_active() != "development":
    price_feed_address = config["networks"][network.show_active()][
      "eth_usd_price_feed"
    ]
  else:
    print(f"The active netowrk is {network.show_active()}")
    mock_aggregator = MockV3Aggregator.deploy(18, 200000000000000000000, {"from": account})
    price_feed_address = mock_aggregator.address

  fund_me = FundMe.deploy(
    price_feed_address,
    {"from": account})

 
  print(f"Contract deployed to {fund_me.address}")

def main(): 
    deploy_simple_storage() 