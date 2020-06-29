# gcp-python-jobs
This repo cotains common python Cloud functions to do admin jobs in GCP. 


Stop-VM-Instance:

It's an utility function to stop all VM instances in a project. This can be used with PUb/Sub topic to stop VM instances when not needed. Typically with Cloud Scheduler you can deploy this script as cloud function and stop all your VMs at a given time. It tries to achieve following pattern:

