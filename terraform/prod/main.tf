module "ecs" {
  source               = "git@github.com:eHealthAfrica/terraform//generic_ecs_service"
  environment           = "${var.environment}"
  project               = "${var.project}"
  project_billing_id    = "${var.project_billing_id}"
  app                   = "api"
  http_rule_priority    = 804
  database_hostname     = "not_required"
  application_memory    = 4096
  memory_reservation    = 1024
  domain                = "grid-nigeria.org"
  url                   = "api"
}
