# An Introduction to Version Control Systems with Git

<!-- .slide: class="section-title" data-background="/lib/images/section-bkg.png" -->

-###-

##  Version Control Systems

* Version control systems record changes to a file or set of files over time so that you can recall specific versions later
* Many systems have risen to popularity over the years
    * RCS
    * CVS
    * Subversion
* We will focus on Git

-###-

##  Why use Version Control?

* These systems help with:
    * Tracking changes
    * Short and long term undo
    * Backup and restore
    * Synchronization
    * Collaboration

-###-

## Local Version Control Systems

![Local Version Control Systems](images/git/local-vcs.png)
<!-- .element: class="img_height" -->

-###-

## Centralized Version Control Systems

![Centralized Version Control Systems](images/git/central-vcs.png)
<!-- .element: class="img_height" -->

-###-

## Distributed Version Control Systems

![Distributed Version Control Systems](images/git/distributed-vcs.png)
<!-- .element: class="img_height" -->

-###-

## The basic Git workflow

* Modify files in your working directory
* Stage the files, adding snapshots to your staging area
* Commit your changes to your local copy of the repository

-###-

## The basic Git workflow

![Basic Git Workflow](images/git/workflow.png)
<!-- .element: class="img_height" -->

-###-

## The lifecycle of a file in Git

* Git does not necessary keep track of all files in your working directory

![Git File Lifecycle](images/git/lifecycle.png)
<!-- .element: class="img_height" -->

-###-

## Example repository

![Git Sample Repo](images/git/sample-repo.png)
<!-- .element: class="img_height" -->

-###-

## Gitting started

* Set your identity
    * `$ git config --global user.name "Jane Doe"`
    * `$ git config --global user.email "jdoe@example.com"`
* Set other configuration options
    * `$ git config --global color.ui true`
* Get help
    * `$ git help <verb>`

-###-

## Creating a new repository

* `$ git init`
* Creates a new (empty) repository in the current directory

-###-

## Copying a repository

* For this class, your instructor will create a repository for you, you will just need to copy it from GitHub to your computer using the following command:
    * `$ git clone <repository>`
    * Creates a copy of *repository* in the current directory

-###-

## Staging Files

* As you work, you will create new files and modify existing files, when you are satisfied with your changes, you can stage them for commit with:
    * `$ git add <file_pattern>`

-###-

## Committing changes

* *Commits* create a new version in the repository
* Include a commit message describing the new version
* `$ git commit -m msg`

-###-

## Checking working directory status

* `$ git status`
* Reports:
    * Files in the working directory that are not tracked
    * File modifications not yet staged for commit
    * File additions and modifications staged for commit

-###-

## Overviewing commit history

* `$ git log`
* Lists commits made to the current repository

-###-

## Handy command - comparing versions

* It may be handy to see exactly how files changed
    * `$ git diff`
    * Shows modifications not yet staged for commit
* `$ git diff <commit_id>`
    * Show changes since the commit specified
* `$ git diff <commit_id_1> <commit_id_2>`
    * Show changes between two commits

-###-

## What we've covered here...

* We've barely scratched the surface. Additional commands:
    * branching
    * rebasing
    * tagging
    * ...
* Further resources:
    * <https://git-scm.com/book/en/v2>
    * <http://gitref.org/>
    * <http://gitimmersion.com/>
