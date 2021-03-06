# QCFractal Pre-built Conda Environments

The QCFractal program has few requirements on its own `meta.yaml` file, however,
you may want to emulate the server side of things on your own. To help make that 
possible, we have provided the various YAML files here which can be used 
to quickly and mostly automatically build a working environment for to emulate 
the server. 

These use the `conda env create` commands (examples below) instead of the 
more common `conda create` (the commands are slightly different as of writting, 
circa Conda 4.3), so note the difference in commands.

## Requirements to use Environments

1. `git`
2. `conda`
3. `conda` installed `pip` (pretty much always available unless you are in 
   some custom Python-less Conda environment such as an `R`-based env.)
4. Network access

## Setup/Install

Run the following command to configure a new environment with the replacements:

* `{name}`: Replace with whatever you want to call the new env
* `{file}`: Replace with target file

```bash
conda env create -n {name} -f {file}
```

To access the new environment:
```bash
conda activate {name}
```

## Manifest and file differences

* `openff.yaml`: [Open Force Field Initiative](http://openforcefield.org/) workflow integrated environment
    * [Fireworks-based](https://materialsproject.github.io/fireworks) Workflows
    * [MongoDB](https://www.mongodb.com/) management
    * [Dask](http://dask.pydata.org/en/latest/) distribution engine
    * **Recomended**
* `fireworks.yaml`: Fireworks based workflow for QCFractal
    * Same as `openff.yaml` without additional workflow components
    * Minimal recommendation to run examples
* `dask.yaml`: Minimal structure using Dask and Mongodb
    * Minimal
    * Does NOT include fireworks
* `parsl.yaml`: Minimal structure using Parsl and Mongodb
    * Minimal
    * Does NOT include fireworks

