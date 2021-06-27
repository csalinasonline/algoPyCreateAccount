# algoPyCreateAccount
Algorand Blockchain using Python to create account on TestNet

Inspired by original tutorial here: 

https://developer.algorand.org/tutorials/create-account-testnet-python/


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

## Change Repo Directory
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



## Deactivating the Virtual Environment
```bash
deactivate
```