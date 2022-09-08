import time, string, requests, itertools, os

from urllib.parse import urlencode
from utils.api import *

class signerr:
    def __init__(self, proxy: str or None = None, count: int = 4) -> None:
        self.proxies  = {'http': f'http://{proxy}', 'https': f'http://{proxy}'} if proxy else None
        self.accounts = []
        self.keywords = get_keywords(count)
        os.system("cls" if os.name == "nt" else "clear")
        
    def __base_params(self, keyword: str, cursor: int = 0) -> str:
        __to_encode = {
            "count"             : 30,
            "cursor"            : cursor,
            "keyword"           : keyword,
            "search_source"     : "report_user",
            "type"              : 1,
            "request_tag_from"  : "h5",
            "storage_type"      : 0,
            "iid"               : 7137816409338136325,
            "channel"           : "googleplay",
            "device_type"       : "SM-G973N",
            "device_id"         : 6990239216324986369,
            "os_version"        : 9,
            "version_code"      : 160904,
            "app_name"          : "musically_go",
            "device_brand"      : "samsung",
            "device_platform"   : "android",
            "aid"               : 1340,
        }
        return urlencode(__to_encode)
        
    def __base_headers(self, params: str) -> dict:
        sig = BSigner(
            params = params
        ).get_value()
        
        return {
            "accept-encoding"   : "gzip",
            "sdk-version"       : "2",
            "x-ss-req-ticket"   : str(int(time.time() * 1000)),
            "x-khronos"         : sig["X-Khronos"],
            "x-gorgon"          : sig["X-Gorgon"],
            "host"              : "api16-normal-c-useast1a.tiktokv.com",
            "connection"        : "Keep-Alive",
            "user-agent"        : "okhttp/3.10.0.1"
        }
        
    def main(self):
        cursor  = 0
        keyword = self.keywords
        __base_params = self.__base_params(keyword, cursor)
        headers = self.__base_headers(__base_params)
        print(headers)
        file = open("data/headers.txt", "a+")
        file.write(f"{headers}\n")
       
if __name__ == "__main__":
    signerr().main()
