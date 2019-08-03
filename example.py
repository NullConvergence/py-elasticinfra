import argparse
import collections
import time
from py_metrics.utils.parse_config import ConfigParser
from py_metrics.elk.elastic import Indexer
from py_metrics.run import Runner


def main(config):
    # connect to elasticsearch
    es = Indexer(config)
    es.connect()
    es.create_index()
    # initialize and run in loop
    runner = Runner(config, es)
    runner.loop()


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="py_metrics")
    args.add_argument("-c", "--config", default=None, type=str,
                      help="config file path (default: None)")
    # custom cli options to modify configuration
    # from default values given in json file.
    custom_args = collections.namedtuple("custom_args", "flags type target")
    options = [
        custom_args(["--elk", "--elk_host"], type=str,
                    target=("elk", "host"))
    ]
    config = ConfigParser(args, options)
    main(config)
