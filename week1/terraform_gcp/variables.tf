variable "credentials_path" {
  description = "My Credentials"
  default     = "./keys/my-cred.json"

}

variable "project" {
  description = "Project"
  default     = "refined-outlet-444512-t6"
}

variable "region" {
  description = "Project region"
  default     = "europe-west10"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "refined-outlet-444512-t6"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
