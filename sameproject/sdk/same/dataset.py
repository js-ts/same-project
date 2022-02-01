import yaml
import os
from urllib.parse import urlparse
import pandas as pd

def dataset(name, same_file = 'same.yaml'):
    """Imports the dataset based upon the env provided
       wrapper around pd.read_<file> and I/O APIs
    NOTE: curently tested for json,csv and ipfs
    """
    try:
      env_var = os.environ['SAME_ENV'] if os.environ['SAME_ENV'] != "" else "default"
    except:
      env_var = "default"
    with open(same_file, 'r') as file:
        same_variables = yaml.safe_load(file)

    parsed_url = urlparse(same_variables['datasets'][name][env_var])
    # If URL is an IPFS url, access it via the IPFS gateway
    if parsed_url.scheme == "ipfs":
      url = 'https://gateway.ipfs.io/ipfs/'+parsed_url.netloc+parsed_url.path
    else:
      url = same_variables['datasets'][name][env_var]
    filename, file_extension = os.path.splitext(url)
    
    extensions = {
      '.csv': 'read_csv',
      '.dta': 'read_stata',
      '.feather': 'read_feather',
      '.html': 'read_html',
      '.json': 'read_json',
      '.orc': 'read_orc',
      '.parquet': 'read_parquet',
      '.pickle': 'read_pickle',
      '.sas': 'read_sas',
      '.sav': 'read_spss',
      '.sql': 'read_sql',
      '.txt': 'read_fwf',
      '.xml': 'read_xml',
      ('.hdf', '.h4', '.hdf4', '.he2', '.h5', '.hdf5', '.he5'): 'read_hdf',
      ('.xlsx', '.ods'): 'read_excel',
    }
    
    for key, value in list(extensions.items()):
      if type(key) == tuple:
        for ext in key:
          extensions[ext] = value
        extensions.pop(key)
    reader = getattr(pd, extensions[file_extension])
    ds = reader(url)
    return ds