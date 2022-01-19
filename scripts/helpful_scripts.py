from brownie import network, config, accounts 


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
      return accounts.load("stu-account")