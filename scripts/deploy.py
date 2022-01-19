from brownie import accounts, FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account
from Web3 import Web3

def deploy_simple_storage():
  account = get_account()

  if network.show_active() != "development":
    price_feed_address = config["networks"][network.show_active()][
      "eth_usd_price_feed"
    ]
  else:
    print(f"The active netowrk is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
      MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": account})
    #use the most recently deployed MockV3Aggregator
    price_feed_address = MockV3Aggregator[-1].address

  fund_me = FundMe.deploy(
    price_feed_address,
    {"from": account},
    publish_source=config["networks"][network.show_active()].get("verify")
    )

 
  print(f"Contract deployed to {fund_me.address}")

def main(): 
    deploy_simple_storage() 