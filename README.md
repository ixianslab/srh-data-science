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
        
## Build a jupyter book
In order to build a jupyter book run the folloing command:

`jupyter-book build mybookname/` 

Make sure that you are in the right directory so that `mybookname/` yields to the place where the `_config.yml` and `_toc.yml` are found. E.g., in our case with the folder structure as outlined above and given that the working directory you are in is `repo-name/`, then the command to fire up the build of `Kapitel_00` is `jupyter-book build notebooks/Kapitel_00/`. Then, after the successful build you find the hmtl files in `repo-name/notebooks/Kapitel_00/_build/html/`
 
## Push to repo
`ghp-import -n -p -f notebooks/_build/html`

## Published at...

https://ixianslab.github.io/srh-data-science/intro.html