from concurrent.futures import ThreadPoolExecutor, as_completed
from naukri import naukri
from internshala import internshala
from Timesjobs import timesjob
from Linkedin import linkedin
import time
import pandas as pd

def fetch_jobs(function, job_title, location, experience):
    return function(job_title, location, experience)

if __name__ == "__main__":
    # User input
    job_title = ['Data Science']
    location = ['Bangalore']
    experience = '3 years'
    job_listings = []

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(fetch_jobs, naukri, job_title, location, experience),
            executor.submit(fetch_jobs, internshala, job_title, location, '3'),
            executor.submit(fetch_jobs, timesjob, job_title, location, experience),
            executor.submit(fetch_jobs , linkedin , job_title, location , ['Entry level'])
        ]
        for future in as_completed(futures):
            job_listings.extend(future.result())

    end_time = time.time()
    print("Total Runtime:", end_time - start_time)
    print("Total Jobs Found:", len(job_listings))
    df = pd.DataFrame(job_listings)
    
    df.to_csv('data.csv', index=False)

    