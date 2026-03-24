local g = import 'g.libsonnet';

g.dashboard.new('Batch Job dashboard')
+ g.dashboard.withUid('batch-job-demo')
+ g.dashboard.withDescription('Dashboard for Batch Job')
+ g.dashboard.graphTooltip.withSharedCrosshair()
+ g.dashboard.withPanels([
  g.panel.timeSeries.new('Duration')
  + g.panel.timeSeries.queryOptions.withTargets([
    g.query.prometheus.new(
      'prometheus',
      'batch_job_duration_seconds{job="batch_job"}',
    ),
  ]),

  g.panel.timeSeries.new('Records')
  + g.panel.timeSeries.queryOptions.withTargets([
    g.query.prometheus.new(
      'prometheus',
      'increase(batch_records_total{job="batch_job"}[1h])',
    ),
  ])
])
