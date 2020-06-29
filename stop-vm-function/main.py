import base64
import googleapiclient.discovery
from pprint import pprint
import logging
import json
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
try:
     def stop_vm(event, context):
          compute = googleapiclient.discovery.build('compute', 'v1')
          if 'data' in event:
               payload = base64.b64decode(event['data']).decode('utf-8')
          else:
               payload="{}"
          json_payload=json.loads(payload)
          print('Got JSON payload')
          pprint(json_payload)
          project=json_payload['project']
          for region in json_payload['regions']:
               zones = region["zones"]
               print(type(zones))
               pprint(zones)
               #zones=["b","c"]
               for myzone in zones:
                    final_zone=region['name']+ "-" + myzone
                    instances = list_instances(compute, project, final_zone)
                    pprint(json_payload['regions'])
                    print('Instances in project %s and zone %s:' % (project, final_zone))
                    for instance in instances or []:
                         print(' - ' + instance['name'])
                         if "RUNNING" in instance['status']:
                              if json_payload["filter"] in instance['name']:
                                   pprint(instance)
                                   request = compute.instances().stop(project=project, zone=final_zone, instance=instance['name'])
                                   response = request.execute()
                                   # TODO: Change code below to process the `response` dict:
                                   pprint(response)

     def list_instances(compute, project, zone):
          result = compute.instances().list(project=project, zone=zone).execute()
          return result['items'] if 'items' in result else None
except Exception as e:
    logger.error(f"Trace: {traceback.format_exc()}")
    time.sleep(5)
    raise e