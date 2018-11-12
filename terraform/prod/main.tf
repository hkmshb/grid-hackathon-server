module "ecs" {
  source               = "git@github.com:eHealthAfrica/terraform//generic_ecs_service?ref=v2.0.2"
  environment           = "${var.environment}"
  project               = "${var.project}"
  app                   = "api"
  data_dir              = "/app"
  database_hostname     = "not_required"
  application_memory    = 4096
  memory_reservation    = 1024
  domain                = "grid-nigeria.org"
  url                   = "api"
}
