import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.aws import *

class AwsElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_aws")

        self.mock_group_json = self.load_group_json()

    def create_formatted_group_request(self, group):
        group_request = ElastigroupCreationRequest(group)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/aws_group.json')) as group_json:
            return json.load(group_json)


# region Third Party Integrations
class AwsElastigroupTestEcsIntegration(AwsElastigroupTestCase):
    def runTest(self):
        ecs_auto_scale_down = EcsAutoScalerDownConfiguration(
            evaluation_periods=3)
        ecs_auto_scale_attribute = EcsAutoScalerAttributeConfiguration(
            key='the_key', value='the_value')
        ecs_auto_scale_headroom = EcsAutoScalerHeadroomConfiguration(
            cpu_per_unit=4096, memory_per_unit=4096, num_of_units=30)
        ecs_auto_scale = EcsAutoScaleConfiguration(
            is_enabled=True,
            is_auto_config=False,
            cooldown=900,
            headroom=ecs_auto_scale_headroom,
            down=ecs_auto_scale_down,
            attributes=[ecs_auto_scale_attribute])
        ecs = EcsConfiguration(
            cluster_name='test-ecs',
            auto_scale=ecs_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(ecs=ecs)

        group = Elastigroup(third_parties_integration=third_party_integrations)

        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['ecs']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['ecs']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestKubernetesIntegration(AwsElastigroupTestCase):
    def runTest(self):
        kubernetes_auto_scale_down = KubernetesAutoScalerDownConfiguration(
            evaluation_periods=5)
        kubernetes_auto_scale_headroom = KubernetesAutoScalerHeadroomConfiguration(
            cpu_per_unit=2000, memory_per_unit=4000, num_of_units=2)
        kubernetes_auto_scale = KubernetesAutoScalerConfiguration(
            is_enabled=True,
            cooldown=300,
            headroom=kubernetes_auto_scale_headroom,
            down=kubernetes_auto_scale_down,
            is_auto_config=False)
        kubernetes = KubernetesConfiguration(integration_mode='pod',
                                             cluster_identifier='test-k8s',
                                             auto_scale=kubernetes_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(
            kubernetes=kubernetes)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['kubernetes']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['kubernetes']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestNomadIntegration(AwsElastigroupTestCase):
    def runTest(self):
        nomad_down = NomadAutoScalerDownConfiguration(evaluation_periods=3)
        nomad_constraints = NomadAutoScalerConstraintsConfiguration(
            key='${node.class}', value='value')
        nomad_scale_headroom = NomadAutoScalerHeadroomConfiguration(
            cpu_per_unit=10, memory_per_unit=1000, num_of_units=2)
        nomad_auto_scale = NomadAutoScalerConfiguration(
            is_enabled=True,
            cooldown=180,
            headroom=nomad_scale_headroom,
            constraints=[nomad_constraints],
            down=nomad_down)
        nomad = NomadConfiguration(
            master_host="https://master.host.com",
            master_port=443,
            acl_token='123',
            auto_scale=nomad_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(nomad=nomad)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['nomad']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['nomad']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestDockerSwarmIntegration(AwsElastigroupTestCase):
    def runTest(self):
        docker_swarm_down = DockerSwarmAutoScalerDownConfiguration(
            evaluation_periods=4)
        docker_swarm_headroom = DockerSwarmAutoScalerHeadroomConfiguration(
            cpu_per_unit=1000000000, memory_per_unit=800000000, num_of_units=3)
        docker_swarm_auto_scale = DockerSwarmAutoScalerConfiguration(
            is_enabled=True,
            cooldown=300,
            headroom=docker_swarm_headroom,
            down=docker_swarm_down)
        docker_swarm = DockerSwarmConfiguration(
            master_host='10.10.10.10',
            master_port=1234,
            auto_scale=docker_swarm_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(
            docker_swarm=docker_swarm)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['dockerSwarm']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['dockerSwarm']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestCodeDeployIntegration(AwsElastigroupTestCase):
    def runTest(self):
        code_deploy_deployment_groups = CodeDeployDeploymentGroupsConfiguration(
            application_name='test-app', deployment_group_name='test-grp')
        code_deploy = CodeDeployConfiguration(
            clean_up_on_failure=False,
            terminate_instance_on_failure=False,
            deployment_groups=[code_deploy_deployment_groups])
        third_party_integrations = ThirdPartyIntegrations(
            code_deploy=code_deploy)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['codeDeploy']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['codeDeploy']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestRoute53Integration(AwsElastigroupTestCase):
    def runTest(self):
        route53_record_set = Route53RecordSetsConfiguration(
            use_public_ip=True, name='test-domain.com')
        route53_domains = Route53DomainsConfiguration(
            hosted_zone_id='Z3UFMBCGJMYLUT', record_sets=[route53_record_set])
        route53 = Route53Configuration(domains=[route53_domains])
        third_party_integrations = ThirdPartyIntegrations(route53=route53)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['route53']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['route53']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestElasticBeanstalkIntegration(AwsElastigroupTestCase):
    def runTest(self):
        deployment_strategy = BeanstalkDeploymentStrategy(
            action='REPLACE_SERVER', should_drain_instances=True)
        deployment_preferences = DeploymentPreferences(
            automatic_roll=True,
            batch_size_percentage=50,
            grace_period=600,
            strategy=deployment_strategy)
        elastic_beanstalk = ElasticBeanstalk(
            environment_id='123',
            deployment_preferences=deployment_preferences)
        third_party_integrations = ThirdPartyIntegrations(
            elastic_beanstalk=elastic_beanstalk)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['elasticBeanstalk']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['elasticBeanstalk']

        self.assertDictEqual(actual_request_json, expected_request_json)


# endregion

# region Scaling
class AwsElastigroupTestScalingIntegration(AwsElastigroupTestCase):
    def runTest(self):
        scaling_policy_up_action = ScalingPolicyAction(
            type='percentageAdjustment', adjustment=20)
        scaling_policy_up_instance_dimension = ScalingPolicyDimension(
            name='InstanceId')
        step_adjustment_action = ScalingPolicyAction(
            type='setMinTarget', min_target_capacity=3)
        step_adjustment = ScalingPolicyStepAdjustment(
            action=step_adjustment_action, threshold=50)
        scaling_policy_up = ScalingPolicy(
            metric_name='CPUUtilization',
            statistic='average',
            unit='percent',
            namespace='AWS/EC2',
            threshold=90,
            period=300,
            evaluation_periods=1,
            cooldown=300,
            operator='gte',
            action=scaling_policy_up_action,
            dimensions=[scaling_policy_up_instance_dimension],
            step_adjustments=[step_adjustment],
            min_target_capacity=1,
            is_enabled=True,
            should_resume_stateful=False)

        scaling_policy_down_action = ScalingPolicyAction(
            type='adjustment', adjustment=1)
        scaling_policy_down_cluster_dimension = ScalingPolicyDimension(
            name='Cluster', value='M2M')
        scaling_policy_down_env_dimension = ScalingPolicyDimension(
            name='Environment', value='ia-staging')
        scaling_policy_down = ScalingPolicy(
            metric_name='overhead',
            statistic='average',
            unit='milliseconds',
            namespace='Monitoring',
            threshold=0.8,
            period=300,
            evaluation_periods=1,
            cooldown=300,
            operator='lt',
            action=scaling_policy_down_action,
            dimensions=[
                scaling_policy_down_cluster_dimension,
                scaling_policy_down_env_dimension])

        target_tracking = TargetTrackingPolicy(
            policy_name='target_policy_1',
            metric_name='CPUUtilization',
            statistic='average',
            source='cloudWatch',
            unit='percent',
            target=50,
            namespace='AWS/EC2',
            cooldown=300)

        expression = MetricExpression(
            name="e1", expression="metric1+10")
        metric_dimension = ScalingPolicyDimension(
            name="instanceId",
            value="string"
        )
        metric = ScalingPolicyMetric(
            name="metric1",
            metric_name="CPUUtilization",
            namespace="AWS/EC2",
            statistic="average",
            extended_statistic="p1.5",
            unit="percent",
            dimensions=[metric_dimension]
        )
        multiple_metrics = MultipleMetrics(
            metrics=[metric],
            expressions=[expression]
        )

        scaling = Scaling(
            up=[scaling_policy_up],
            down=[scaling_policy_down],
            target=[target_tracking],
            multiple_metrics=multiple_metrics)
        group = Elastigroup(scaling=scaling)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['scaling']
        expected_request_json = self.mock_group_json['group']['scaling']

        self.maxDiff = None
        self.assertDictEqual(actual_request_json, expected_request_json)


# endregion

# region Scheduling
class AwsElastigroupTestSchedulingIntegration(AwsElastigroupTestCase):
    def runTest(self):
        scheduled_ami_backup = ScheduledTask(
            frequency='hourly', task_type='backup_ami')
        scheduled_roll = ScheduledTask(
            cron_expression='00 17 * * 3',
            task_type='roll',
            batch_size_percentage=30)
        scheduled_scale = ScheduledTask(
            cron_expression='00 22 * * 3',
            task_type='scale',
            start_time='2018-05-23T10:55:09Z',
            scale_target_capacity=0,
            scale_min_capacity=0,
            scale_max_capacity=3)

        scheduling = Scheduling(
            tasks=[
                scheduled_ami_backup,
                scheduled_roll,
                scheduled_scale])
        group = Elastigroup(scheduling=scheduling)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['scheduling']
        expected_request_json = self.mock_group_json['group']['scheduling']

        self.maxDiff = None
        self.assertDictEqual(actual_request_json, expected_request_json)
# endregion

# region Rancher
class AwsElastigroupTestRancher(AwsElastigroupTestCase):
    def runTest(self):
        rancher = Rancher(access_key="Access", secret_key="Secret", master_host="https://master.com:8080", version="2")
        third_parties_integration = ThirdPartyIntegrations(rancher=rancher)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            third_parties_integration=third_parties_integration)

        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']
        expected_request_json = {
            'rancher': {
                'accessKey': 'Access', 
                'masterHost': 'https://master.com:8080', 
                'secretKey': 'Secret', 'version': '2'
            }
        }

        self.assertDictEqual(actual_request_json, expected_request_json)
# endregion

# region Compute
class AwsElastigroupTestCompute(AwsElastigroupTestCase):
    def runTest(self):
        compute = Compute(product="Linux/UNIX",
                          preferred_availability_zones=["us-west-2a"])
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']
        expected_request_json = {
            'product': "Linux/UNIX",
            'preferredAvailabilityZones': ["us-west-2a"]}

        self.assertDictEqual(actual_request_json, expected_request_json)

class AwsElastigroupTestLaunchSpecification(AwsElastigroupTestCase):
    def runTest(self):
        launch_specification = LaunchSpecification(image_id="ami-123",
                                                   health_check_type="type")
        compute = Compute(launch_specification=launch_specification)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']['launchSpecification']
        expected_request_json = {
            'imageId': "ami-123",
            'healthCheckType': "type"
        }

        self.assertDictEqual(actual_request_json, expected_request_json)

class AwsElastigroupTestLaunchSpecificationMultipleAMI(AwsElastigroupTestCase):
    def runTest(self):
        image_list = []
        image_list.append(Image(id="ami-08e2d37b6a0129927"))
        image_list.append(Image(id="ami-0d70650c3afa9cf54"))
        image_list.append(Image(id="ami-0f05b297987cf6aff"))

        launch_specification = LaunchSpecification(images=image_list,
                                                   health_check_type="type")
        compute = Compute(launch_specification=launch_specification)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']['launchSpecification']
        expected_request_json = {
            'images': [ { "id" : "ami-08e2d37b6a0129927" }, { "id" : "ami-0d70650c3afa9cf54" }, { "id" : "ami-0f05b297987cf6aff" } ],
            'healthCheckType': "type"
        }

        self.assertDictEqual(actual_request_json, expected_request_json)

class AwsElastigroupTestBlockDeviceMapping(AwsElastigroupTestCase):
    def runTest(self):
        block_device_mappings = [BlockDeviceMapping(device_name='device')]
        launch_specification = LaunchSpecification(block_device_mappings=block_device_mappings)
        compute = Compute(launch_specification=launch_specification)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']['launchSpecification']['blockDeviceMappings'][0]
        expected_request_json = {
            'deviceName': "device"
        }

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestResourceTagSpecification(AwsElastigroupTestCase):
    def runTest(self):
        eni_specifcation = TagSpecification(should_tag=True)
        ami_specification = TagSpecification(should_tag=False)
        resource_tag_specification = ResourceTagSpecification(amis=ami_specification, enis=eni_specifcation)
        launch_specification = LaunchSpecification(resource_tag_specification=resource_tag_specification)
        compute = Compute(launch_specification=launch_specification)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']['launchSpecification']['resourceTagSpecification']

        expected_request_json = {
            'enis': {
                "shouldTag": True
            },
            'amis': {
                "shouldTag": False
            }
        }

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestEbs(AwsElastigroupTestCase):
    def runTest(self):
        ebs = [EBS(snapshot_id="snp-1", throughput=500)]
        block_device_mappings = [BlockDeviceMapping(ebs=ebs)]
        launch_specification = LaunchSpecification(block_device_mappings=block_device_mappings)
        compute = Compute(launch_specification=launch_specification)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']['launchSpecification']['blockDeviceMappings'][0]['ebs'][0]
        expected_request_json = {
            'snapshotId': "snp-1",
            'throughput': 500
        }

        self.assertDictEqual(actual_request_json, expected_request_json)

class AwsElastigroupTestDynamicVolumeSize(AwsElastigroupTestCase):
    def runTest(self):
        dynamic_volume_size = DynamicVolumeSize(resource="resource")
        ebs = [EBS(dynamic_volume_size=dynamic_volume_size)]
        block_device_mappings = [BlockDeviceMapping(ebs=ebs)]
        launch_specification = LaunchSpecification(block_device_mappings=block_device_mappings)
        compute = Compute(launch_specification=launch_specification)
        group = Elastigroup(
            name="TestGroup",
            description="Created by the Python SDK",
            compute=compute)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['compute']['launchSpecification']['blockDeviceMappings'][0]['ebs'][0]['dynamicVolumeSize']
        expected_request_json = {
            'resource': "resource"
        }

        self.assertDictEqual(actual_request_json, expected_request_json)
# endregion