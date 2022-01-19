from brownie import accounts, FundMe, network
from scripts.helpful_scripts import get_account

def deploy_simple_storage():
  account = get_account()
  fund_me = FundMe.deploy({"from": account})
  print(f"Contract deployed to {fund_me.address}")

def main(): 
    deploy_simple_storage() 