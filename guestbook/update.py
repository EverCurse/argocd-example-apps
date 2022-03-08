import yaml
file = open('guestbook-ui-deployment.yaml', 'r')
file_data = file.read()
file.close()
data = yaml.load(file_data)
data['spec']['template']['spec']['containers'][0]['image'] = "httpd"
with open('guestbook-ui-deployment.yaml', 'w') as stream:
  yaml.dump(data,stream)
