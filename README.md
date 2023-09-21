# Retailing Billing App with Tkinter

Currently is a simple program made with Tkinter to demonstrate a graphical user interface in Python.

## Prerequisites

- Python 3.9
- Tkinter

## Installation

1. **Clone the repository** (If you have the code in a Git repository, otherwise skip this step):

   ```bash
   git clone https://github.com/davidcastagnetoa/billing-aplication-py.git
   cd billing-project
   ```

2. **Set up a virtual environment** (optional, but recommended):

   ```bash
   python -m venv venv
   ```

   - On Unix-based systems (Linux/macOS):

     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

3. **Create a .env file and add your APP gmail password**

   ```python
   EMAIL= "YOUR EMAIL" # Your GMail account email address here!
   PASSWORD="YOUR APP PASSWORD!"   # The app's password for that specific account
   ```

4. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Execution

Once everything is set up, you can run the application with:

```bash
python main.py
```

If you want to create a .exe file run the next command.

```bash
python setup.py bdist_msi
```
