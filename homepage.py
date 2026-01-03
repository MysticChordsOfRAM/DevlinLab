from flask import Flask, render_template
import supersecrets as shh

app = Flask(__name__)

SUBNETS = [

    {"name": 'Admin Network',
     "IP": shh.admin_ip,
     "color": "#3e0b87"},
    
    {"name": 'Data Warehouse',
     "IP": shh.dw_ip,
     "color": "#1d6a32"},

    {"name": 'IOT WiFi',
     "IP": shh.iot_ip,
     "color": "#c14b00"},

    {"name": 'Mobile Devices WiFi',
     "IP": shh.mobile_ip,
     "color": "#0988b6"},

    {"name": 'Guest WiFi',
     "IP": shh.guest_ip,
     "color": "#e7ec38"}

]

DEVICES = [

    {"name": 'TheMessTent',
     "IP": shh.messtent_ip,
     "build": 'Intel i9-13900k ~ 96GB',
     "color": '#a438ec'},

    {"name": 'ECHO',
     "IP": shh.echo_ip,
     "build": 'AMD Ryzen 5 7600 ~ 32GB',
     "color": "#2d57ae"},

    {"name": 'COSMO',
     "IP": shh.cosmo_ip,
     "build": 'Raspberry Pi 5',
     "color": "#1b830a"},

    {"name": 'DARREN',
     "IP": shh.darren_ip,
     "build": 'Raspberry Pi 5',
     "color": "#d67334"}

]

SERVICES = [

    {"name": 'Router',
     "url": shh.router_link,
     "desc": shh.router_model,
     "home": shh.router_ip,
     "color": '#3e6674'},

    {"name": 'Switch',
     "url": shh.switch_link,
     "desc": shh.switch_model,
     "home": shh.switch_ip,
     "color": '#3e6674'},

    {"name": 'WiFi AP',
     "url": shh.ap_link,
     "desc": shh.ap_model,
     "home": shh.ap_ip,
     "color": '#3e6674'},

    {"name": 'Cosmo The Budget Bot',
     "url": shh.bot_link,
     "home": shh.bot_ip,
     "desc": 'A Twilio app that I use for on-the-go data entry',
     "color": '#1b830a'},

    {"name": 'Shiny',
     "url": shh.shiny_link,
     "home": shh.shiny_ip,
     "desc": 'Shiny apps that I use for data analysis',
     "color": '#2d57ae'},

    {"name": 'Wiki.JS',
     "url": shh.wiki_link,
     "home": shh.wiki_ip,
     "desc": 'Documentation for my Postgres Database',
     "color": '#1b830a'},

    {"name": 'Ollama',
     "url": shh.lama_link,
     "home": shh.lama_ip,
     "desc": 'The Open-Web UI for local Ollama Models',
     "color": '#2d57ae'},

    {"name": 'Grafana',
     "url": shh.graf_link,
     "home": shh.graf_ip,
     "desc": 'Monitoring Dashboard',
     "color": '#2d57ae'},

    {"name": 'Prometheus',
     "url": shh.prom_link,
     "home": shh.prom_ip,
     "desc": 'Data Collection for Grafana',
     "color": '#2d57ae'},

    {"name": 'Plex',
     "url": shh.plex_link,
     "home": shh.plex_ip,
     "desc": 'My collection of Movies and TV Shows',
     "color": '#1b830a'},

    {"name": 'Grocy',
     "url": shh.groc_link,
     "home": shh.groc_ip,
     "desc": 'Home Grocery Inventory Management',
     "color": '#d67334'},

    {"name": 'Barcode Buddy',
     "url": shh.bb_link,
     "home": shh.bb_ip,
     "desc": 'Barcode Scanner Advanced Mode',
     "color": '#d67334'}

]

@app.route('/')
def homepage():
    return render_template('homepage.html', 
                           services = SERVICES,
                           devices = DEVICES,
                           subnets = SUBNETS)

if __name__ == "__main__":
    app.run(host = shh.app_host, port = shh.app_port)
