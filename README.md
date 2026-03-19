# Web-Fuzzing-Box

[English](README.md) | [中文](README_CN.md)

Web Fuzzing Box - A collection of web fuzzing dictionaries and payloads, including: brute force attacks, directory and file enumeration, web vulnerabilities...

Real-world case studies using these dictionaries:
https://gh0st.cn/archives/2019-11-11/1
https://gh0st.cn/archives/2018-07-25/1

Some parameters, directories, filenames and related data are sourced from the CaA project:
https://github.com/gh0stkey/CaA

```shell
❯ tree -L 2
.
├── Brute [Brute Force]
│   ├── Chinese_Hacker_Id.txt [Hacker ID Dictionary]
│   ├── Application [Service & Application Dictionary]
│   ├── Basic_401_Login.txt [401 Authentication Dictionary]
│   ├── Full_Name [Name Pinyin Dictionary]
│   ├── Password [Password Dictionary]
│   ├── Ports [Port Dictionary]
│   ├── Security_Product [Security Products]
│   ├── Subdomain [Subdomain]
│   ├── Top_Password [Top Ranked Passwords]
│   ├── Test_Chinese_Mobilephonenumber.txt [Test Mobile Numbers]
│   └── Username [Username Dictionary]

├── Dir [Directory, Filename, API]
│   ├── Others [Other Dictionaries]
│   ├── Burpsuite [Dictionaries for BurpSuite]
│   ├── Wooyun [Wooyun Historical Vulnerability Directories & Files]
│   └── Yujian [Chinese Yujian Dictionary]

├── Vuln [Vulnerability Related Dictionaries]
│   ├── Api_Bypass [API Vulnerabilities: 403 Bypass, Auth Bypass]
│   ├── File_Upload [File Upload Vulnerabilities]
│   ├── Logic [Logic Vulnerabilities]
│   ├── File_Include [File Inclusion Dictionary]
│   ├── Image_Dos [Image Resource DoS Vulnerability Dictionary]
│   ├── Jsonp [JSONP Cross-Domain Hijacking Dictionary]
│   ├── Open_Redirect [URL Redirect Vulnerability Dictionary]
│   ├── Sql_Injection [SQL Injection Dictionary]
│   ├── Traversal_Directory [Directory Traversal Vulnerability Dictionary]
│   ├── Xml_Bomb [XML Bomb Payloads]
│   └── Xss [XSS Dictionary & Payloads]

├── Other [Other Dictionaries]
│   ├── 2W_Words.txt
│   └── Chinese Province Mobile Number Segments

└── Web [Web Testing Dictionary]
    ├── File_Path [Some Files and Paths]
    ├── Funcation_Name.txt [Function Names]
    ├── HTML [HTML Related]
    ├── Headers [HTTP Headers]
    ├── Http_Methods.txt [HTTP Request Methods]
    ├── Integer_Overflows.txt [Integer Overflow]
    ├── Javascript_Filename.txt [JavaScript Filenames]
    ├── Lcoalhost.txt [Localhost Addresses]
    ├── Dict [Verb/Noun Dictionary, Request Parameters]
    ├── URL [URL Related Protocols and Types]
    └── ViewState_Key.txt [For ViewState Deserialization]
```

## Acknowledgements

[yuanhaiGreg](https://github.com/yuanhaiGreg): Contributed file upload parameters, ViewState_Key
