<h1 id="spotinst_sdk2.clients.ocean.OceanAzureClient">OceanAzureClient</h1>

```python
OceanAzureClient(self,
                 session=None,
                 print_output=True,
                 log_level=None,
                 user_agent=None,
                 timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.create_ocean_cluster">create_ocean_cluster</h2>

```python
OceanAzureClient.create_ocean_cluster(ocean: Ocean)
```

Create an Ocean Cluster

__Arguments__

- __ocean (Ocean)__: Ocean Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_all_ocean_clusters">get_all_ocean_clusters</h2>

```python
OceanAzureClient.get_all_ocean_clusters()
```

List the configurations for all Ocean clusters in the specified account.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanAzureClient.get_ocean_cluster(ocean_id: str)
```

Get an existing Ocean Cluster json

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanAzureClient.delete_ocean_cluster(ocean_id: str)
```

Delete an Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanAzureClient.update_ocean_cluster(ocean_id: str, ocean: Ocean)
```

Update an existing Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.import_cluster_configuration">import_cluster_configuration</h2>

```python
OceanAzureClient.import_cluster_configuration(aks_cluster_name: str,
                                              resource_group_name: str)
```

Import cluster configuration of an AKS cluster to use in create_ocean_cluster api call

__Arguments__

- __aks_cluster_name (String)__: Name of the AKS cluster
- __resource_group_name (String)__: Resource Group Name

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.create_ocean_vng">create_ocean_vng</h2>

```python
OceanAzureClient.create_ocean_vng(vng: VirtualNodeGroupTemplate)
```

Create a VNG inside ocean cluster

__Arguments__

- __vng (VirtualNodeGroup)__: VirtualNodeGroup Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.update_ocean_vng">update_ocean_vng</h2>

```python
OceanAzureClient.update_ocean_vng(vng_id: str,
                                  vng: VirtualNodeGroupTemplate)
```

Update an existing VNG inside an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean Virtual Node Group
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_ocean_vng">get_ocean_vng</h2>

```python
OceanAzureClient.get_ocean_vng(vng_id: str)
```

Get an existing Ocean Virtual Node Group json

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_all_ocean_vngs">get_all_ocean_vngs</h2>

```python
OceanAzureClient.get_all_ocean_vngs(ocean_id: str = None)
```

List the configurations for all virtual node groups in the account
or in a specified cluster.

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.delete_ocean_vng">delete_ocean_vng</h2>

```python
OceanAzureClient.delete_ocean_vng(vng_id: str)
```

Delete an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.import_vng_configuration">import_vng_configuration</h2>

```python
OceanAzureClient.import_vng_configuration(node_pool_name: str,
                                          ocean_id: str)
```

Import cluster configuration of an AKS cluster to use in create_ocean_cluster api call

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.launch_new_nodes">launch_new_nodes</h2>

```python
OceanAzureClient.launch_new_nodes(node_config: LaunchNewNodes)
```

Launch new nodes for a cluster

__Arguments__

- __node_config (LaunchNewNodes)__: LaunchNewNodes object

__Returns__

`(Object)`: Ocean Launch New Nodes API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_allowed_vng_vm_sizes">get_allowed_vng_vm_sizes</h2>

```python
OceanAzureClient.get_allowed_vng_vm_sizes(vng_id: str)
```

Get allowed vm sizes for a particular VNG

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG

__Returns__

`(Object)`: Array of allowed vm sizes list

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.initiate_roll">initiate_roll</h2>

```python
OceanAzureClient.initiate_roll(ocean_id: str, cluster_roll: Roll)
```

Initiate Cluster Rolls

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __cluster_roll (Roll)__: Cluster Roll / Node Pool names/ VNG Ids

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_roll">get_roll</h2>

```python
OceanAzureClient.get_roll(ocean_id: str, roll_id: str)
```

Get status for a roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __account_id (String)__: The ID of the account associated with your token.
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.list_rolls">list_rolls</h2>

```python
OceanAzureClient.list_rolls(ocean_id: str)
```

Get status for all rolls of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: List of Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.stop_roll">stop_roll</h2>

```python
OceanAzureClient.stop_roll(ocean_id: str, roll_id: str)
```

Stop roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __account_id (String)__: The ID of the account associated with your token.
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.create_migration">create_migration</h2>

```python
OceanAzureClient.create_migration(ocean_id: str, migration: Migration)
```

Create a migration for a given existing instances.

__Arguments__

- __migration (Migration)__: Migration Object

__Returns__

`(Object)`: Migration create response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_migration_discovery">get_migration_discovery</h2>

```python
OceanAzureClient.get_migration_discovery(ocean_id: str,
                                         should_fetch_pods: bool)
```

Get information about nodes which can be migrated into Ocean.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __should_fetch_pods (bool)__: Should fetch data about running pods for each node.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.stop_migration">stop_migration</h2>

```python
OceanAzureClient.stop_migration(ocean_id: str, migration_id: str)
```

Stop an ongoing Workload Migration.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __migration_id (String)__: The migration identifier of a specific migration

__Returns__

`(Object)`: Ocean Migration response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_migration">get_migration</h2>

```python
OceanAzureClient.get_migration(ocean_id: str, migration_id: str)
```

Get Migration full info and status for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __migration_id (String)__: The migration identifier of a specific migration.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.list_migrations">list_migrations</h2>

```python
OceanAzureClient.list_migrations(ocean_id: str)
```

Get summary of migrations history for an Ocean cluster.

__Returns__

`(Object)`: Ocean Migrations response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.detach_nodes">detach_nodes</h2>

```python
OceanAzureClient.detach_nodes(detach_nodes: DetachNodes)
```

Detach nodes from your Ocean cluster.

__Arguments__

- __detach_nodes (DetachNodes)__: Detach Nodes Object

__Returns__

`(Object)`: Detach Nodes response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_elastilog">get_elastilog</h2>

```python
OceanAzureClient.get_elastilog(ocean_id: str,
                               from_date: str,
                               to_date: str,
                               severity: str = None,
                               resource_id: str = None,
                               limit: int = None)
```

Get the log of an Ocean Cluster.

__Arguments__

- __to_date (String)__: end date value
- __from_date (String)__: beginning date value
- __severity(String) (Optional)__: Log level severity
- __resource_id(String) (Optional)__: specific resource identifier
- __limit(int) (Optional)__: Maximum number of lines to extract in a response

__Returns__

`(Object)`: Ocean Get Log API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_aggregated_detailed_costs">get_aggregated_detailed_costs</h2>

```python
OceanAzureClient.get_aggregated_detailed_costs(
  ocean_id: str, aggregated_cluster_costs: AggregatedClusterCosts)
```

Provides Kubernetes cluster resource usage and costs over a time interval which can be grouped and/or filtered by label/annotaion

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __aggregated_cluster_costs (AggregatedClusterCosts)__: Aggregated Cluster Costs request

__Returns__

`(Object)`: Aggregated Cluster Costs API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_aggregated_summary_costs">get_aggregated_summary_costs</h2>

```python
OceanAzureClient.get_aggregated_summary_costs(
  ocean_id: str, aggregated_cluster_costs: AggregatedClusterCosts)
```

Provides Kubernetes cluster summary usage and costs over a time interval which can be grouped and/or filtered by label/annotaion

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __aggregated_cluster_costs (AggregatedClusterCosts)__: Aggregated Cluster Costs request

__Returns__

`(Object)`: Aggregated Cluster Costs API response

