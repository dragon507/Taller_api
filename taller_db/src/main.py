from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True


list = [
    {
        'id': 0,
        'Company': 'Microsoft azure',
        'What is azure': 'Azure es conjunto en constante expansión de servicios en la nube para ayudar a su organización a satisfacer sus necesidades comerciales.',
        'price': '152.62',
        'service':  'Virtual Machine'
    },
    {
        'id': 1,
        'Company': 'Amazon Web Services AWS',
        'What is AWS':'servicios de nube que proporciona una variedad de servicios de infraestructura',
        'price': '71.84',
        'Service': 'Amazon Ec2'
    },
    {
        'id': 2,
        'Company': 'Google',
        'What is Google Cloud':'una plataforma que ha reunido todas las aplicaciones de desarrollo web que Google estaba ofreciendo por separado. Es utilizada para crear ciertos tipos de soluciones a través de la tecnología almacenada en la nube',
        'price': '79.95',
        'Service': 'Cloud CDN'
    },
    {
        'id': 3,
        'Company': 'Alibaba Cloud',
        'What is Alibaba':'ofrece una gama de servicios de infraestructura, plataforma y aplicaciones en numerosas áreas. ',
        'price': '93.52',
        'Service': 'Amazon Ec2'
    },
    {
        'id': 4,
        'Company': 'IBM Cloud',
        'What is IBM Cloud':'IBM Cloud ofrece la nube pública más abierta y segura para los negocios, una plataforma híbrida multicloud de próxima generación',
        'price': '28.75',
        'Service': 'Cloud CDn'
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1> API con Flask <h1>"

@app.route('/api/v1/empresas', methods= ['GET'])
def service():
    return jsonify(list)

if __name__ =='__main__':
    app.run()