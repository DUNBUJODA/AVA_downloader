### Source
https://github.com/mtobeiyf/ava_downloader

### Environment

Python 3.5

### Description

#### anti-scratch mechanism

Reference: https://blog.csdn.net/c406495762/article/details/60137956?utm_source=distribute.pc_relevant.none-task

##### Step 1

Go to https://www.xicidaili.com/ for a free ip address.

##### Step 2

Copy it to `proxy = {'http':'163.204.246.76:9999'}` in ip_test.py

##### Step 3

Test the ip address.

```bash
python ip_test.py
```

#####   Step 4

Copy the ip address to `proxy = {'http':'163.204.246.76:9999'}` in ava

_downloader.py

##### Step 5

Run downloader.

```bash
python ava_downloader.py 50 100
```

Path downloader/AVA_dataset/image will receive images.

### BUGS

- no ip address can pass the 'step-3 test' in that website.