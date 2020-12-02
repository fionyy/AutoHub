# -*- coding: utf-8 -*-
# @Time : 2020/11/30 19:24 

# @Author : youding

# @File : wbrunner.py

# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from runner.baserunner import BaseRunner

class WbRunner(BaseRunner):

    def __init__(self, name="Webdriver Runner"):
        super().__init__(name=name)


    def remote_driver(self, command_executor='127.0.0.1:444/wd/hub',
                      desired_capabilities=None, browser_profile=None, proxy=None,
                      keep_alive=False, file_detector=None, options=None):

        return webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_capabilities,
                                browser_profile=browser_profile, proxy=proxy, keep_alive=keep_alive,
                                file_detector=file_detector, options=options)

    def chrome_driver(self, executable_path="chromedriver", port=0, options=None, service_args=None,
                      desired_capabilities=None, service_log_path=None, chrome_options=None, kee_alive=True):

        return webdriver.Chrome(executable_path=executable_path, port=port, options=options,
                                service_args=service_args, desired_capabilities=desired_capabilities,
                                service_log_path=service_log_path, chrome_options=chrome_options,
                                keep_alive=kee_alive)


    def firefox_driver(self, firefox_profile=None, firefox_binary=None, timeout=30,
                       capabilities=None, proxy=None, executable_path="geckodriver", options=None,
                       service_log_path="geckodriver.log", firefox_options=None,
                       service_args=None, desired_capabilities=None, log_path=None, keep_alive=True):

        return webdriver.Firefox(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                                 timeout=timeout, capabilities=capabilities, proxy=proxy,
                                 executable_path=executable_path, options=options, service_log_path=service_log_path,
                                 firefox_options=firefox_options, service_args=service_args, desired_capabilities=desired_capabilities,
                                 log_path=log_path, keep_alive=keep_alive)

    def ie_driver(self, executable_path="IEDriverServer.exe", capabilities=None,
                  port=0, timeout=30, host=None, log_lever=None, service_log_path=None,
                  options=None, ie_options=None, desired_capabilities=None, log_file=None,
                  keep_alive=False):

        return webdriver.Ie(executable_path=executable_path,capabilities=capabilities,
                            port=port, timeout=timeout, host=host, log_level=log_lever, options=options,
                            service_log_path=service_log_path, ie_options=ie_options, desired_capabilities=desired_capabilities,
                            log_file=log_file, keep_alive=keep_alive)


    def edge_driver(self, executable_path="MicrosoftWebDriver.exe", capabilities=None,
                    port=0, verbose=False, service_log_path=None, log_path=None, keep_alive=False):

        return webdriver.Edge(executable_path=executable_path, capabilities=capabilities, port=port, verbose=verbose, service_log_path=service_log_path,
                              log_path=log_path, keep_alive=keep_alive)


    def safafi_driver(self, executable_path="/usr/bin/safaridriver", reuse_service=False,
                      desired_capabilities=DesiredCapabilities.SAFARI,quiet=False,
                      keep_alive=True, service_args=None):

        return webdriver.Safari(executable_path=executable_path, reuse_service=reuse_service, desired_capabilities=desired_capabilities, quiet=quiet, keep_alive=keep_alive,
                                service_args=service_args)
