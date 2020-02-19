# Lab 3 - Hands on DynamoDB

### Instructions

**Step 1:**
Start DynamoDB Server

$ dynamodb

**Step 2:**
Open another terminal.

$ git clone https://github.com/sanket143/DynamoDB-Lab

This will create a folder DynamoDB-Lab.

[DynamoDB Lab Template](https://github.com/sanket143/DynamoDB-Lab): Here is the boilerplate you'll be using.

Click on `Use this template` button on the repo to make a copy for you and clone it and you're good to go.

Your Directory Tree

```
.
├── data
│   ├── books
│   │   └── books.json
│   ├── devhub
│   │   ├── commits.json
│   │   ├── issues.json
│   │   ├── repositories.json
│   │   └── users.json
│   └── logs
│       └── web_access_log.json
├── finish.py
├── README.md
├── setup.py
└── soln
    ├── task1
    │   ├── q1.py
    │   ├── q2.py
    │   ├── q3.py
    │   ├── q4.py
    │   ├── q5.py
    │   ├── q6.py
    │   └── q7.py
    ├── task2
    │   ├── q1.py
    │   ├── q2.py
    │   ├── q3.py
    │   └── q4.py
    └── task3
        ├── q2.py
        ├── q3.py
        ├── q4.py
        ├── q5.py
        └── q6.py

8 directories, 25 files
```

Here you have three tasks!

In each task you are given a set of data files.
<span style="color: crimson !important">Before proceeding, understand structure of respective data files</span>

You'll be writing all your code in `q#.py` files and are suppose to submit compressed `soln/`

<div style="page-break-after: always;"></div>

## Task 1

**1. Create table `Books` for <span style="color: crimson !important">data/books/books.json</span> with following inputs**
  - Partition Key: Publisher
  - Sort Key: Title
  - Global Secondary Index: ISBN

**2. Add a book using `put item`**

**3. Add all the rest of the books using `batch write`**

**4. Get book <span style="color: crimson !important">Learning JavaScript Design Patterns</span> published by <span style="color: crimson !important">O'Reilly Media</span>**

**5. Get book with ISBN number <span style="color: crimson !important">9781491904244</span>**

**6. Update pages of book <span style="color: crimson !important">Git Pocket Guide</span> published by <span style="color: crimson !important">O'Reilly Media</span> to <span style="color: crimson !important">268</span>**

**7. List out book `titles` with `pages` with more than <span style="color: crimson !important">300</span> pages**

[DynamoDB Reference Codes](https://github.com/sanket143/DynamoDB-Lab/wiki/DynamoDB-Reference-Codes)

---

## Task 2

**1. Create a table `WebAccessLog` for <span style="color: crimson">data/logs/web_access_log.json</span> with following constraints:**

- Partition Key: `ipaddr`
- Sort Key: `req_no`


**2. Write script to perform batch writes with batch size of 25 items for all log items ( i.e 201 entries )**

**3. For IP address `188.45.108.168`, give count of requests that have not returned status `200`**

**4. For IP address `191.182.199.16`, give daily count of requests, and daily total data (size) downloaded**

---

<div style="page-break-after: always;"></div>

## Task 3

Here you are given a set of data files: Users, Repositories, Commits, Issues
under the directory [data/devhub]!

For creating required tables, you have been given a python script setup.py; you can run the script for creating all the required table. Schema information of tables is also given here for your information.

Setup Database
```shell
$ python setup.py # will do required changes
```

**Table Definitions**

**Users** <br>
- Primary Key: `email`

**Repositories**
- Partition Key: `name`
- Sort Key: `owner`
- Global Secondary Index: `repo_id-index`
  - Primary Key: `repo_id`

**Commits**
- Primary Key: `project_id`
- Sort Key: `sha`

**Issues**
- Partition Key: `title`
- Sort Key: `repo_id`
- Local Secondary Index: `reporter-index`
  - Partition Key: `title`
  - Sort Key: `reporter`

**1. Run setup and study the given data**

**2. List all pending issues for the repository `2048` (owner `janet`)**

**3. Find out the latest commit and its author of the repo `linux` which is owned by `torvalds`**

**4. Print list of issue reporters(`name`, `issue_title`) of the repo `toml-lang` owned by `github`**

**5. Run following update queries**

Add a new commit

```json
{
  "sha": "K9QTUE0U3SKDFFKFVP7PMTMQF6GZNEB8NSFH1K",
  "author": "lisa",
  "message": "Resolved an issue from pdf.js",
  "project_id": 4243,
  "timestamp": "2020-02-19T20:40:38Z"
}
```
Set the issue ( `repo-id` = `4243` and `title` = `No Documentation for installation` ) as resolved

**6. List commits (`author_name`) done by the member of
mozilla organization on repo name `pdf.js`**

At last, destroy all your tables so that others could have a cold start.

```shell
$ python finish.py
```
