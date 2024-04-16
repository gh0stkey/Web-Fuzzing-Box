# Web-Fuzzing-Box

Web Fuzzing Box - Web 模糊测试字典与一些Payloads，主要包含：弱口令暴力破解、目录以及文件枚举、Web漏洞...

字典运用于实战案例：
https://gh0st.cn/archives/2019-11-11/1
https://gh0st.cn/archives/2018-07-25/1

参数、目录、文件名等相关数据部分来源于CaA项目：
https://github.com/gh0stkey/CaA

```shell
❯ tree -L 2
.
├── Brute [爆破]
│   ├── Chinese_Hacker_Id.txt [黑客ID字典]
│   ├── Application [服务、应用字典]
│   ├── Basic_401_Login.txt [401认证字典]
│   ├── Name [姓名拼音字典]
│   ├── Password [密码字典]
│   ├── Ports [端口字典]
│   ├── Security_Product [安全产品]
│   ├── Subdomain [子域名]
│   ├── Top_Password [Top排名字典]
│   ├── Test_Chinese_Mobilephonenumber.txt [测试手机号字典]
│   └── Username [用户名字典]

├── Dir [目录、文件名、接口]
│   ├── Others [其他字典]
│   ├── Burpsuite [适用于BurpSuite的字典]
│   ├── Wooyun [乌云历史漏洞目录、文件字典]
│   └── Yujian [中国御剑字典]

├── Vuln [漏洞相关字典]
│   ├── Api_Bypass [Api漏洞：绕过403、鉴权绕过]
│   ├── File_Upload [文件上传漏洞]
│   ├── Logic [逻辑漏洞]
│   ├── File_Include [文件包含字典]
│   ├── Image_Dos [图片资源导致的DoS拒绝服务漏洞字典]
│   ├── Jsonp [JSONP跨域劫持漏洞字典]
│   ├── Open_Redirect [URL跳转漏洞字典]
│   ├── Sql_Injection [SQL注入字典]
│   ├── Traversal_Directory [遍历目录漏洞字典]
│   ├── Xml_Bomb [XML炸弹Payloads]
│   └── Xss [XSS字典与Payloads]

├── Other [其他字典]
│   ├── 2W_Words.txt
│   └── 各省市手机号号段

└── Web [Web测试字典]
    ├── File_Path [一些文件及路径]
    ├── Funcation_Name.txt [函数名]
    ├── HTML [HTML相关]
    ├── Headers [HTTP头]
    ├── Http_Methods.txt [HTTP请求方式]
    ├── Integer_Overflows.txt [整数溢出]
    ├── Javascript_Filename.txt [JavaScript文件名]
    ├── Lcoalhost.txt [本地地址]
    ├── Parameters [请求参数]
    ├── URL [URL相关协议和类型]
    └── ViewState_Key.txt [用于ViewState反序列化]
```

## 致谢

[远海](https://github.com/yuanhaiGreg): 贡献文件上传参数、ViewState_Key