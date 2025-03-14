# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import logging
import os
from pathlib import Path
from typing import Any

import requests
from openapi_core import Spec, validate_request, validate_response
from openapi_core.contrib.requests import RequestsOpenAPIRequest, RequestsOpenAPIResponse

from manifests.test_manifest import TestManifest
from test_workflow.smoke_test.smoke_test_runner import SmokeTestRunner
from test_workflow.test_args import TestArgs
from test_workflow.test_result.test_component_results import TestComponentResults
from test_workflow.test_result.test_result import TestResult
from test_workflow.test_result.test_suite_results import TestSuiteResults


class SmokeTestRunnerOpenSearch(SmokeTestRunner):

    def __init__(self, args: TestArgs, test_manifest: TestManifest) -> None:
        super().__init__(args, test_manifest)
        logging.info("Entering Smoke test for OpenSearch Bundle.")

        # Below URL is for the pre-release latest. In the future may consider use formal released spec when available.
        self.spec_url = "https://github.com/opensearch-project/opensearch-api-specification/releases/download/main-latest/opensearch-openapi.yaml"
        self.spec_local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "smoke_tests_spec", "opensearch-openapi-local.yaml")
        self.spec_download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "smoke_tests_spec", "opensearch-openapi.yaml")
        self.spec_path = self.download_spec(self.spec_url, self.spec_local_path, self.spec_download_path)
        self.spec_ = Spec.from_file_path(self.spec_path)
        self.mimetype = {
            "Content-Type": "application/json"
        }

    def download_spec(self, url: str, local_path: str, download_path: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(download_path, "wb") as file:
                    file.write(response.content)
                    logging.info(f"Downloaded latest spec from {url}")
                    return download_path
            else:
                logging.info(f"Failed to fetch remote API spec, using local file: {local_path}")
                return local_path
        except requests.RequestException:
            logging.info(f"Could not reach {url}, using local file: {local_path}")
            return local_path

    def validate_request_swagger(self, request: Any) -> None:
        request = RequestsOpenAPIRequest(request)
        validate_request(request=request, spec=self.spec_)
        logging.info("Request is validated.")

    def validate_response_swagger(self, response: Any) -> None:
        request = RequestsOpenAPIRequest(response.request)
        response = RequestsOpenAPIResponse(response)
        validate_response(response=response, spec=self.spec_, request=request)
        logging.info("Response is validated.")

    def start_test(self, work_dir: Path) -> TestSuiteResults:
        url = "https://localhost:9200"

        all_results = TestSuiteResults()
        for component in self.test_manifest.components.select(self.args.components):
            if component.smoke_test:
                logging.info(f"Running smoke test on {component.name} component.")
                component_spec = self.extract_paths_from_yaml(component.name, component.smoke_test.get("test-spec"), self.version)
                logging.info(f"component spec is {component_spec}")
                test_results = TestComponentResults()
                for api_requests, api_details in component_spec.items():
                    request_url = ''.join([url, api_requests])
                    logging.info(f"Validating api request {api_requests}")
                    logging.info(f"API request URL is {request_url}")
                    for method in api_details.keys():  # Iterates over each method, e.g., "GET", "POST"
                        requests_method = getattr(requests, method.lower())
                        parameters_data = self.convert_parameter_json(api_details.get(method).get("parameters"))
                        header = api_details.get(method).get("header", self.mimetype)
                        logging.info(f"Parameter is {parameters_data} and type is {type(parameters_data)}")
                        logging.info(f"header is {header}")
                        status = 0
                        try:
                            response = requests_method(request_url, verify=False, auth=("admin", "myStrongPassword123!"), headers=header, data=parameters_data)
                            logging.info(f"Response is {response.text}")
                            self.validate_response_swagger(response)
                        except Exception as e:
                            status = 1
                            logging.error(f"Unexpected Error type is {type(e)}")
                            logging.error(e)
                            logging.info("Response is not validated. Please check the response output text above.")
                        finally:
                            test_result = TestResult(component.name, ' '.join([api_requests, method]), status)  # type: ignore
                            test_results.append(test_result)
                all_results.append(component.name, test_results)
        return all_results
