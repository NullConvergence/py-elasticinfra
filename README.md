# py-elasticinfrastructure
This small utilty indexes infrastructure metrics to elasticsearch.


It was created to gather infrastructure data from machine learning experiments, with a focus on GPU utilization and CPU temperature.
The inspiration comes from metricbeats, by Elastic, however, this module is written in Python and it is easier to customize (unfortunately some community beats for Elastic are outdated and hard to run).

## Install

```
$ pip install py-elasticinfrastructure 
```

## Run

There are two ways of running the project: (1) as an individual program, see [example.py](https://github.com/NullConvergence/py_metrics/blob/master/example.py) or (2) on a separate thread, part of a bigger project, see [example_multithread.py](https://github.com/NullConvergence/py_metrics/blob/master/example_multithread.py).


In order to run the project in the first case, you have to add a configuration JSON file (see [configs](https://github.com/NullConvergence/py_metrics/tree/master/configs)) and run:

```
$ python example.py --config=configs/<config-file>.json
```

An example config file is provided as [default](https://github.com/NullConvergence/py_metrics/blob/master/configs/default.json). 
Make sure you edit the elasticsearch host data before you run the project.

## Extend

You can add new metrics by adding a new file in the ```py_metrics/metrics``` folder and subclassing the BaseMetric.
Afterwards, you can add it to the ```__init__.py``` file and to the config.

## ELK Docker

In order to run the ELK stack in docker, see [docker-elk](https://github.com/deviantony/docker-elk).
The indexed data can be mined using Kibana.
