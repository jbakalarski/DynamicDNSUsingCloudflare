<h1 align = 'center'>
    <img 
        src = '/assets/icon.png' 
        height = '200' 
        width = '200' 
        alt = 'Icon' 
    />
    <br>
    Dynamic DNS using Cloudflare
    <br>
</h1>

<div align = 'center'>
    <a href = 'https://github.com/(https://github.com/jbakalarski/DynamicDNSUsingCloudflare/wiki/Config-File)(https://github.com/jbakalarski/DynamicDNSUsingCloudflare/wiki/Config-File)/DynamicDNSUsingCloudflare/'>
        <img src = 'https://img.shields.io/github/stars/jbakalarski/DynamicDNSUsingCloudflare?style=for-the-badge&color=%23cfb002'/>
    </a>
    <a href = 'https://github.com/jbakalarski/DynamicDNSUsingCloudflare/tags'>
        <img src = 'https://img.shields.io/github/v/tag/jbakalarski/DynamicDNSUsingCloudflare?style=for-the-badge&label=version'/>
    </a>
    <a href = 'https://github.com/jbakalarski/DynamicDNSUsingCloudflare/issues'>
        <img src = 'https://img.shields.io/github/issues/jbakalarski/DynamicDNSUsingCloudflare?style=for-the-badge&color=%23ff6f00'/>
    </a>
    <a href = 'https://github.com/jbakalarski/DynamicDNSUsingCloudflare/pulls'>
        <img src = 'https://img.shields.io/github/issues-pr/jbakalarski/DynamicDNSUsingCloudflare?style=for-the-badge'/>
    </a>
</div>

<br>

**❓ What is this?** Simple script written in python that allows you to assign domain to changing IP address.

**❓ How to use it?**
* [**Using docker-compose**](#-using-docker-compose-to-run-dynamic-dns-using-cloudflare)
* [**Using Python**](#-using-python-to-run-dynamic-dns-using-cloudflare)

**❓ What did I use?**
* [Python](https://www.python.org/)
* [Python libraries](/requirements.txt)
* [Docker](https://www.docker.com/)
* [Cloudflare API](https://developers.cloudflare.com/api/)
* [Getting IP Address](https://www.ipify.org/)
* [Coding](https://code.visualstudio.com/)
* [Git management](https://desktop.github.com/)


## 🐳 Using docker-compose to run Dynamic DNS using Cloudflare
1) Install Docker and docker-compose
2) Copy `docker-compose.yml`
3) Fill it in according to [wiki](https://github.com/jbakalarski/DynamicDNSUsingCloudflare/wiki/Config)
4) Run container:
```bash
docker-compose up -d
```
5) It works!

## 🐍 Using Python to run Dynamic DNS using Cloudflare
1) Install Python and Git
2) Clone this repository and enter its directory:
```bash
git clone https://github.com/jbakalarski/DynamicDNSUsingCloudflare.git
```
3) Install requirements:
```bash
python -m pip install -r requirements.txt
```
4) Create `.env` and fill it in according to [wiki](https://github.com/jbakalarski/DynamicDNSUsingCloudflare/wiki/Config)
5) Run main.py:
```
python main.py
```
6) It works!

## 🚀 Features
* Assigning domain to changing IP address using Cloudflare DNS records
* Running every now and then defined by user

## ❓ Purpose
Assigning domain to changing IP address. Changing IP address is commonly occurring at home.

## ❗ Other informations
This project is not created by Cloudflare Inc., but it uses Cloudflare Inc. API to edit DNS zones.

## 💲 Support
<p><a href="https://support.jedrzej.me/" target="_blank"> <img align="left" src="https://raw.githubusercontent.com/jbakalarski/jbakalarski/main/assets/supportme.svg" height="50" width="210" alt="jbakalarski" /></a></p>