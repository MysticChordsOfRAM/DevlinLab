from flask import Flask, render_template
import supersecrets as shh

app = Flask(__name__)

admin_color = "#16171c"
echo_color = "#875cc9"
yavin_color = "#1b830a"
cosmo_color = "#ec9bec"
darren_color = "#b84143"
lomez_color = "#71adc7"
bobcobb_color = "#a0c771"

SUBNETS = [

    {"name": 'Admin Network',
     "IP": shh.admin_ip,
     "color": admin_color},
    
    {"name": 'Data Warehouse',
     "IP": shh.dw_ip,
     "color": echo_color},

    {"name": 'IOT WiFi',
     "IP": shh.iot_ip,
     "color": bobcobb_color},

    {"name": 'Mobile Devices WiFi',
     "IP": shh.mobile_ip,
     "color": lomez_color},

    {"name": 'Guest WiFi',
     "IP": shh.guest_ip,
     "color": "#e7ec38"},

    {"name": 'Home Services',
     "IP": shh.homesvc_ip,
     "color": darren_color}

]

DEVICES = [

    {"name": 'TheMessTent',
     "IP": shh.messtent_ip,
     "build": 'Intel i9-13900k 96GB DDR5',
     "color": admin_color},

    {"name": 'ECHO',
     "IP": shh.echo_ip,
     "build": 'AMD Ryzen 5 7600 32GB DDR5',
     "color": echo_color},

     {"name": "YAVIN",
      "IP": shh.yavin_ip,
      "build": 'AMD Ryzen 5 5600 32GB ECC DDR4',
      "color": yavin_color},

    {"name": 'COSMO',
     "IP": shh.cosmo_ip,
     "build": 'Raspberry Pi 5',
     "color": cosmo_color},

    {"name": 'DARREN',
     "IP": shh.darren_ip,
     "build": 'Raspberry Pi 5',
     "color": darren_color},

    {"name": 'LOMEZ',
     "IP": shh.lomez_ip,
     "build": 'Raspberry Pi 5',
     "color": lomez_color},
    
    {"name": "BOBCOBB",
     "IP": shh.bob_ip,
     "build": 'Raspberry Pi Zero 2 W',
     "color": bobcobb_color}

]

SERVICES = [

    {"name": 'Router',
     "url": shh.router_link,
     "desc": shh.router_model,
     "home": shh.router_ip,
     "color": admin_color},

    {"name": 'Switch',
     "url": shh.switch_link,
     "desc": shh.switch_model,
     "home": shh.switch_ip,
     "color": admin_color},

    {"name": 'WiFi AP',
     "url": shh.ap_link,
     "desc": shh.ap_model,
     "home": shh.ap_ip,
     "color": admin_color},

    {"name": 'Hall Camera',
     "url": shh.cam_link,
     "desc": shh.cam_model,
     "home": shh.cam_ip,
     "color": bobcobb_color},

    {"name": 'Shiny',
     "url": shh.shiny_link,
     "home": shh.shiny_ip,
     "desc": 'Shiny apps that I use for data analysis',
     "color": echo_color},

    {"name": 'Ollama',
     "url": shh.lama_link,
     "home": shh.lama_ip,
     "desc": 'The Open-Web UI for local Ollama Models',
     "color": echo_color},

    {"name": 'Grafana',
     "url": shh.graf_link,
     "home": shh.graf_ip,
     "desc": 'Monitoring Dashboard',
     "color": echo_color},

    {"name": 'Prometheus',
     "url": shh.prom_link,
     "home": shh.prom_ip,
     "desc": 'Data Collection for Grafana',
     "color": echo_color},

    {"name": 'Guacamole',
     "url": shh.guac_link,
     "home": shh.guac_ip,
     "desc": 'Remote On In!',
     "color": echo_color},

    {"name": 'Cosmo The Budget Bot',
     "url": shh.bot_link,
     "home": shh.bot_ip,
     "desc": 'A Twilio app that I use for on-the-go data entry',
     "color": cosmo_color},

    {"name": 'Wiki.JS',
     "url": shh.wiki_link,
     "home": shh.wiki_ip,
     "desc": 'Documentation for my Postgres Database',
     "color": cosmo_color},

    {"name": 'Personal Website',
     "url": shh.mcor_link,
     "home": shh.mcor_ip,
     "desc": 'My personal website, still under construction',
     "color": cosmo_color},

    {"name": 'Grocy',
     "url": shh.groc_link,
     "home": shh.groc_ip,
     "desc": 'Home Grocery Inventory Management',
     "color": darren_color},

    {"name": 'Barcode Buddy',
     "url": shh.bb_link,
     "home": shh.bb_ip,
     "desc": 'Barcode Scanner Advanced Mode',
     "color": darren_color},

     {"name": 'My Resume',
     "url": shh.res_link,
     "home": shh.res_ip,
     "desc": 'My Digital Resume - UNDER CONSTRUCTION',
     "color": lomez_color},

    {"name": 'TrueNAS',
     "url": shh.nas_link,
     "home": shh.nas_ip,
     "desc": 'TrueNAS Login',
     "color": yavin_color},

    {"name": 'Plex',
     "url": shh.plex_link,
     "home": shh.plex_ip,
     "desc": 'My collection of Movies and TV Shows',
     "color": yavin_color},

]

@app.route('/')
def homepage():
    return render_template('homepage.html', 
                           services = SERVICES,
                           devices = DEVICES,
                           subnets = SUBNETS)

if __name__ == "__main__":
    app.run(host = shh.app_host, port = shh.app_port)
