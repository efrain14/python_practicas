import time  # importamos la biblioteca time
from tqdm import tqdm  # importamos la biblioteca tqdm

for i in tqdm(range(0,50), desc = "Procesando"): 
    time.sleep(0.1)
