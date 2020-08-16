from typing import Optional, List, Dict
from dataclasses import dataclass

@dataclass()
class ValidatorInfo():
    host: str
    grpc_port: int
    http_port: int
    pub_key: str

    def to_dict(self):
        return {'host': self.host, 'grpc_port':self.grpc_port, 'http_port':self.http_port, 'pub_key': self.pub_key}

@dataclass()
class Settings():
    DB_PATH: str
    TARGET_RNODE_HOST: str
    TARGET_RNODE_PORT: int
    TARGET_RNODE_HTTP_PORT: int
    USE_HTTPS: bool
    HOST: str
    PORT: int
    NUM_CORE: int
    LOG_PATH: str
    MAX_MEM: int
    CACHE_TTL: int
    validator_list: Optional[List[ValidatorInfo]]
    original_setting_dict: Dict

    @classmethod
    def parse_from_yaml(cls, settings):
        if settings.get('VALIDATOR_LIST'):
            validator_list = [ValidatorInfo(v['host'], v['grpc_port'], v['http_port'], v['pub_key']) for v in settings['VALIDATOR_LIST']]
        else:
            validator_list = None
        return cls(DB_PATH=settings['DB_PATH'],
                   TARGET_RNODE_HOST=settings['TARGET_RNODE_HOST'],
                   TARGET_RNODE_PORT=settings['TARGET_RNODE_PORT'],
                   TARGET_RNODE_HTTP_PORT=settings['TARGET_RNODE_HTTP_PORT'],
                   USE_HTTPS=settings['USE_HTTPS'],
                   HOST=settings['HOST'],
                   PORT=settings['PORT'],
                   NUM_CORE=settings['NUM_CORE'],
                   LOG_PATH=settings['LOG_PATH'],
                   MAX_MEM=settings['MAX_MEM'],
                   CACHE_TTL=settings['CACHE_TTL'],
                   validator_list=validator_list, original_setting_dict=settings)