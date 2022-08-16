#! /usr/bin/python3

import re
import typing

import requests
from bs4 import BeautifulSoup


class GoogleForm:
    __regex_pattern = re.compile(r'(?<=\[\[)(\d+)')
    __headers = {}
    __params = {}

    def __init__(self, url: str, answers: str, headers: typing.Dict[str, str] = {}, params: typing.Dict[str, str] = {}):
        self.__view_form_url = url
        self.__form_response_url = url.replace('viewform', 'formResponse')
        self.__answers = answers
        self.__set_headers(headers)
        self.__set_params(params)

    def __set_headers(self, headers: typing.Dict[str, str]):
        if headers:
            self.__headers = headers
        else:
            self.__headers = {
                'Host': 'docs.google.com',
                'Content-Length': '0',
            }

    def __set_params(self, params: typing.Dict[str, str]):
        if params:
            self.__params = params
        else:
            for q, a in zip(self.get_all_entry_ids(self.__view_form_url), self.__answers):
                self.__params[q] = a

    @classmethod
    def get_all_entry_ids(cls, url: str, prefix=False) -> typing.List[str]:
        form_html = requests.get(url)
        dom = BeautifulSoup(form_html.text, 'html.parser')
        questions = dom.find_all('div', attrs={'data-params': True})
        entry_ids = []

        for question in questions:
            entry_ids.append(
                ("entry." if prefix else "") +
                re.search(cls.__regex_pattern, str(question)).group(0)
            )

        return entry_ids

    def set_headers(self, headers: typing.Dict[str, str]) -> None:
        self.__set_headers(headers)

    def set_params(self, params: typing.Dict[str, str]) -> None:
        self.__set_params(params)

    def add_header(self, key: str, value: str) -> None:
        self.__headers[key] = value

    def add_param(self, key: str, value: str) -> None:
        self.__params[key] = value

    def send(self) -> bool:
        request = requests.post(
            url=self.__form_response_url,
            params=self.__params,
            headers=self.__headers
        )

        return True if request.status_code == 200 else False
