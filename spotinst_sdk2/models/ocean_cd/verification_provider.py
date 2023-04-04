import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"


class Prometheus:
    """
    # Arguments
    address : str
    """

    def __init__(
            self,
            address: str = none):
        self.address = address


class Datadog:
    """
    # Arguments
    address : str
    api_key : str
    app_key : str
    """

    def __init__(
            self,
            address: str = none,
            api_key: str = none,
            app_key: str = none):
        self.address = address
        self.api_key = api_key
        self.app_key = app_key


class NewRelic:
    """
    # Arguments
    account_id : str
    base_url_nerd_graph : str
    base_url_rest : str
    personal_api_key : str
    region : str
    """

    def __init__(
            self,
            account_id: str = none,
            base_url_nerd_graph: str = none,
            base_url_rest: str = none,
            personal_api_key: str = none,
            region: str = none):
        self.account_id = account_id
        self.base_url_nerd_graph = base_url_nerd_graph
        self.base_url_rest = base_url_rest
        self.personal_api_key = personal_api_key
        self.region = region


class CloudWatch:
    """
    # Arguments
    iam_arn : str
    """
    def __init__(
            self,
            iam_arn: str = none):
        self.iam_arn = iam_arn


class VerificationProvider:
    """
    # Arguments
    name : str
    cluster_ids : List[str]
    prometheus : Prometheus
    datadog : Datadog
    newRelic : NewRelic
    cloudWatch : CloudWatch
    created_at : str
    updated_at : str
    """

    def __init__(
            self,
            name: str = none,
            cluster_ids: List[str] = none,
            prometheus: Prometheus = none,
            datadog: Datadog = none,
            new_relic: NewRelic = none,
            cloud_watch: CloudWatch = none,
            created_at: str = none,
            updated_at: str = none):
        self.name = name
        self.cluster_ids = cluster_ids
        self.prometheus = prometheus
        self.datadog = datadog
        self.new_relic = new_relic
        self.cloud_watch = cloud_watch
        self.created_at = created_at
        self.updated_at = updated_at


class VerificationProviderRequest:
    """
    # Arguments
    verification_provider : VerificationProvider
    """
    def __init__(self, verification_provider: VerificationProvider):
        self.verification_provider = verification_provider

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
