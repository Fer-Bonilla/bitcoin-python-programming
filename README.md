# bitcoin python programming examples

Some blockchain coding examples with python running on the bitcoin testnet

## Dependencies

This python scripts uses these libraries:

- **Click**

  Used to handle the command line commands
  
  Install: pip install click
  
  URL: [https://palletsprojects.com/p/click/](https://palletsprojects.com/p/click/)

- **bitcoin-utils**
  
  Python base bitcoin utility function to create address, transactions and scripts for Bitcoin
  
  Install: pip install bitcoin-utils
  
  URL: [https://github.com/karask/python-bitcoin-utils](https://github.com/karask/python-bitcoin-utils)

## Program 1

This code create a P2sH address with a lock time script from a utx transaction:

- Accept a public key for the P2PKH part of the redeem script
- Accept a future time expressed in block height
- The P2SH address might have received funds from multiple transactions
- Multiple transactions require sing of all them
- Display the P2SH address


## Program 2

This code uses a redem script to claim the funds locked with the program 1

- Accept a future time (expressed in block height) and a private key; to recreate the redeem script as above and also use to unlock the P2PKH part
- Accept a P2SH address to get the funds from (the one created by the first script - this could be recreated but we want to pass to double check it!)
- Check if the P2SH address has any UTXOs to get funds from
- Accept a P2PKH address to send the funds to
- Calculate the appropriate fees with respect to the size of the transaction
- Send all funds that the P2SH address received to the P2PKH address provided
- Display the raw unsigned transaction
- Sign the transaction
- Display the raw signed transaction
- Display the transaction id
- Verify that the transaction is valid and will be accepted by the Bitcoin nodes
- If the transaction is valid, send it to the blockchain





## Sources and references



