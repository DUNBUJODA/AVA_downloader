### Source
https://github.com/mtobeiyf/ava_downloader

### Environment

Python 3.5

### Description

#### 1: anti-scratch mechanism

Reference: https://blog.csdn.net/c406495762/article/details/60137956?utm_source=distribute.pc_relevant.none-task

##### Step 1

Go to https://www.xicidaili.com/ for a free IP address.

##### Step 2

Copy it to `proxy = {'http':'163.204.246.76:9999'}` in ip_test.py

##### Step 3

Test the IP address.

```bash
python ip_test.py
```

##### Step 4

Copy the IP address to `proxy = {'http':'163.204.246.76:9999'}` in ava_downloader.py

##### Step 5

Run downloader.

```bash
python ava_downloader.py 50 100
```

Path downloader/AVA_dataset/image will receive images.

#### 2: Conclusion

- No IP address can pass the 'step-3 test' in that website.
- ava_downloader_no_ip_camouflage.py will return nothing, which may be caused by my IP being blocked.
- ava_downloader_no_ip_camouflage.py can run on the Colab and return correct results. That's because Colab is a virtual machine and will change its IP address every time remount.