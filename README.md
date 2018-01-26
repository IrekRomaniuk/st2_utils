# my st2 Pack with utils and tests

Experimenting with concurrent and parallel tasks on multiple targets

## Actions

- /api/v1/webhooks/netpro - webhook
- st2_utils.cmd - Run command on remote Linux (parallel ssh)
- st2_utils.cmd2file - Action chain to run command on remote Linux and write output to file ( 'dict object' has no attribute 'stdout')


## Using the pack - Under development

### Installing

```
$ st2 pack install https://github.com/irekromaniuk/st2_utils
st2ctl reload --register-actions or st2ctl reload --register-all
st2 action list --pack=st2_utils
```

### Trobleshooting

```
st2 rule-enforcement list --rule=st2_utils.on_hello_event1
st2 rule-enforcement list --rule=st2_utils.hook_cmd
tail -f /var/log/st2/st2rulesengine.log
```

### Testing

```
$ time st2 run st2-utils.cmd hosts="1.1.1.1,2.2.2.2,3.3.3.3,1.1.1.1,2.2.2.2,3.3.3.3" username=user password='password' cmd=uptime timeout=2
...
real    1m15.943s
user    0m0.700s
sys     0m0.076s

st2 rule disable st2_utils.on_hello_event1

$ curl -k https://st2/api/v1/webhooks/netpro -d '{"hosts":"1.1.1.1,2.2.2.2", "user": "user", "pass": "password", "cmd":"uptime"}' -H 'Content-Type: application/json' -H 'St2-Api-Key: key'

st2 run st2_utils.cmd2file cmd=uptime hosts="1.1.1.1,2.2.2.2" password="pass" username=user
```