from brownie import accounts, FundMe, network

def deploy_simple_storage():
  account = get_account()
  # account = accounts.load("stu-account")
  # print(account)
  fund_me = FundMe.deploy({"from": account})
  stored_value = fund_me.retrieve()
  transaction = fund_me.store(15, {"from": account})
  transaction.wait(1)
  updated_stored_value = fund_me.retrieve()
  print(updated_stored_value)


def main(): 
    deploy_simple_storage() 