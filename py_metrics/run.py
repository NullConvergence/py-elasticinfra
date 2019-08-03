import py_metrics.metrics as module_metric
import time


class Runner:
    def __init__(self, config, elastic, metrics=None):
        self.config = config
        self.es = elastic

        if metrics is None:
            self.metrics = [config.initialize(module_metric, met)
                            for met in config["metrics"]]
        else:
            self.metrics = metrics

    def loop(self):
        while True:
            self.run()

    def run(self, index=True):
        time.sleep(self.config['time'])
        bulk_results = [met.measure() for met in self.metrics]
        print(bulk_results)
        if index is True:
            return self.es.index_bulk(bulk_results)
        else:
            return bulk_results
