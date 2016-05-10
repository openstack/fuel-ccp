import os

from oslo_config import cfg


CONF = cfg.CONF
repositories_opts = [
    cfg.BoolOpt('clone',
                default=True,
                help='Automatic cloning of microservices repositories'),
    cfg.BoolOpt('skip-empty',
                default=True,
                help='Skip repositories not containing Dockerfiles without '
                     'error'),
    cfg.StrOpt('path',
               default=os.path.expanduser('~/microservices-repos/'),
               help='Path where the microservice repositories are cloned'),
    cfg.ListOpt('components',
                default=['ms-debian-base',
                         'ms-aodh',
                         'ms-ceilometer',
                         'ms-ceph',
                         'ms-cinder',
                         'ms-designate',
                         'ms-elasticsearch',
                         'ms-glance',
                         'ms-heat',
                         'ms-heka',
                         'ms-horizon',
                         'ms-ironic',
                         'ms-keystone',
                         'ms-kibana',
                         'ms-magnum',
                         'ms-manila',
                         'ms-mariadb',
                         'ms-memcached',
                         'ms-mistral',
                         'ms-mongodb',
                         'ms-murano',
                         'ms-neutron',
                         'ms-nova',
                         'ms-openstack-base',
                         'ms-openvswitch',
                         'ms-rabbitmq',
                         'ms-sahara',
                         'ms-swift',
                         'ms-tempest',
                         'ms-toolbox',
                         'ms-trove',
                         'ms-zaqar'],
                help='List of repositories'),
    cfg.StrOpt('ms-debian-base',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-debian-base'),
    cfg.StrOpt('ms-aodh',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-aodh'),
    cfg.StrOpt('ms-ceilometer',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-ceilometer'),
    cfg.StrOpt('ms-ceph',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-ceph'),
    cfg.StrOpt('ms-cinder',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-cinder'),
    cfg.StrOpt('ms-designate',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-designate'),
    cfg.StrOpt('ms-elasticsearch',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-elasticsearch'),
    cfg.StrOpt('ms-glance',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-glance'),
    cfg.StrOpt('ms-heat',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-heat'),
    cfg.StrOpt('ms-heka',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-heka'),
    cfg.StrOpt('ms-horizon',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-horizon'),
    cfg.StrOpt('ms-ironic',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-ironic'),
    cfg.StrOpt('ms-keystone',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-keystone'),
    cfg.StrOpt('ms-kibana',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-kibana'),
    cfg.StrOpt('ms-magnum',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-magnum'),
    cfg.StrOpt('ms-manila',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-manila'),
    cfg.StrOpt('ms-mariadb',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-mariadb'),
    cfg.StrOpt('ms-memcached',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-memcached'),
    cfg.StrOpt('ms-mistral',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-mistral'),
    cfg.StrOpt('ms-mongodb',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-mongodb'),
    cfg.StrOpt('ms-murano',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-murano'),
    cfg.StrOpt('ms-neutron',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-neutron'),
    cfg.StrOpt('ms-nova',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-nova'),
    cfg.StrOpt('ms-openstack-base',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-openstack-base'),
    cfg.StrOpt('ms-openvswitch',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-openvswitch'),
    cfg.StrOpt('ms-rabbitmq',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-rabbitmq'),
    cfg.StrOpt('ms-sahara',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-sahara'),
    cfg.StrOpt('ms-swift',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-swift'),
    cfg.StrOpt('ms-tempest',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-tempest'),
    cfg.StrOpt('ms-toolbox',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-toolbox'),
    cfg.StrOpt('ms-trove',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-trove'),
    cfg.StrOpt('ms-zaqar',
               default='ssh://%s@review.fuel-infra.org:29418/'
                       'nextgen/ms-zaqar')
]
repositories_opt_group = cfg.OptGroup(name='repositories',
                                      title='Git repositories for components')
CONF.register_group(repositories_opt_group)
CONF.register_cli_opts(repositories_opts, repositories_opt_group)
CONF.register_opts(repositories_opts, repositories_opt_group)
