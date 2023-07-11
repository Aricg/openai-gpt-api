#!/usr/bin/env python

import logging
import os
import argparse

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import (
    RelevanceFilters,
    TimeFilters,
    TypeFilters,
    ExperienceLevelFilters,
    OnSiteOrRemoteFilters,
)

# Change root logger level (default is WARN)
logging.basicConfig(level=logging.INFO)

def sanitize_filename(s):
    """
    Sanitize a string to be used as a filename.
    """
    return "".join([c for c in s if c.isalpha() or c.isdigit()]).rstrip()

def on_data(data: EventData):
    print(
        '[ON_DATA]',
        data.title,
        data.company,
        data.company_link,
        data.date,
        data.link,
        data.insights,
        len(data.description),
    )

    # Create a directory for each company
    company_dir = os.path.join('jobs', sanitize_filename(data.company))
    os.makedirs(company_dir, exist_ok=True)

    # Create a file for each job in the respective company directory
    job_file = os.path.join(company_dir, sanitize_filename(data.title) + '.txt')

    # Check if the file already exists
    if not os.path.exists(job_file):
        with open(job_file, 'w') as f:
            # Write the link as the first line
            f.write(f"Job Link: {data.link}\n")
            f.write("\n")
            f.write("Job Description:\n")
            f.write(data.description)
    else:
        print(f'Job already exists: {job_file}')


def on_metrics(metrics: EventMetrics):
    print('[ON_METRICS]', str(metrics))


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


def main(limit):
    scraper = LinkedinScraper(
        chrome_executable_path=None,
        chrome_options=None,
        headless=True,
        max_workers=1,
        slow_mo=5,
        page_load_timeout=40,
    )

    # Add event listeners
    scraper.on(Events.DATA, on_data)
    scraper.on(Events.ERROR, on_error)
    scraper.on(Events.END, on_end)

    queries = [
        Query(
            query='devops',
            options=QueryOptions(
                locations=['Canada'],
                apply_link=True,
                skip_promoted_jobs=False,
                page_offset=0,
                limit=limit,
                filters=QueryFilters(
                    relevance=RelevanceFilters.RECENT,
                    time=TimeFilters.MONTH,
                    on_site_or_remote=[
                        OnSiteOrRemoteFilters.REMOTE,
                        OnSiteOrRemoteFilters.HYBRID,
                    ],
                    experience=[
                        ExperienceLevelFilters.MID_SENIOR,
                        ExperienceLevelFilters.ASSOCIATE,
                    ],
                ),
            ),
        ),
    ]

    scraper.run(queries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1, help="Set the limit for number of jobs")
    args = parser.parse_args()

    main(args.limit)

