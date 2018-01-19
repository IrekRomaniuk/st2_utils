# my st2 Pack with utils and tests

Under development

```
$ st2 pack install https://github.com/irekromaniuk/st2_utils
st2ctl reload --register-actions or st2ctl reload --register-all
st2 action list --pack=st2_utils
st2 rule-enforcement list --rule=st2_utils.on_hello_event1
tail -f /var/log/st2/st2rulesengine.log
$ time st2 run st2-utils.my_linux-cmd hosts="1.1.1.1,2.2.2.2,3.3.3.3,1.1.1.1,2.2.2.2,3.3.3.3" username=user password='password' cmd=uptime timeout=2
...
real    1m15.943s
user    0m0.700s
sys     0m0.076s
```
st2 rule disable st2_utils.on_hello_event1