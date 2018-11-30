#!/usr/bin/env bash

pytest --alluredir="results"

allure serve results