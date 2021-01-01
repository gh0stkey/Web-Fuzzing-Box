# Web-Fuzzing-Box

Web Fuzzing Box - Web 模糊测试字典与一些Payloads，主要包含：弱口令暴力破解、目录以及文件枚举、Web漏洞...

字典运用于实战案例：https://gh0st.cn/archives/2019-11-11/1

```shell
❯ tree -L 2

├── Brute [爆破]
│   ├── Abroad [国外字典]
│   ├── Application [服务、应用字典]
│   ├── Basic_401_Login.txt [401认证字典]
│   ├── Chinese [适用于中国的字典]
│   ├── Chinese_Hacker_Id.txt [中国黑客ID]
│   ├── Password [密码字典]
│   ├── Security_Product [安全产品]
│   ├── Subdomain [子域名]
│   ├── Test_Chinese_Mobilephonenumber.txt [中国手机号测试字典]
│   ├── Top [Top排名字典]
│   └── Username [用户名字典]

├── Dir [目录、文件名、接口]
│   ├── Api.txt [接口字典]
│   ├── Aspx_Asp_Cfm_Svc_Ashx_Asmx.txt [Aspx、Asp、Cfm、Svc、Ashx、Asmx后缀文件名字典]
│   ├── Burpsuite [适用于BurpSuite的字典，源于：https://gh0st.cn//archives/2020-02-13/1]
│   ├── Ctf.txt [适用于CTF比赛的字典]
│   ├── Directories.txt [目录字典]
│   ├── Jsp_Jspa_Do_Action.txt [Jsp、Jspa、Do、Action后缀文件名字典]
│   ├── Php.txt [Php后缀文件名字典]
│   └── Yujian [中国御剑字典]

├── Vuln [漏洞相关字典]
│   ├── Api [Api漏洞：绕过403、鉴权绕过]
│   ├── File_Upload [文件上传漏洞]
│   ├── File_Include [文件包含字典]
│   ├── Image_Dos [图片资源导致的DoS拒绝服务漏洞字典]
│   ├── Jsonp [JSONP跨域劫持漏洞字典]
│   ├── Open_Redirect [URL跳转漏洞字典]
│   ├── Sql_Injection [SQL注入字典]
│   ├── Traversal_Directory [遍历目录漏洞字典]
│   ├── Xml_Bomb [XML炸弹Payloads]
│   └── Xss [XSS字典与Payloads]

└── Web [Web测试字典]
    ├── *nix_Etc_Path [*nix系统的etc路径下的文件]
    ├── All_Html_Tag.txt [所有的HTML标签]
    ├── File_Extensions.txt [文件后缀名]
    ├── Http_Methods.txt [HTTP请求方式]
    ├── Integer_Overflows.txt [整数溢出]
    ├── Javascript_Filename.txt [Javascript文件名]
    ├── Lcoalhost.txt [本地地址]
    ├── Linux_File.txt [Linux文件]
    ├── Parameters [HTTP请求参数]
    ├── Proc_Path.txt [Proc路径下的文件]
    ├── Server_Log_Path.txt [服务日志路径]
    ├── Url_Schemes.txt [URL协议类型]
    ├── User_Agent.txt [UA头]
    └── Windows_File.txt [Windows文件]

27 directories, 25 files

```