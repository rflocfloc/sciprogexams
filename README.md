# Scientific Programming Exams

An exam database of the course Scientific Programming for Data Science and Quantitative and Computational Biology (University of Trento)


## How to

All the material is contained inside the ```docs``` folder. When it comes to add new exams to the repo these are the following steps:

### 1. Create exam folder

If folder/folders are **NOT** already present, create them, the structure and syntax is the following:

``` bash
.
├── docs
│   └── yyyy_mm_dd
│       ├── ds
│       └── qcb
└── lazy_template.md
```

 exams folders are name with **year_month_day** . All the material of the exam divided by course will be stored into docs/yyyy_mm_dd/{ds, qcb}/ .

### 2. Create markdown for webpage

Copy the ```lazy_template.md``` present in the ```docs``` folder to the wanted exam path and start modifying it: 

``` 
cp lazy_template.md yyyy_mm_dd/{ds, qcb}/web_page.md
```

### 3. Load and zip material

Load the exam material inside the ```ds``` or ```qcb``` folder (text, scripts and data necessary). Make sure to create also a ```solutions``` directory containing the solutions scripts inside the ```exam_material``` folder.
The structure of the exam material will result in something like:

```bash
.
├── docs
│   └── yyyy_mm_dd
│       ├── ds
│       │   ├── exam_material
│       │   │   ├── data
│       │   │   ├── exam.pdf
│       │   │   ├── exercise1.py
│       │   │   └── solutions
│       │   ├── exam_material.zip
│       │   └── web_page.md
│       └── qcb
│           ├── exam_material
│           │   ├── data
│           │   ├── exam.pdf
│           │   ├── exercise1.py
│           │   └── solutions
│           ├── exam_material.zip
│           └── web_page.md
└── lazy_template.md
```

Once the folder is ready zip it (convention is as ```exam_material.zip```). Add the relative path to the ```exam_material.zip``` inside the ```web_page.md``` file.

### 4. Make web page available

Add relative path to the ```web_page.md``` to the ```mkdocs.yml``` config file as a new entry of either Data Science or QCB specifying the wanted name for the menu (yy_mm_dd).

Here is an example of the ```mkdocs.yml```:

```yaml
site_name: ScientificProgramming Exams
site_url: https://rflocfloc.github.io/sciprogexams/
nav:
  - Home: index.md
  - Data Science:
     - 23_11_07: 2023_11_07/ds/web_page.md
     - 23_12_19: 2023_12_19/ds/web_page.md
  - QCB:
     - 23_12_19: 2023_12_19/qcb/web_page.md
     - 24_01_22: 2024_01_22/qcb/web_page.md

theme: readthedocs
```


### 4. Update the site

For updating the site you just need to push a new commit and GitHub Actions and Pages will handle the website building automatically.
