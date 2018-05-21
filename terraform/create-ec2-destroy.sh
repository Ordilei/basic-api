#!/bin/bash

terraform init

terraform plan 

terraform apply -input=false -auto-approve

sleep 60

terraform destroy