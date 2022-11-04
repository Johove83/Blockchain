# PyChain Ledger
### Johnathan Overton


## Overview of the Analysis

* The purpose of this file is to demonstrate the ability to create, modify, and deploy a blockchain ledger so as to accept sender, receiver, and amount data and encode this data with a unique hash identifier in order to ensure trust and security in completing financial transactions.

* In this model, the following technologies were incorporated:
  * Jupyterlab Notebook
  * Pandas
  * Streamlit
  * Dataclasses
  * Typing
  * Datetime
  * Hashlib

* How to Use
  * Simply clone the repository and execute streamlit run./pychain.py

* PyChain Ledger process stages
  * Create a Record Data Class
  * Modify the Existing Block Data Class to Store Record Data
  * Add Relevant User Inputs to the Streamlit Interface
  * Test the PyChain Ledger by Storing Records

## Results

### Record Dropdown Box Functionality

![1](https://github.com/Johove83/Blockchain/blob/main/Pychain%20Challenge/images/dropdownpychain.png)

![2](https://github.com/Johove83/Blockchain/blob/main/Pychain%20Challenge/images/godsendpychain.png)

As seen, on the Streamlit sidebar, the difficulty of the blockchain can be set. The first image shows that Block records can be selected, individually, from the drop down box. 

The following image shows the results of selecting a record. In this case, we find the record with all data attributes as well as the previous hash supplied for proof of work.

### PyChain Validation

![3](https://github.com/Johove83/Blockchain/blob/main/Pychain%20Challenge/images/validity.png)

The above image demonstrates the interfaces ability to store records, in a chain and to display these records via pandas dataframe. Most importantly, the "Validate Chain" button is able to compare the "prev_hash" stored in a block to the block before to ensure that the chain has not been interrupted with inconsistencies.



## Summary

This proof of concept has easily demonstrated pychain functionality in receiving information, hashing that information, and building a valid chain to ensure the highest order of trustworthiness, security, and functionality.
