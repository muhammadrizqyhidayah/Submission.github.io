# Cara install library
pip install streamlit
pip install pandas
pip install matplotlib
pip install seaborn

# Setup Environment - Anaconda

```sh
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

# Setup Environment - Shell/Terminal

```sh
mkdir dashboard
cd dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```
# Run Streamlit langsung python
python -m streamlit run dashboard/dashboard.py 

# Run Streamlit App

```sh
streamlit run dashboard.py
```



