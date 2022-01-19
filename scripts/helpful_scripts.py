from brownie import network, config, accounts, MockV3Aggregator 
from web3 import Web3


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
      return accounts.load("stu-account")

def deploy_mocks():
   print(f"The active netowrk is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
      MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": get_accout()})
    #use the most recently deployed MockV3Aggregator