# my st2 Pack with utils and tests

Experimenting with concurrent and parallel tasks on multiple targets

## Actions

- /api/v1/webhooks/netpro - webhook
- gost2netpro - Go program to [post json to st2 webhook](https://github.com/IrekRomaniuk/gost2netpro)
- st2_utils.cmd - Run command on remote targets (parallel ssh)
- st2_utils.mistral_cmd2file - Mistral workflow to run command on remote targets and write output to file
- st2_utils.chain_cmd2file - Action chain to run command on remote targets and write output to file (or two files with "succeeded" and "failed" IPs  based on JSON result)
```
"result": {
            "1.1.1.1": {
                "succeeded": true,
                "failed": false,
                "return_code": 0,
                "stderr": "",
                "stdout": " 15:06:09 up 37 days,  2:44, load average: 0.00, 0.00, 0.00"
            },
            "2.2.2.2": {
                "succeeded": true,
                "failed": false,
                "return_code": 0,
                "stderr": "",
                "stdout": " 15:06:10 up 53 days,  4:16, load average: 0.54, 0.28, 0.16"
            }
} 
```
- st2_utils.chain_cmd2cmd - Action chain to re-run command with different params on failed remote targets



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
st2 run st2_utils.cmd cmd=uptime hosts="1.1.1.1,2.2.2.2" password="pass" username=user
st2 run st2_utils.chain_cmd2file cmd=uptime hosts="1.1.1.1,2.2.2.2" password="pass" username=user
st2 run st2_utils.mistral_cmd2file cmd=uptime hosts="1.1.1.1,2.2.2.2" password="pass" username=user
```