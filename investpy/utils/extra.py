# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pandas as pd
import pkg_resources

import random

from . import constant as cst


def resource_to_data(path_to_data):
    """
    This is an auxiliar function to read data from a given path, so as to wrap the load
    process of the static data files from investpy.

    Returns:
        :obj:`pandas.DataFrame` - data:
            This function returns a :obj:`pandas.DataFrame` object with all the static file's data
            retrieved from investpy.

    Raises:
        FileNotFoundError: raised if the static data file was not found.
        IOError: raised if the data file is empty or errored.

    """

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', path_to_data))
    if pkg_resources.resource_exists(resource_package, resource_path):
        data = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0115: data file not found or errored.")

    if data is None:
        raise IOError("ERR#0115: data file was empty or errored.")

    return data


def random_user_agent():
    """
    This function selects a random User-Agent from the User-Agent list, which is a constant
    variable that can be found at `investpy.utils.constant.USER_AGENTS`. User-Agents are used in
    order to avoid the limitations of the requests to Investing.com. The User-Agent is
    specified on the headers of the requests and is different for every request.

    Note that Investing.com, via changing the User-Agent on the headers of every request, allows
    a lot of requests, since it has been tested with over 10k consecutive requests without getting
    any HTTP error code from Investing.com.

    Returns:
        :obj:`str` - user_agent:
            The returned :obj:`str` is the name of a random User-Agent, which will be passed on the 
            headers of a request so to avoid restrictions due to the use of multiple requests from the 
            same User-Agent.
    
    """

    return str(random.choice(cst.USER_AGENTS))


def get_proxy(api_key):
    """
    This function passes the Zyte API key and retrieves a proxy that can be used to fetch data
    without IP BAN or limitation. This requires an active subscription with Zyte. 
    """
    proxy_host = "proxy.crawlera.com"
    proxy_port = "8010"
    proxy_auth = f"{api_key}:"
    proxies = {"https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
      "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
    
    return proxies
