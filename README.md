# Getting started


## Clone from git 

Repo: https://github.com/ixianslab/srh-data-science


## Build conda environment

Run the command `conda env create -f environment.yml` to install the conda env named `srh`.


## Development of new content

### Git branches 
We work with branches. Our naming convention for a branch is `kapitel_XXX_name`. 

### Folder structure
Add new folders such as `Kapitel_CLT` in the `./notebooks` folder so that we get a structure such as 

The repository should have the following structure:

    repo-name
    ├── _experimental        # Stuff that never made it but is too valuable to be deleted ;-)   
    ├── .git                 # Git internals, don't mess around here.
    ├── .gitignore           # Specifies files and folders that should be ignored by git.
    ├── requirements.yml     # The requirements file for reproducing the analysis environment. 
    ├── notebooks            # Find all Jupyter notebooks here.
    │   └── Kapitel_00       # Serves as a template. Copy and paste this folder to get staretd
    │   │   └── _img         # Rendered images/pdfs/videos within notebooks are placed here.
    │   └── Kapitel_xxx      # Any topic of interest
    │   │   └── _img         # Rendered images/pdfs/videos within notebooks are placed here.
    │   └── ...              # Find all Jupyter notebooks here.
    │       └── _img         # Rendered images/pdfs/videos within notebooks are placed here.│   
    ├── README.md            # README for using this project.
    ├── references           # Scientific papers, links, manuals, and all other explanatory materials.
    ├── reports              # Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures          # Generated graphics and figures to be used in reporting.
    └── src                  # Source code for use in this project.
        ├── __init__.py      # Makes src a Python module.
        └── notebook_env.py  # A file with basic settings when working with Jupyter notebooks.
