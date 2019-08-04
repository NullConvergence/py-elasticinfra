import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class Indexer:
    def __init__(self, config):
        self.config = config["elk"]["elastic"]
        self.index = self.config["index"]
        self.logger = config.get_logger("elk_logger")

    def connect(self):
        try:
            self.ex = Elasticsearch(self.config["host"])
        except Exception as exception:
            self.logger.error("[ERROR] \t Could not connect "
                              "to elasticsearch {}".format(self.config["host"]))
            raise exception
        else:
            if self.ex is None:
                self.logger.error("[ERROR] \t Could not connect "
                                  "to elasticsearch {}".format(self.config["host"]))
                raise "Could not connect to elasticsearch"
            else:
                self.logger.info("[INFO] \t Successfully connected "
                                 "to es")

    def index_bulk(self, metrics):
        try:
            bulk(self.ex, self._prepare_index(metrics))
        except Exception as exception:
            self.logger.error("[ERROR] \t Could not index "
                              "bulk to elasticsearch {}".format(exception))
        else:
            self.logger.info("[INFO] \t Indexed bulk in es.")

    def _prepare_index(self, metrics):
        for met in metrics:
            yield{
                "_index": self.index["name"],
                "_source": met
            }

    def _check_connection(self):
            # TODO: decide on other connection checks
            # e.g. es.cluster.health()
        if not self.ex:
            return False

    def create_index(self, index=None, config=None):
        if index is None:
            index = self.index["name"]
        if config is None:
            config = self.index["config"]
        try:
            json_config = json.dumps(config, indent=4)
            self.ex.indices.create(index=index,
                                   body=json_config,
                                   ignore=400)
        except Exception as exception:
            self.logger.error("[ERROR] \t Could not create es "
                              " index {}".format(exception))
            raise exception
        else:
            self.logger.info("[INFO] \t Index successfully checked.")
