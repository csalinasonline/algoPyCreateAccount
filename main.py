# ******************************************************************************
# Project               :   algoPyCreateAccount
# Filename              :   main.py
# Author                :   csali
# Origin Date           :   6/27/2021 
# License               :   MIT
# Notes                 :   Used example from
# https://developer.algorand.org/tutorials/create-account-testnet-python/ to
# create 4 accounts.
# ******************************************************************************

import json
from algosdk import account, mnemonic


def main():
    """
    Main hook

    """

    # create 4 accounts
    acct = account.generate_account()
    address1 = acct[1]
    mnemonic1 = mnemonic.from_private_key(acct[0])

    acct = account.generate_account()
    address2 = acct[1]
    mnemonic2 = mnemonic.from_private_key(acct[0])

    acct = account.generate_account()
    address3 = acct[1]
    mnemonic3 = mnemonic.from_private_key(acct[0])

    acct = account.generate_account()
    address4 = acct[1]
    mnemonic4 = mnemonic.from_private_key(acct[0])

    # account info to console
    print("")
    print("Copy off accounts above and add TestNet Algo funds using\
    the TestNet Dispenser at https://bank.testnet.algorand.network/")
    print("copy off the following mnemonic code for use later")
    print("")
    print("Account 1\n" + str(address1))
    print("mnemonic1 = \"{}\"\r\n".format(mnemonic1))
    print("Account 2\n" + str(address2))
    print("mnemonic2 = \"{}\"\r\n".format(mnemonic2))
    print("Account 3\n" + str(address3))
    print("mnemonic3 = \"{}\"\r\n".format(mnemonic3))
    print("Account 4\n" + str(address4))
    print("mnemonic4 = \"{}\"\r\n".format(mnemonic4))

    # save accounts to file for later
    print("Saving account info to file.")
    file = open('ACCOUNT_INFO.txt', 'w')
    file.write("Copy off accounts above and add TestNet Algo funds using"
               " the TestNet Dispenser at https://bank.testnet.algorand.network/"
               " and copy off the following mnemonic code for use later\r\n")
    file.write("Account Info:\r\n")
    file.write("Account 1 = " + str(address1))
    file.write("\r\nmnemonic1 = \"{}\"\r\n".format(mnemonic1))
    file.write("Account 2 = " + str(address2))
    file.write("\r\nmnemonic2 = \"{}\"\r\n".format(mnemonic2))
    file.write("Account 3 = " + str(address3))
    file.write("\r\nmnemonic3 = \"{}\"\r\n".format(mnemonic3))
    file.write("Account 4 = " + str(address4))
    file.write("\r\nmnemonic4 = \"{}\"\r\n".format(mnemonic4))
    file.close()


if __name__ == "__main__":
    main()
