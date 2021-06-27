# algoPyCreateAccount
Algorand Blockchain using Python to create account on TestNet

Inspired by original tutorial here: 

https://developer.algorand.org/tutorials/create-account-testnet-python/

To fund accounts on TestNet go here for free algos:
https://bank.testnet.algorand.network/


## Install Python 3
Go here and install python 3 for Win, Mac or Linux here: 

https://www.python.org/downloads/

## Setting Python Path
```bash
# Mac, Linux
export PATH=”$PATH:/usr/local/bin/python”
```

Windows 10 is more complicated.

- Go into "Run" prompt and enter "**sysdm.cpl**"
- This should open up the **System Properties** window. Go to the **Advanced** tab and click the **Environment Variables** button.
- In the **System variable** window, find the **Path** variable and click **Edit**:
- Position your cursor at the end of the **Variable** **value** line and add the path to the **python.exe** file, preceded with the semicolon character (**;**). 
- Example:
  -  **;C:\Python\Python39**


## Change to Target Directory
```bash
# Mac, Linux and Windows
cd <your target dir>
```

## Clone Repo
```bash
# Mac, Linux and Windows
git clone https://github.com/csalinasonline/algoPyCreateAccount.git
```

## Change to Repo Directory
```bash
# Mac, Linux and Windows
cd algoPyCreateAccount
```

## Run Pip
```bash
# Mac, Linux and Windows
pip install -r requirements.txt
```

## Activating a Virtual Environment
```bash
# Mac and Linux
source env/bin/activate

# windows
.\env\Scripts\activate

# find Mac or Linux python interpeter
which python
.../env/bin/python

# ... on Windows
where python
.../env/bin/python.exe
```

## Run program
```bash
# Mac, Linux and Windows
python main.py
```
If all went well we should see console account info and a text file with account info.

```bash
Copy off accounts above and add TestNet Algo funds using the TestNet Dispenser at https://bank.testnet.algorand.network/ copy off the following mnemonic code for use later

Account 12DH43BSEWVQZ2XSVKWFMS5SGFDHV5EBXDSFCQHCODCPXJYIOGL7WEOID6I
mnemonic1 = "swarm transfer border digital gather wage blouse knee frozen cart taxi balance festival helmet radio ill bicycle notice fade hungry stomach shiver kidney abstract bronze"

Account 2OLOCVXHXMOLOV4BN2FHXS23S46UWJIKFDVZJ2WL3KOSX3JFRMTJWYW2OIY
mnemonic2 = "sunny dismiss buffalo sponsor gentle goose fix assist wonder young tag thank exclude decade retire onion birth horse grace album slice armor sketch absorb cereal"

Account 3HDIBUPS7F66RW5IUOEUVS7XCFS56PO6DWK37AMKVWSALMOGCYMDHSUMG3A
mnemonic3 = "erosion appear subway planet pear follow diet twice only delay adult goddess clerk keep raise bind hurdle wire mass animal frequent among month absent time"

Account 4Y3NGZ2UELKRXIV2U2PV42CIV6VD3HTKPGRFEA2UVHEWJT364JHB4YM2MOA
mnemonic4 = "muffin actor candy juice carbon balcony stone street section rival alert little typical muscle legend gallery squirrel daring awake gaze poverty license decade about almost"

Saving account info to file.
```

## Deactivating the Virtual Environment
```bash
deactivate
```