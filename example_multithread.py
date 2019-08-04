import argparse
import collections
import time
import threading
from py_elasticinfra.utils.parse_config import ConfigParser
from py_elasticinfra.elk.elastic import Indexer
from py_elasticinfra.runner import Runner


def foreground_thread():
    for i in range(5):
        time.sleep(3)
        print('[INFO] Foreground thread, iteration {}'.format(i+1))


def main(config):
        # connect to elasticsearch
    es = Indexer(config)
    es.connect()
    es.create_index()
    # initialize threads and run in parallel
    runner = Runner(config, es)
    thread_es = runner.run_background()
    thread_main = threading.Thread(name="foreground_thread",
                                   target=foreground_thread)
    thread_es.start()
    thread_main.start()


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="py_elasticinfra")
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
